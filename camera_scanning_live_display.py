#--------------------------------------------Document---------------------------------------------------------|

# Functionality of this program: The program detects the camera connected to the system. 
# After the user selects the detected camera, the live feed is displayed only without recording.
#-------------------------------------------------------------------------------------------------------------
# Additionally, to close the live window, please use the "q" key.
#-------------------------------------------------------------------------------------------------------------


import cv2

def list_cameras():
    """This function lists the connected cameras (including internal and external)."""
    available_cameras = []
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            available_cameras.append(index)
        cap.release()
        index += 1
    
    if not available_cameras:
        print("No cameras found.")
        return []
    
    return available_cameras

def select_camera_and_show(available_cameras):
    """This function plays the selected camera stream."""
    print("Available cameras:")
    for i, cam in enumerate(available_cameras):
        print(f"{i}: Camera {cam}")
    
    choice = int(input("Enter the camera number: "))
    
    if choice < 0 or choice >= len(available_cameras):
        print("Invalid choice.")
        return
    
    cap = cv2.VideoCapture(available_cameras[choice])  
    
    if not cap.isOpened():
        print("Unable to open the camera.")
        return
    
    print("Showing video... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to retrieve frame from camera.")
            break
        
        cv2.imshow(f"Camera {available_cameras[choice]}", frame)
        
        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    available_cameras = list_cameras()
    
    if available_cameras:
        select_camera_and_show(available_cameras)



