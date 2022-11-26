#Dynamixel XL430-W250 driver
Dynamixel XL430-W250 driver, based on Dynamixel SDK, written in Python.
1. First step for You is to download Dynamixel SDK from their GitHub.
2. Then in your file manager go to "/home/[your-user-name]/[path-to-your-downloaded-folder]/DynamixelServoXL430/DynamixelSDK_master/python", and open terminal. Run '''bash sudo python3 setup.py install'''
3. Now  you have succesfully installed setup and you can continue to work with the SDK.

#Important Registry Adresses
Here is a table of adresses that are used in this example.

|Name            |ADDR |  Value |Num of bytes TXRx|
|-------------------------------------------------|
|Goal Position   | 116 | 0-4095 |         4       |
|Torque          |  64 | 0 or 1 |         1       |
|LED             |  65 | 0 or 1 |         1       |
|Operating Mode  |  11 | 3 or 4 |         4       |
|Velocity        | 112 | xxxxxx |         4       |
