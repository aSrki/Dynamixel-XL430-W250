from dynamixel_sdk import *
import sys
import time

test = False

if(test):
    while True:

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

        #turning the led off
        current_position = 10000000000000

        id = int(input("Enter ID: "))

        angle = int(input("Enter goal angle: "))
        angle = int((angle/360)*4095)
                
        speed = int(input("Enter speed: "))
        speed = int((speed/1023)*327.67)

        #setting velocity of Dynamixel
        communication_result, servo_error = handler.write4ByteTxRx(portHandler, id, 112, speed)
        print("VELOCITY : %s" % handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("VELOCITY : %s" % handler.getRxPacketError(servo_error))

        #setting goal position angle (4095 = 360deg)
        communication_result, servo_error = handler.write4ByteTxRx(portHandler, id, 116, int(angle))
        print("POSITION : %s" % handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("POSITION : %s" % handler.getRxPacketError(servo_error))

        #while the servo is moving LED will be turned on
        while(abs(current_position - angle) > 10):
            current_position,_,_ = handler.read4ByteTxRx(portHandler, id, 132)
            communication_result, servo_error = handler.write1ByteTxRx(portHandler, id, 65, 1)
            print("LED : %s" % handler.getTxRxResult(communication_result))
            if servo_error != 0:
                print("LED : %s" % handler.getRxPacketError(servo_error))

        communication_result, servo_error = handler.write1ByteTxRx(portHandler, id, 65, 0)
        print("LED : %s" % handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("LED : %s" % handler.getRxPacketError(servo_error))

class ServoXL430:

    id = 0
    speed = 0
    angle = 0
    mode = "s"
    portHandler = None
    handler = None

    def __init__(self, id, speed = 1023, mode = "s"):
        self. id = id
        self.speed = speed
        self.mode = mode

        #USB port used by U2D2
        SERVO_PORT = "/dev/ttyUSB0"

        self.portHandler = PortHandler(SERVO_PORT)
        self.portHandler.openPort()
        #Baud rate set via Wizard (default value is 57600)
        self.portHandler.setBaudRate(57600)

        self.handler = Protocol2PacketHandler()

        #Disable torque in order to set operating mode
        communication_result, servo_error = self.handler.write1ByteTxRx(self.portHandler, id, 64, 0)
        print("TORQUE : %s" % self.handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("TORQUE : %s" % self.handler.getRxPacketError(servo_error))

        #choosing operating mode
        if(self.mode == "m"):
            print("Multi mode on")
            communication_result, servo_error = self.handler.write1ByteTxRx(self.portHandler, id, 11, 4)
            print("MULTIMODE : %s" % self.handler.getTxRxResult(communication_result))
            if servo_error != 0:
                print("MULTIMODE : %s" % self.handler.getRxPacketError(servo_error))
        else:
            print("Single mode on")
            communication_result, servo_error = self.handler.write1ByteTxRx(self.portHandler, id, 11, 3)
            print("SINGLEMODE : %s" % self.handler.getTxRxResult(communication_result))
            if servo_error != 0:
                print("SINGLEMODE : %s" % self.handler.getRxPacketError(servo_error))

        #enabling torque in order to set position goal and velocity
        communication_result, servo_error = self.handler.write1ByteTxRx(self.portHandler, id, 64, 1)
        print("TORQUE : %s" % self.handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("TORQUE : %s" % self.handler.getRxPacketError(servo_error))

    def __del__(self):
        self.portHandler.closePort()

    def rotate(self, *args):
        if len(args) == 1:
            velocity = self.speed
            sleep = 0
        if len(args) == 2:  
            velocity = int(args[1])
            sleep = 0
        if len(args) == 3:
            velocity = int(args[1])
            sleep = int(args[2])

        current_position = 10000000000000
        servo_angle = int((int(args[0])/360)*4095)
        servo_speed = int(((velocity*10.23)/1023)*327.67)

        #setting velocity of Dynamixel
        communication_result, servo_error = self.handler.write4ByteTxRx(self.portHandler, self.id, 112, servo_speed)
        print("VELOCITY : %s" % self.handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("VELOCITY : %s" % self.handler.getRxPacketError(servo_error))

        #setting goal position angle (4095 = 360deg)
        communication_result, servo_error = self.handler.write4ByteTxRx(self.portHandler, self.id, 116, servo_angle)
        print("POSITION : %s" % self.handler.getTxRxResult(communication_result))
        if servo_error != 0:
            print("POSITION : %s" % self.handler.getRxPacketError(servo_error))

        #while the servo is moving LED will be turned on
        while(abs(current_position - servo_angle) > 10):
            current_position,_,_ = self.handler.read4ByteTxRx(self.portHandler, self.id, 132)
            communication_result, servo_error = self.handler.write1ByteTxRx(self.portHandler, self.id, 65, 1)
            #print("LED ON: %s" % self.handler.getTxRxResult(communication_result))
            #if servo_error != 0:
            #    print("LED ON: %s" % self.handler.getRxPacketError(servo_error))

        communication_result, servo_error = self.handler.write1ByteTxRx(self.portHandler, self.id, 65, 0)
        #print("LED : %s" % self.handler.getTxRxResult(communication_result))
        #if servo_error != 0:
        #    print("LED : %s" % self.handler.getRxPacketError(servo_error))

        time.sleep(sleep/1000)