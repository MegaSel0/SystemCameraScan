#--------------------------------------------Document---------------------------------------------------------|

# Functionality of this program: After running the program, it starts recording from the connected camera.
#  When you close the program, the recorded file is saved as output.mp4.
#-------------------------------------------------------------------------------------------------------------


import cv2

def find_first_camera():
    """This function returns the first available camera."""
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            cap.release()
            return index
        cap.release()
        index += 1
    return None

def record_camera():
    """This function records video from the first available camera without displaying it."""
    camera_index = find_first_camera()
    
    if camera_index is None:
        print("No cameras found.")
        return

    cap = cv2.VideoCapture(camera_index)
    
    if not cap.isOpened():
        print("Unable to open the camera.")
        return
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))  

    print("Recording started... Press 'Ctrl + C' to stop.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to retrieve frame from camera.")
                break

            out.write(frame)

    except KeyboardInterrupt:
        # Handle Ctrl+C to stop recording
        print("\nRecording stopped.")

    cap.release()
    out.release()
    print("Video saved as 'output.avi'.")

if __name__ == "__main__":
    record_camera()

