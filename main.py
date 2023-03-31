#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile

# Initialize the EV3 Brick.
ev3 = EV3Brick()
motor = Motor(Port.A)
# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.D)
# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=109)
def pickUp():
    motor.run_angle(460,1900,wait=True)

def putDown():
    motor.run_angle(460,-1900,wait=True)
while True:
    ev3.speaker.say("pv yk bschk pv zk pv")
"""
robot.turn(90)
robot.turn(-90)
ev3.speaker.beep()
wait(2000)
ev3.speaker.play_file(SoundFile.CAT_PURR)
robot.turn(-90)
robot.turn(90)
putDown()
"""
"""
while True:
    pickUp()
    wait(2000)
    putDown()
    wait(2000)
"""





