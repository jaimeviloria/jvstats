class Delays:

  def __init__(self, delays=[],width=3):

    #sets the initial width of the sliding window
    self.width = width

    # sets the initial list of delays
    self.delays = delays

    # sets the initial sliding window
    self.__sliding_window = self.getSlidingWindow(delays,width,len(delays))

  @property
  def delays(self):
    return self.__delays

  @property
  def width(self):
    return self.__width

  @property
  def sliding_window(self):
    return self.__sliding_window

  @delays.setter
  def delays(self, dls):

    # check that the delays set is either an integer or a list of integers
    if isinstance(dls,int):
      self.__delays = [dls]
    elif all(isinstance(x,int) for x in dls):
      self.__delays = dls
    else:
      raise TypeError("delays must either be integer or an array of integers")

    # set the new sliding window for stats
    self.__sliding_window = self.getSlidingWindow(self.__delays,self.__width,0)

  @width.setter
  def width(self,wdh):
    if isinstance(wdh,int):
      self.__width=wdh
    else:
      self.__width=None
      raise TypeError("width must be an integer")
  
  def addDelay(self,delay):
    '''
    Adds a delay value to the list of delays

    Parameters:
    delay (int,Array): the delay to add to the list of delays
 
    Returns:
    Array: The list of delays
    '''

    # check that the delay added is either an integer or list of integers
    if isinstance(delay,int):
      self.__delays.append(delay)
    elif all(isinstance(x,int) for x in delay):
      self.__delays+=delay
    else:
      raise TypeError("delay must be an integer or array of integers")

    # set the new sliding window for stats
    self.__sliding_window = self.getSlidingWindow(self.delays,self.width,0)

    return self.__delays

  @staticmethod
  def getSlidingWindow(delays=[],width=3,offset=0):
    if (len(delays) < width):
      return delays
    else:
      return delays[len(delays)-width:len(delays)]

   

