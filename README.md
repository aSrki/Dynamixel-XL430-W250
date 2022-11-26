#Dynamixel XL430-W250 driver
  Dynamixel XL430-W250 driver, based on Dynamixel SDK, written in Python.
  1. First step for You is to download Dynamixel SDK from their GitHub.
  2. Then in your file manager go to "/home/[your-user-name]/[path-to-your-downloaded-folder]/DynamixelServoXL430/DynamixelSDK_master/python", and open terminal. Run '''bash sudo python3 setup.py install'''
  3. Now  you have succesfully installed setup and you can continue to work with the SDK.

#Useful Registry Adresses
  Here is a table of adresses that are used in this example.

|Name            |ADDR |  Value |Num of bytes TXRx| Comment
|----------------|-----|--------|-----------------|-------------------------------------------------------------------------------------------------------|
|Goal Position   | 116 | 0-4095 |         4       | -or in case of multiturn mode -2,147,483,648 - 2,147,483,647                                          |
|Torque          |  64 | 0 or 1 |         1       |                                                                                                       |
|LED             |  65 | 0 or 1 |         1       |                                                                                                       |
|Operating Mode  |  11 | 3 or 4 |         4       | - 3 is used for single turn(0-4095), and 4 for multiturn mode (-2,147,483,648 - 2,147,483,647)        |
|Velocity        | 112 | xxxxxx |         4       | - This parameter edits the profile which velocity follows, see official Dynamixel website for details.|
