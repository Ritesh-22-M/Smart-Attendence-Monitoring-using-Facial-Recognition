import cv2

# Initialize the camera
cam_port = 0  # Use 0 for the default camera, or change it to the appropriate port number
cam = cv2.VideoCapture(cam_port)

# Reading the input person's name
inp = input('Enter person name: ')

# Loop to continuously capture images
while True:
    # Capture frame-by-frame
    ret, frame = cam.read()
    
    # Display the captured frame
    cv2.imshow('Captured Frame', frame)
    
    # Wait for the user to press a key
    key = cv2.waitKey(1) & 0xFF
    
    # If the 's' key is pressed, save the image
    if key == ord('s'):
        cv2.imwrite(inp + ".png", frame)
        print("Image saved as", inp + ".png")
    
    # If the 'q' key is pressed, quit the loop
    elif key == ord('q'):
        break

# Release the camera and close OpenCV windows
cam.release()
cv2.destroyAllWindows()
