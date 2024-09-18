#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
from ultralytics import YOLO

class BlueBallDetector:
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node('blue_ball_detector', anonymous=True)

        # Create CvBridge object to convert ROS Image messages to OpenCV format
        self.bridge = CvBridge()

        # Subscribe to the RGB camera topic
        self.rgb_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.rgb_callback)

        # Publisher to publish detection results (True if blue ball detected, False otherwise)
        self.detect_pub = rospy.Publisher("/blue_ball_detected", Bool, queue_size=10)

        # Load YOLOv8 model from ultralytics
        self.model = YOLO('yolov8n.pt')  # Using the pre-trained YOLOv8n model

        # Threshold for blue detection
        self.lower_blue = np.array([100, 150, 0])
        self.upper_blue = np.array([140, 255, 255])

    def rgb_callback(self, rgb_msg):
        try:
            # Convert the ROS image message to an OpenCV image (BGR format)
            frame = self.bridge.imgmsg_to_cv2(rgb_msg, "bgr8")
        except CvBridgeError as e:
            rospy.logerr(f"CvBridge Error: {e}")
            return

        # Run YOLO detection on the frame
        results = self.model(frame)

        # Filter YOLO results and check if a blue ball is detected
        detected = self.detect_blue_ball(results, frame)

        # Publish the result of the detection
        self.detect_pub.publish(detected)

        if detected:
            rospy.loginfo("Blue ball detected!")
        else:
            rospy.loginfo("No blue ball detected.")

        # Optionally, visualize the frame with detections
        cv2.imshow("YOLO Detection", frame)
        cv2.waitKey(1)

    def detect_blue_ball(self, results, frame):
        """
        Process YOLO results and use color filtering to detect blue balls.
        """
        for result in results:
            # Extract bounding box and class information
            for box in result.boxes:
                # YOLO box contains (x1, y1, x2, y2) coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Crop the detected region
                detected_region = frame[y1:y2, x1:x2]

                # Convert the detected region to HSV color space
                hsv_region = cv2.cvtColor(detected_region, cv2.COLOR_BGR2HSV)

                # Create a mask for blue color within the bounding box
                mask = cv2.inRange(hsv_region, self.lower_blue, self.upper_blue)

                # Check if a sufficient number of pixels in the mask are blue
                if cv2.countNonZero(mask) > 100:  # Adjust the threshold based on ball size
                    # Draw a rectangle around the detected blue ball
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    return True  # Blue ball detected

        return False  # No blue ball detected

if __name__ == '__main__':
    try:
        # Initialize the detector node
        detector = BlueBallDetector()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    finally:
        cv2.destroyAllWindows()
