## Dynamixel XL430-W250 driver
  Dynamixel XL430-W250 driver, based on Dynamixel SDK, written in Python.
  1. First step for You is to download Dynamixel SDK from their GitHub.
  2. Then in your file manager go to /home/[your-user-name]/[path-to-your-downloaded-folder]/DynamixelServoXL430/DynamixelSDK_master/python, and open terminal. Run ```console bash sudo python3 setup.py install ```
  3. Now  you have succesfully installed setup and you can continue to work with the SDK.

## Useful Registry Adresses
  Here is a table of registry adresses that are used in this project.

|Name            |ADDR |  Value |Num of bytes TXRx| Comment
|----------------|-----|--------|-----------------|-------------------------------------------------------------------------------------------------------|
|Goal Position   | 116 | 0-4095 |         4       | -or in case of multiturn mode -2,147,483,648 - 2,147,483,647                                          |
|Torque          |  64 | 0 or 1 |         1       |                                                                                                       |
|LED             |  65 | 0 or 1 |         1       |                                                                                                       |
|Operating Mode  |  11 | 3 or 4 |         4       | - 3 is used for single turn(0-4095), and 4 for multiturn mode (-2,147,483,648 - 2,147,483,647)        |
|Velocity        | 112 | xxxxxx |         4       | - This parameter edits the profile which velocity follows, see official Dynamixel website for details.|

## Code structure
  It is important to mention that the order of apperance of parts of code is EXTREMLY important (ask me how i know...) so if you change anything be aware that some errors may occure because of that.
  
### Order of operation
- First and foremost, Torque enabled must be set to 0 in order to choose Operating mode. 
- Then, after choosing the mode (Single-turn or Multi-turn) you can set the Tourque enabled to 1.
- Because I wanted the LED to be turned on while Dynamixel is turning, firstly it needs to be turned off, and then after setting Goal position, LED turns on and code checks if Dynamixel has achieved given position, and if it is within giver error (10 pulses / 0.88 deg) the LED turns off again.

  
 Happy coding :)
