import cv2
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
# Load the video capture object
cap = cv2.VideoCapture(0)
 
# Set the camera resolution
cap.set(3, 640) # Width
cap.set(4, 480) # Height
 
# Create a CLAHE object with default parameters
clahe = cv2.createCLAHE()
 
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
 
#using the 17th GPIO pin the pi to activate the relay
RELAY_GPIO = 17
GPIO.setup(RELAY_GPIO, GPIO.OUT) # GPIO Assign mode
 
# Set up a loop to process each frame of the video stream
while True:
    GPIO.output(RELAY_GPIO, GPIO.HIGH) # on
         	# Capture a frame from the video stream 
ret, frame = cap.read()
          
 
# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
# Apply CLAHE to the grayscale image
gray_clahe = clahe.apply(gray)
# Write the CLAHE-enhanced frame to the output video
out.write(cv2.cvtColor(gray_clahe, cv2.COLOR_GRAY2BGR))
 
# Display the original and CLAHE-enhanced frames side-by-side
cv2.imshow('CLAHE', gray_clahe)
 
# Check for key presses and exit if 'q' is pressed
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
 
# Clean up resources
cap.release()
out.release()
GPIO.output(RELAY_GPIO, GPIO.LOW) # out
cv2.destroyAllWindows()
