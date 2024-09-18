import rospy
from sensor_msgs.msg import Image, Imu
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

# Define HSV color ranges for red and green detection
# These ranges may need adjustment based on your specific lighting conditions and camera calibration
RED_LOW = np.array([0, 100, 100])
RED_HIGH = np.array([10, 255, 255])

GREEN_LOW = np.array([35, 100, 100])
GREEN_HIGH = np.array([85, 255, 255])

bridge = CvBridge()

def camera_rgb_callback(data):
    try:
        # Convert ROS image message to OpenCV image
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        
        # Convert BGR image to HSV color space
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        
        # Create masks for red and green colors
        red_mask = cv2.inRange(hsv_image, RED_LOW, RED_HIGH)
        green_mask = cv2.inRange(hsv_image, GREEN_LOW, GREEN_HIGH)
        
        # Check if there is any red or green detected
        if np.any(red_mask):
            rospy.loginfo("Detected penalty zone (red area)")
        elif np.any(green_mask):
            rospy.loginfo("Detected goal area (green area)")
        else:
            rospy.loginfo("No restricted zones detected")
    
    except CvBridgeError as e:
        rospy.logerr("CvBridge error: %s", str(e))

def imu_callback(data):
    rospy.loginfo("Received IMU data")

def odom_callback(data):
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    if is_in_penalty_zone(x, y) or is_in_goal_area(x, y):
        rospy.loginfo("Warning: Robot is in a restricted zone!")
        stop_robot()
    elif is_in_permitted_zone(x, y):
        move_robot()

def is_in_zone(x, y, zone):
    x_min, y_min, length, width = zone
    return x_min <= x <= x_min + length and y_min <= y <= y_min + width

def is_in_permitted_zone(x, y):
    # Define goal areas and penalty zones here
    for goal_area in GOAL_AREAS:
        if is_in_zone(x, y, goal_area):
            return False
    for penalty_zone in PENALTY_ZONES:
        if is_in_zone(x, y, (*penalty_zone, PENALTY_ZONE_SIZE, PENALTY_ZONE_SIZE)):
            return False
    return 0 <= x <= FIELD_LENGTH / 2 and 0 <= y <= FIELD_WIDTH

def is_in_penalty_zone(x, y):
    for penalty_zone in PENALTY_ZONES:
        if is_in_zone(x, y, (*penalty_zone, PENALTY_ZONE_SIZE, PENALTY_ZONE_SIZE)):
            return True
    return False

def is_in_goal_area(x, y):
    for goal_area in GOAL_AREAS:
        if is_in_zone(x, y, goal_area):
            return True
    return False

def move_robot():
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 0.5
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.loginfo("Moving robot forward")

def stop_robot():
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    velocity_publisher.publish(vel_msg)
    rospy.loginfo("Stopping robot due to restricted zone")

def main():
    rospy.init_node('robot_controller', anonymous=True)
    rospy.Subscriber("/camera/rgb/image_raw", Image, camera_rgb_callback)
    rospy.Subscriber("/imu", Imu, imu_callback)
    rospy.Subscriber("/odom", Odometry, odom_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
