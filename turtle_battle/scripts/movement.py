#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from turtlesim.srv import Spawn


from pynput import keyboard
from pynput.keyboard import Key

pub1 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
pub2 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
attack_pub1 = rospy.Publisher('/turtle1/attack', Bool, queue_size=10)
attack_pub2 = rospy.Publisher('/turtle2/attack', Bool, queue_size=10)


def on_key_press(key):
    if key == Key.right:
        vel2.angular.z = -angular_velocity
    elif key == Key.left:
        vel2.angular.z = angular_velocity
    elif key == Key.up:
        vel2.linear.x = linear_velocity
    elif key == Key.down:
        vel2.linear.x = -linear_velocity
    elif key.char == 'w':
        vel1.linear.x = linear_velocity
    elif key.char == 's':
        vel1.linear.x = -linear_velocity
    elif key.char == 'a':
        vel1.angular.z = angular_velocity
    elif key.char == 'd':
        vel1.angular.z = -angular_velocity
    elif key.char == 'q':
        attack1 = True
        attack_pub1.publish(attack1)
    elif key.char == 'k':
        attack2 = True
        attack_pub2.publish(attack2)


    pub1.publish(vel1)
    pub2.publish(vel2)

def on_key_release(key):
    if key == Key.right:
        vel2.angular.z = 0
    elif key == Key.left:
        vel2.angular.z = 0
    elif key == Key.up:
        vel2.linear.x = 0
    elif key == Key.down:
        vel2.linear.x = 0
    elif key.char == 'w':
        vel1.linear.x = 0
    elif key.char == 's':
        vel1.linear.x = 0
    elif key.char == 'a':
        vel1.angular.z = 0
    elif key.char == 'd':
        vel1.angular.z = 0
    elif key.char == 'q':
        attack1 = False
        attack_pub1.publish(attack1)
    elif key.char == 'k':
        attack2 = False
        attack_pub2.publish(attack2)


    pub1.publish(vel1)
    pub2.publish(vel2)

def spawnTurtle(x, y, theta, name):
    rospy.wait_for_service('/spawn')
    try:
        spawn = rospy.ServiceProxy('/spawn', Spawn) 
        spawn(x, y, theta, name)
    except rospy.ServiceException as e:
        pass



def move(linear_velocity_, angular_velocity_):
    global linear_velocity
    linear_velocity = linear_velocity_
    global angular_velocity
    angular_velocity = angular_velocity_
    
    rate = rospy.Rate(10)
    global vel1
    vel1 = Twist()
    global vel2 
    vel2 = Twist()
    global attack1
    attack1 = Bool()
    global attack2
    attack2 = Bool()


    vel1.linear.x = 0
    vel1.linear.y = 0
    vel1.linear.z = 0
    vel1.angular.x = 0 
    vel1.angular.y = 0 
    vel1.angular.z = 0

    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release, suppress=True) as listener:
        listener.join() 



   

    
if __name__ == '__main__':
    rospy.init_node('game_controller', anonymous= True)
    spawnTurtle(5, 5, 0, 'turtle2')
    move(3.0, 4.0)
    
