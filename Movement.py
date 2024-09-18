import rospy
from sensor_msgs.msg import Image, Imu
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

def camera_callback(data):
    rospy.loginfo("Received camera data")

def imu_callback(data):
    rospy.loginfo("Received IMU data")

def odom_callback(data):
    rospy.loginfo("Received odometry data")

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

def main():
    rospy.init_node('robot_controller', anonymous=True)

    rospy.Subscriber("/camera/rgb/image_raw", Image, camera_callback)
    rospy.Subscriber("/imu", Imu, imu_callback)
    rospy.Subscriber("/odom", Odometry, odom_callback)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        move_robot()
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
