import cv2
import numpy as np

def identify_blue_balls(frame):
    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color range for detecting blue (you might need to adjust this based on lighting)
    lower_blue = np.array([100, 150, 0])  # HSV lower bound for blue
    upper_blue = np.array([140, 255, 255])  # HSV upper bound for blue

    # Threshold the image to get only blue regions
    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    # Find contours of the detected blue areas
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    ball_positions = []  # List to store the positions of the detected balls

    for contour in contours:
        # Get the bounding box around the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Set a minimum size threshold to filter out noise or small objects
        if w * h > 100:  # You may need to adjust this threshold based on ball size in the frame
            # Find the center of the blue ball
            center_x = x + w // 2
            center_y = y + h // 2
            ball_positions.append((center_x, center_y))

            # Draw a rectangle around the detected blue ball (for visualization)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return ball_positions  # Return a list of ball positions (center_x, center_y)

# Capture video stream from the robot's camera
cap = cv2.VideoCapture(0)  # Replace with the correct camera source

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect the blue balls
    ball_positions = identify_blue_balls(frame)

    # Print the positions of the detected balls (for testing)
    for i, (cx, cy) in enumerate(ball_positions):
        print(f"Ball {i+1}: Position ({cx}, {cy})")

    # Show the video frame with the detection (for visualization)
    cv2.imshow('Frame', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
