import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu  # Added IMU sensor input
from std_msgs.msg import Bool
import math

class RobotNavigator:
    def __init__(self):
        rospy.init_node('robot_navigator', anonymous=True)
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.ball_detected_sub = rospy.Subscriber('/blue_ball_detector', Bool, self.ball_detected)  #subscribe to the camera results
        self.imu_sub = rospy.Subscriber('/imu', Imu, self.imu_callback)  # Subscribe to IMU sensor

        self.robot_x = 0
        self.robot_y = 0.22
        self.ball_detected = False
        self.rotate_angle = 0
        self.current_orientation = 0  # Stores the current orientation from the IMU

    def odom_callback(self, msg):
        # Get robot's position from odom
        self.robot_x = msg.pose.pose.position.x
        self.robot_y = msg.pose.pose.position.y
        rospy.loginfo("Current position: x={}, y={}".format(self.robot_x, self.robot_y))
        self.check_zone()

    def imu_callback(self, msg):
        # Convert quaternion to Euler angles to get yaw (rotation around z-axis)
        orientation_q = msg.orientation
        siny_cosp = 2 * (orientation_q.w * orientation_q.z + orientation_q.x * orientation_q.y)
        cosy_cosp = 1 - 2 * (orientation_q.y * orientation_q.y + orientation_q.z * orientation_q.z)
        self.current_orientation = math.atan2(siny_cosp, cosy_cosp)

    def rotate_180(self):
        # Rotate 180 degrees
        twist = Twist()
        target_angle = (self.current_orientation + math.pi) % (2 * math.pi)
        while abs(angle_diff(self.current_orientation, target_angle)) > 0.1:  # Rotate until the target is reached
            twist.angular.z = 0.5  # Adjust rotation speed
            self.cmd_vel_pub.publish(twist)
            rospy.sleep(0.1)
        twist.angular.z = 0
        self.cmd_vel_pub.publish(twist)
        self.search_ball()

    def return_to_start(self):
        # Move back to the original starting position (0, 0.22)
        twist = Twist()
        while abs(self.robot_x - 0) > 0.1 or abs(self.robot_y - 0.22) > 0.1:
            twist.linear.x = -0.2  # Move backward
            self.cmd_vel_pub.publish(twist)
            rospy.sleep(0.1)
        twist.linear.x = 0
        self.cmd_vel_pub.publish(twist)
        self.rotate_180()
    def move(self):
        twist = Twist()
        twist.linear.x = 0.3
        self.cmd_vel_pub.publish(twist)
        rospy.sleep(0.1)
        twist.linear.x=0
        self.cmd_vel_pub.publish(twist)
        self.check_zone()
    def search_ball(self):
        # rotates 10 degrees to detect the ball
        twist = Twist()
        target_angle = (self.current_orientation + math.radians(10)) % (2 * math.pi)

        while abs(self.current_orientation - target_angle) > 0.1:
            if self.ball_detected:
                rospy.loginfo("Ball detected! Stopping rotation.")
                self.move()
                

            twist.angular.z = 0.5  # Set rotation speed
            self.cmd_vel_pub.publish(twist)
            rospy.sleep(0.1)

        twist.angular.z = 0  # Stop rotation
        self.cmd_vel_pub.publish(twist)

    def check_zone(self):
        if self.robot_y > 1.1:  # the red line
            rospy.loginfo("Reached red line, rotating 180 degrees")
            self.rotate_180()  # Rotate 180 degrees away
        elif self.robot_x == -0.95 or self.robot_x == 0.95:         # boundaries
            rospy.loginfo("Reached boundary, rotating 180 degrees")
            self.rotate_180()  # Rotate 180 degrees away
        elif 0.8 < self.robot_x < 1 and 0.2 < self.robot_y < 0.4:   # positive penalty zone
            rospy.loginfo("Reached positive penalty zone, returning to start position")
            self.return_to_start()  # Return to original position
        elif -1 < self.robot_x < -0.8 and 0.2 < self.robot_y < 0.4:  # negative penalty zone
            rospy.loginfo("Reached negative penalty zone, returning to start position")
            self.return_to_start()  # Return to original position
        elif -0.4 < self.robot_x < 0.4 and 0 < self.robot_y < 0.2:  # green zone
            rospy.loginfo("Reached green zone")
            self.return_to_start()
        else:
            if not self.ball_detected:
                self.search_ball()

if __name__ == '__main__':
    try:
        navigator = RobotNavigator()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
