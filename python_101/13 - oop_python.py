#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def talk(self):
        print(f"Hi Human! I'm {self.name} robot, have {self.color} color and type '{self.__class__.__name__}'")

    def walk(self):
        print(f'WALKING -> {self.name}')

    def stop(self):
        print(f'STOPPING -> {self.name}')


class IndustrialRobot(Robot):
    def __init__(self, name, color, tool):
        self.tool = tool
        Robot.__init__(self, name, color)

    # Override method
    def talk(self):
        print(
            f"Hi Human! I'm {self.name} robot, have {self.color} color, type '{self.__class__.__name__}' and {self.tool} tool!")


class AIRobot(Robot):
    def __init__(self, name, color, brain):
        self.brain = brain
        Robot.__init__(self, name, color)

    # New method
    def eliminate_humans(self):
        print('Yeah! Just kill everyone!')

def main():
    print('[+] Using Robot base class [+]')
    # Creating instances
    robot_1 = Robot('George', 'red')
    robot_2 = Robot('Bob', 'blue')

    # Using methods
    robot_1.walk()
    robot_1.talk()
    robot_2.walk()
    robot_2.talk()
    robot_2.stop()
    robot_1.stop()

    # Accessing attributes
    print(robot_1.name)
    print(robot_2.name)

    print('\n[+] Using derived IndustrialRobot and AIRobot class [+]')

    # Creating instances
    industrial_robot = IndustrialRobot('Xpto', 'green', 'hammer')
    ai_robot = AIRobot('T1000', 'red', 'Neural circuit')

    # Using methods
    industrial_robot.walk()
    industrial_robot.talk()
    ai_robot.talk()
    ai_robot.walk()
    ai_robot.stop()
    industrial_robot.stop()

if __name__ == "__main__":
    main()
