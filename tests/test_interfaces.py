import pytest
from pytest_mock import mocker
from jvstats import Delays
import os

# delays1 are the delays to add iteratively
# consequently all_delays1, sliding_windows1 and outputs1 are the expected delays, current window and median output respectively

# test for adding integers
delays1=[100,102,101,110,120,115]
all_delays1=[[100],[100,102],[100,102,101], [100,102,101,110],[100,102,101,110,120], [100,102,101,110,120,115]]
sliding_windows1=[[100],[100,102],[100, 102, 101],[102, 101, 110],[101, 110, 120],[110, 120, 115]]
outputs1=[[-1],[-1,101],[-1,101,102],[-1,101,102,110],[-1,101,102,110,115]]

# test for adding arrays
# expected sliding window is the latest
# however expected output is that of all the medians being calculated
delays2=[100,[102, 101, 110, 120, 115]]
all_delays2=[[100],[100,102,101,110,120,115]]
sliding_windows2=[[100],[110, 120, 115]]
outputs2=[[-1],[-1,101,102,110,115]]

# test for adding strings
delays3=[100,'a']
all_delays3=[[100],[100]]
sliding_windows3=[[100],[100]]
outputs3=[[-1],None]

# Test for setting delays directly
@pytest.mark.parametrize('delays,expected,outputs',[
  (100,[100],[-1]),
  ([100,102,101],[100, 102, 101],[-1,101,101]),
])
def test_set_delay(delays,expected,outputs):
  d = Delays([],3)
  
  # if delays is neither an integer or a list of integers then raise an error
  if (isinstance(delays,int) or all(isinstance(x,int) for x in delays)):
    d.delays=delays
  else:
    with pytest.raises(TypeError):
      d.delays=delays

  assert d.delays == expected

# Testing the addition of delays
@pytest.mark.parametrize('delays,all_delays',[
  (delays1,all_delays1),
  (delays2,all_delays2),
  (delays3,all_delays3),
])
def test_jvstats_addDelay(delays,all_delays):

  d = Delays([],3)

  # here we iterate over each element in the delays and then check if the corresponding list of delays is as expected
  for i,delay in enumerate(delays):


    # if delay is neither an integer or an array of integers, we expect a TypeError
    if (isinstance(delay,int) or (all(isinstance(x,int) for x in delay))):
      d.addDelay(delay)
    else:
      with pytest.raises(TypeError):
        d.addDelay(delay)

    # check that the list of delays is as expected
    assert d.delays == all_delays[i]


# testing the variable width of the window
@pytest.mark.parametrize('width',[(3),('a')])
def test_jvstats_delay_width(width):

  # if width is not an integer then we should expect a TypeError exception
  if not isinstance(width,int):
    with pytest.raises(TypeError):
      d=Delays([],width)
  else:
    d=Delays([],width)

# testing that we get the expected sliding windows on addition of each delay
@pytest.mark.parametrize('delays,sliding_windows',[
  (delays1,sliding_windows1),
  (delays2,sliding_windows2),
  (delays3,sliding_windows3),
])
def test_jvstats_sliding_window(delays,sliding_windows):

  d = Delays([],3)
  
  # here we iterate over each element in the delays and then check if the sliding window is as expected
  for i,delay in enumerate(delays):
    
    # addDelay the delay
    # if delay is neither an integer or an array of integers, we expect a TypeError
    if (isinstance(delay,int) or (all(isinstance(x,int) for x in delay))):
      d.addDelay(delay)
    else:
      with pytest.raises(TypeError):
        d.addDelay(delay)

    # check that the sliding window is as expected
    assert d.sliding_window == sliding_windows[i]

@pytest.mark.parametrize('all_delays,output',[
  ([100],[-1]),
  ([100,102,101,110,120,115],[-1,101,101,102,110,115]),
])
def test_jvstats_getMedian(all_delays,output):

  d = Delays([],3)
  d.delays=all_delays
  medians = d.get_Median()

  assert medians == output

