from dynamixel_sdk import *
import sys

#USB port used by U2D2
SERVO_PORT = "/dev/ttyUSB0"

portHandler = PortHandler(SERVO_PORT)
portHandler.openPort()
#Baud rate set via Wizard (default value is 57600)
portHandler.setBaudRate(57600)

handler = Protocol2PacketHandler()

#Disable torque in order to set operating mode
communication_result, servo_error = handler.write1ByteTxRx(portHandler, 1, 64, 0)
print("TORQUE : %s" % handler.getTxRxResult(communication_result))
if servo_error != 0:
    print("TORQUE : %s" % handler.getRxPacketError(servo_error))

mode = input("Choose mode single turn(s)/multiturn(m)")

#choosing operating mode
if(mode == "m"):
    print("Multi mode on")
    communication_result, servo_error = handler.write1ByteTxRx(portHandler, 1, 11, 4)
    print("MULTIMODE : %s" % handler.getTxRxResult(communication_result))
    if servo_error != 0:
        print("MULTIMODE : %s" % handler.getRxPacketError(servo_error))
else:
    print("Single mode on")
    communication_result, servo_error = handler.write1ByteTxRx(portHandler, 1, 11, 3)
    print("SINGLEMODE : %s" % handler.getTxRxResult(communication_result))
    if servo_error != 0:
        print("SINGLEMODE : %s" % handler.getRxPacketError(servo_error))

#enabling torque in order to set position goal and velocity
communication_result, servo_error = handler.write1ByteTxRx(portHandler, 1, 64, 1)
print("TORQUE : %s" % handler.getTxRxResult(communication_result))
if servo_error != 0:
    print("TORQUE : %s" % handler.getRxPacketError(servo_error))

while True:
    #turning the led off
    current_position = 10000000000000
    communication_result, servo_error = handler.write1ByteTxRx(portHandler, 1, 65, 0)
    print("LED : %s" % handler.getTxRxResult(communication_result))
    if servo_error != 0:
        print("LED : %s" % handler.getRxPacketError(servo_error))

    angle = int(input("Enter goal angle: "))
    angle = int((angle/360)*4095)
            
    speed = int(input("Enter speed: "))
    speed = int((speed/1023)*327.67)

    #setting velocity of Dynamixel
    communication_result, servo_error = handler.write4ByteTxRx(portHandler, 1, 112, speed)
    print("VELOCITY : %s" % handler.getTxRxResult(communication_result))
    if servo_error != 0:
        print("VELOCITY : %s" % handler.getRxPacketError(servo_error))

    #setting goal position angle (4095 = 360deg)
    communication_result, servo_error = handler.write4ByteTxRx(portHandler, 1, 116, int(angle))
    print("POSITION : %s" % handler.getTxRxResult(communication_result))
    if servo_error != 0:
        print("POSITION : %s" % handler.getRxPacketError(servo_error))

    #while the servo is moving LED will be turned on
    while(abs(current_position - angle) > 10):
        current_position,_,_ = handler.read4ByteTxRx(portHandler, 1, 132)
        communication_result, servo_error = handler.write1ByteTxRx(portHandler, 1, 65, 1)
        print("LED : %s" % handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("LED : %s" % handler.getRxPacketError(servo_error))

portHandler.closePort()
