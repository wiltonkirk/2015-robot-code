#!/usr/bin/env python3

import wpilib

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.joystick = wpilib.Joystick(0)

        self.left_motor = wpilib.Jaguar(0)
        self.right_motor = wpilib.Jaguar(1)

        self.drive_train = wpilib.RobotDrive(self.left_motor, self.right_motor)
        self.drive_train.setExpiration(0.2)

    def autonomousInit(self):
        autonomous = True

    def teleopPeriodic(self):
        self.drive_train.arcadeDrive(self.joystick)

if __name__ == '__main__':
    wpilib.run(MyRobot)
