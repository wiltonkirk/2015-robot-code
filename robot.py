#!/usr/bin/env python3

import wpilib


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.joystick_right = wpilib.Joystick(0)
        self.joystick_left = wpilib.Joystick(1)

        self.motor_left = wpilib.Jaguar(0)
        self.motor_right = wpilib.Jaguar(1)

        self.motor_left_arm = wpilib.Jaguar(2)
        self.motor_right_arm = wpilib.Jaguar(3)

        self.drive_train = wpilib.RobotDrive(self.motor_left, self.motor_right)
        self.drive_train.setExpiration(0.2)

        self.light_relay = wpilib.Relay(0, wpilib.Relay.Direction.kForward)

    def autonomousInit(self):
        autonomous = True

    def teleopPeriodic(self):
        self.drive_train.arcadeDrive(self.joystick_right.getY(), self.joystick_left.getX())

        # Right Arm Motor
        if self.joystick_right.getRawButton(3):
            self.motor_right_arm.set(0.40)
        else:
            self.motor_right_arm.set(0.0)

        # Left Arm Motor
        if self.joystick_left.getRawButton(3):
            self.motor_left_arm.set(0.40)
        else:
            self.motor_left_arm.set(0.0)

        # Light (turns on with button 1, off with button 2)
        if self.joystick_right.getRawButton(1):
            self.light_relay.set(wpilib.Relay.Value.kForward)
        elif self.joystick_right.getRawButton(2):
            self.light_relay.set(wpilib.Relay.Value.kOff)

if __name__ == '__main__':
    wpilib.run(MyRobot)
