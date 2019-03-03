import pytest
from pytest_mock import mocker
from getstats import Delays
import os

delays1=[100,102,101,112,115]
all_delays1=[[100],[100,102],[100,102,101],[100,102,101,112],[100,102,101,112,115]]
sliding_windows1=[[100],[100,102],[100,102,101],[102,101,110],[110,120,115]]
outputs1=[-1,101,101,102,110,115]

@pytest.mark.parametrize('delays,all_delays',[
  (delays1,all_delays1),
])
def test_getstats_addDelay(delays,all_delays):

  d = Delays()

  # here we iterate over each element in the delays and then check if the corresponding list of delays is as expected
  for i,delay in enumerate(delays):

    # addDelay the delay
    d.addDelay(delay)

    # check that the list of delays is as expected
    assert d.delays == all_delays[i]

@pytest.mark.parametrize('delays,sliding_windows',[
  (delays1,sliding_windows1),
])
def test_getstats_sliding_window(delays,sliding_windows):

  d = Delays()
  
  # here we iterate over each element in the delays and then check if the sliding window is as expected
  for i,delay in enumerate(delays):
    
    # addDelay the delay
    d.addDelay(delay)

    # check that the sliding window is as expected
    assert d.sliding_window == sliding_windows[i]

@pytest.mark.parametrize('sliding_windows,outputs',[
  (sliding_windows1,outputs1),
])
def test_getstats_getMedian(mocker,sliding_windows,outputs):

  d = Delays()

  # we are not interested in whether sliding_window is properly functioning
  # only that it is of the value that we want to test
  mocker.patch.object(Delays,'sliding_window')

  # we iterate over each element in the sliding_windows to test
  for i,sliding_window in enumerate(sliding_windows):
    Delays.sliding_window.return_value=sliding_window

    # check that the median is as expected of the given sliding window
    assert d.get_Median() == outputs[i]

