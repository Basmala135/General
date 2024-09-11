import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2, sqrt, cos, sin

# PID gains
Kp_lin = 0.5
Ki_lin = 0.0
Kd_lin = 0.1

Kp_ang = 1.0
Ki_ang = 0.0
Kd_ang = 0.1

# Velocity limits
MAX_LINEAR_VELOCITY = 0.5
MAX_ANGULAR_VELOCITY = 1.0

# Thresholds
POSITION_THRESHOLD = 0.1
ORIENTATION_THRESHOLD = 0.1

# Time step for kinematic model
dt = 0.1

# Initialize global variables
current_x = 0.0
current_y = 0.0
current_theta = 0.0
target_x = 2.0
target_y = 2.0
target_theta = 0.0

# Initialize previous errors and integrals
prev_error_lin = 0.0
prev_error_ang = 0.0
integral_lin = 0.0
integral_ang = 0.0

def odom_callback(msg):
    global current_x, current_y, current_theta
    current_x = msg.pose.pose.position.x
    current_y = msg.pose.pose.position.y
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (_, _, current_theta) = euler_from_quaternion(orientation_list)

def compute_pid():
    global prev_error_lin, prev_error_ang, integral_lin, integral_ang, current_x, current_y, current_theta

    error_lin = sqrt((target_x - current_x)**2 + (target_y - current_y)**2)
    desired_theta = atan2(target_y - current_y, target_x - current_x)
    error_ang = desired_theta - current_theta

    control_signal_lin = Kp_lin * error_lin + Ki_lin * integral_lin + Kd_lin * (error_lin - prev_error_lin)
    integral_lin += error_lin
    prev_error_lin = error_lin

    control_signal_ang = Kp_ang * error_ang + Ki_ang * integral_ang + Kd_ang * (error_ang - prev_error_ang)
    integral_ang += error_ang
    prev_error_ang = error_ang

    # Limit velocities
    control_signal_lin = min(max(control_signal_lin, -MAX_LINEAR_VELOCITY), MAX_LINEAR_VELOCITY)
    control_signal_ang = min(max(control_signal_ang, -MAX_ANGULAR_VELOCITY), MAX_ANGULAR_VELOCITY)

    # Calculate linear and angular velocities using kinematic model
    v = control_signal_lin
    omega = control_signal_ang

    # Update TurtleBot's position and orientation
    current_x += v * cos(current_theta) * dt
    current_y += v * sin(current_theta) * dt
    current_theta += omega * dt

    return v, omega

def main():
    rospy.init_node('pid_controller_no_oop', anonymous=True)
    rospy.Subscriber('/odom', Odometry, odom_callback)
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        v, omega = compute_pid()

        if abs(v) < POSITION_THRESHOLD and abs(omega) < ORIENTATION_THRESHOLD:
            v = 0.0
            omega = 0.0

        vel_msg = Twist()
        vel_msg.linear.x = v
        vel_msg.angular.z = omega

        cmd_vel_pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
