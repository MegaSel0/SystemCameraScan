#--------------------------------------------Document---------------------------------------------------------|

# All the code sections for camera scanning, live camera recording, 
# and live camera display are provided in this file as separate parts. You can use any of them as you wish.
#--------------------------------------------------------------------------------------------------------------

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
    # Finding the first camera
    camera_index = find_first_camera()
    
    if camera_index is None:
        print("No cameras found.")
        return

    # Opening the first camera
    cap = cv2.VideoCapture(camera_index)
    
    if not cap.isOpened():
        print("Unable to open the camera.")
        return
    
    # Defining the codec and creating a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for .avi files
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))  # Output file

    print("Recording started... Press 'Ctrl + C' to stop.")

    try:
        # Loop to record the video stream
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to retrieve frame from camera.")
                break

            # Write the frame to the output file
            out.write(frame)

    except KeyboardInterrupt:
        # Handle Ctrl+C to stop recording
        print("\nRecording stopped.")

    # Releasing resources
    cap.release()
    out.release()
    print("Video saved as 'output.avi'.")

if __name__ == "__main__":
    record_camera()






#----------------------------------------------------------------------------------------------------------






#----------Once the user selects the detected camera, it will display the live feed and simultaneously start recording.----------
# import cv2

# def list_cameras():
#     """This function lists the connected cameras (including internal and external)."""
#     available_cameras = []
#     index = 0
#     while True:
#         cap = cv2.VideoCapture(index)
#         if not cap.read()[0]:
#             break
#         else:
#             available_cameras.append(index)
#         cap.release()
#         index += 1
    
#     if not available_cameras:
#         print("No cameras found.")
#         return []
    
#     return available_cameras

# def select_camera_and_show(available_cameras):
#     """This function plays the selected camera stream and records it."""
#     # Displaying the list of available cameras
#     print("Available cameras:")
#     for i, cam in enumerate(available_cameras):
#         print(f"{i}: Camera {cam}")
    
#     # Selecting a camera
#     choice = int(input("Enter the camera number: "))
    
#     if choice < 0 or choice >= len(available_cameras):
#         print("Invalid choice.")
#         return
    
#     # Opening the selected camera with OpenCV
#     cap = cv2.VideoCapture(available_cameras[choice])  # Using the camera index
    
#     if not cap.isOpened():
#         print("Unable to open the camera.")
#         return
    
#     # Defining the codec and creating a VideoWriter object
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for .avi files
#     out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))  # Output file

#     print("Showing video and recording... Press 'q' to quit.")

#     # Loop to display the video stream and record
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to retrieve frame from camera.")
#             break
        
#         # Display the video stream
#         cv2.imshow(f"Camera {available_cameras[choice]}", frame)

#         # Write the frame to the output file
#         out.write(frame)
        
#         # Exit when 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     # Releasing resources
#     cap.release()
#     out.release()  # Stop recording
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     available_cameras = list_cameras()
    
#     if available_cameras:
#         select_camera_and_show(available_cameras)



#----------------------------------------------------------------------------------------------------------------



#----------After the user selects the detected camera, the live feed is displayed only without recording.-----------
# import cv2

# def list_cameras():
#     """This function lists the connected cameras (including internal and external)."""
#     available_cameras = []
#     index = 0
#     while True:
#         cap = cv2.VideoCapture(index)
#         if not cap.read()[0]:
#             break
#         else:
#             available_cameras.append(index)
#         cap.release()
#         index += 1
    
#     if not available_cameras:
#         print("No cameras found.")
#         return []
    
#     return available_cameras

# def select_camera_and_show(available_cameras):
#     """This function plays the selected camera stream."""
#     # Displaying the list of available cameras
#     print("Available cameras:")
#     for i, cam in enumerate(available_cameras):
#         print(f"{i}: Camera {cam}")
    
#     # Selecting a camera
#     choice = int(input("Enter the camera number: "))
    
#     if choice < 0 or choice >= len(available_cameras):
#         print("Invalid choice.")
#         return
    
#     # Opening the selected camera with OpenCV
#     cap = cv2.VideoCapture(available_cameras[choice])  # Using the camera index
    
#     if not cap.isOpened():
#         print("Unable to open the camera.")
#         return
    
#     print("Showing video... Press 'q' to quit.")

#     # Loop to display the video stream
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to retrieve frame from camera.")
#             break
        
#         cv2.imshow(f"Camera {available_cameras[choice]}", frame)
        
#         # Exit when 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     # Releasing resources
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     available_cameras = list_cameras()
    
#     if available_cameras:
#         select_camera_and_show(available_cameras)








