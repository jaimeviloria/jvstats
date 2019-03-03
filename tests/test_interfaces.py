import pytest
from pytest_mock import mocker
from getstats import Delays
import os


# delays1 are the delays to add iteratively
# consequently all_delays1, sliding_windows1 and outputs1 are the expected delays, current window and median output respectively

# test for adding integers
delays1=[100, 102, 101, 110, 120, 115]
all_delays1=[[100],[100,102],[100,102,101], [100,102,101,110],[100,102,101,110,120], [100,102,101,110,120,115]]
sliding_windows1=[[100],[100,102],[100, 102, 101],[102, 101, 110],[101, 110, 120],[110, 120, 115]]
outputs1=[-1,101,101,102,110,115]

# test for adding arrays
# expected sliding window is the latest
# however expected output is that of all the medians being calculated
delays2=[100,[102, 101, 110, 120, 115]]
all_delays2=[[100],[100,102,101,110,120,115]]
sliding_windows2=[[100],[110, 120, 115]]
outputs2=[-1,101,101,102,110,115]

# test for adding strings
delays2=[100,'a']
all_delays2=[[100],[100]]
sliding_windows2=[[100],[100]]
outputs2=[-1,-1]

# Testing the addition of delays
@pytest.mark.parametrize('delays,all_delays',[
  (delays1,all_delays1),
  (delays2,all_delays2),
])
def test_getstats_addDelay(delays,all_delays):

  d = Delays([],3)

  # here we iterate over each element in the delays and then check if the corresponding list of delays is as expected
  for i,delay in enumerate(delays):

    # addDelay the delay
    d.addDelay(delay)

    # check that the list of delays is as expected
    assert d.delays == all_delays[i]

@pytest.mark.parametrize('delays,sliding_windows',[
  (delays1,sliding_windows1),
  (delays2,sliding_windows2)
])
def test_getstats_sliding_window(delays,sliding_windows):

  d = Delays([],3)
  
  # here we iterate over each element in the delays and then check if the sliding window is as expected
  for i,delay in enumerate(delays):
    
    # addDelay the delay
    d.addDelay(delay)

    # check that the sliding window is as expected
    assert d.sliding_window == sliding_windows[i]

@pytest.mark.parametrize('sliding_windows,outputs',[
  (sliding_windows1,outputs1),
  (sliding_windows2,outputs2),
])
def test_getstats_getMedian(mocker,sliding_windows,outputs):

  d = Delays([],3)

  # we are not interested in whether sliding_window is properly functioning
  # only that it is of the value that we want to test
  mocker.patch.object(Delays,'sliding_window')

  # we iterate over each element in the sliding_windows to test
  for i,sliding_window in enumerate(sliding_windows):
    Delays.sliding_window.return_value=sliding_window

    # check that the median is as expected of the given sliding window
    assert d.get_Median() == outputs[i]

