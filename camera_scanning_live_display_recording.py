#--------------------------------------------Document---------------------------------------------------------|

# Functionality of this program: The program detects the camera connected to the system.                      
# Once the user selects the detected camera, it will display the live feed and simultaneously start recording.
# The output will be saved as output.mp4 after the process completes.                                         
#--------------------------------------------------------------------------------------------------------------
# Additionally, to close the live window, please use the "q" key.                                             
#--------------------------------------------------------------------------------------------------------------


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
    """This function plays the selected camera stream and records it."""
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
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))  # Output file

    print("Showing video and recording... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to retrieve frame from camera.")
            break
        
        cv2.imshow(f"Camera {available_cameras[choice]}", frame)

        out.write(frame)
        
        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    out.release()  
    cv2.destroyAllWindows()

if __name__ == "__main__":
    available_cameras = list_cameras()
    
    if available_cameras:
        select_camera_and_show(available_cameras)
