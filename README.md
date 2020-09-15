# QuadSevenSegmentDisplay
Python and C++ based SAA1064 (4-digit LED-driver with I2C-Bus interface) Display Application

-Unit tests-
The unit tests provided by  unitTest_SevenSegment.py use the simulated smbus class which will work on Windows, but for Raspberry PI the unit test will try to use the real smbus module, which doesn't have special call to reset the simulator (see resetWriteFlag()). 
If you want to run the unit test on a raspberry pi you will need to ensure both the unitTest_SevenSegment.py and the SevenSegment.py files use the simulated smbus.... i.e import classes.smbus as smbus .

-7SegmentSimulation.py- 
This is a tester uses a GUI based on Tkinter. Added for those curious about Python GUI work.

-displayTester.py-
This is an example of how to use SevenSegment.py and its SevenSegmentDisplay class

optional arguments:

  -h, --help            show this help message and exit
  
  -d DISPLAYID, --displayID DISPLAYID the display ID/number to use
  
  --countUp             The count up switch
  
  -c COUNTVAL, --countVal COUNTVAL  The count start value
  
  -i, --interactive     Interactive mode

Hope this might be useful to someone out there.
