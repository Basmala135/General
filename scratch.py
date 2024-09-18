#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import cv2
import numpy as np
from cv_bridge import CvBridge

# Global variables
kinect_rgb_image = None


# Kinect RGB image callback
def kinect_rgb_callback(msg):
    global kinect_rgb_image
    bridge = CvBridge()
    kinect_rgb_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')


# Detect the green goal area in the RGB image
def detect_green_goal(rgb_image):
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)

    # Define the HSV range for detecting green
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([70, 255, 255])

    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Find contours of the green area
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find the largest green area (goal)
        largest_contour = max(contours, key=cv2.contourArea)

        # Get the center of the green area
        M = cv2.moments(largest_contour)
        if M['m00'] > 0:
            center_x = int(M['m10'] / M['m00'])
            center_y = int(M['m01'] / M['m00'])
            return (center_x, center_y)  # Return the center of the goal
    return None


# Adjust the robot’s position based on the goal's position in the image
def adjust_position_to_goal(goal_position, image_width):
    if goal_position is None:
        print("No goal detected")
        return None

    goal_x, _ = goal_position
    center_of_frame = image_width / 2

    if goal_x < center_of_frame - 50:  # Add a tolerance
        return 'left'
    elif goal_x > center_of_frame + 50:
        return 'right'
    else:
        return 'straight'


# Move the robot based on alignment and shoot the ball with gradual acceleration
def move_and_shoot(robot_orientation, velocity_publisher, shoot_velocity):
    twist = Twist()

    # Acceleration parameters
    acceleration_step = 0.1  # Increment of velocity each step
    max_velocity = shoot_velocity
    acceleration_time = 2.0  # Duration to reach max velocity in seconds
    shooting_duration = 0.5  # Duration to shoot in seconds
    stop_time = 0.5  # Time to decelerate to stop after shooting

    if robot_orientation == 'left':
        twist.angular.z = 0.5  # Turn left
        velocity_publisher.publish(twist)

    elif robot_orientation == 'right':
        twist.angular.z = -0.5  # Turn right
        velocity_publisher.publish(twist)

    elif robot_orientation == 'straight':
        # Gradual acceleration
        current_velocity = 0
        start_time = rospy.get_time()
        while rospy.get_time() - start_time < acceleration_time:
            current_velocity = min(max_velocity, current_velocity + acceleration_step)
            twist.linear.x = current_velocity
            velocity_publisher.publish(twist)
            rospy.sleep(0.1)

        # Maintain max velocity for shooting
        twist.linear.x = max_velocity
        velocity_publisher.publish(twist)
        rospy.sleep(shooting_duration)  # Shoot for the specified duration

        # Gradual deceleration
        start_time = rospy.get_time()
        while rospy.get_time() - start_time < stop_time:
            current_velocity = max(0, current_velocity - acceleration_step)
            twist.linear.x = current_velocity
            velocity_publisher.publish(twist)
            rospy.sleep(0.1)

        # Final stop
        stop_robot(velocity_publisher)
        print("Shot the ball!")


# Stop the robot
def stop_robot(publisher):
    twist = Twist()
    twist.linear.x = 0
    twist.angular.z = 0
    publisher.publish(twist)


def robot_control():
    rospy.init_node('robot_controller')

    # Initialize ROS topics
    rospy.Subscriber('/camera/rgb/image_raw', Image, kinect_rgb_callback)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if kinect_rgb_image is not None:
            goal_position = detect_green_goal(kinect_rgb_image)
            image_width = kinect_rgb_image.shape[1]
            robot_orientation = adjust_position_to_goal(goal_position, image_width)

            if robot_orientation:
                move_and_shoot(robot_orientation, velocity_publisher, shoot_velocity=1.0)

        rate.sleep()


if __name__ == '__main__':
    try:
        robot_control()
    except rospy.ROSInterruptException:
        pass
