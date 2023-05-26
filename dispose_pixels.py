import cv2
import os
input_folder = "hhh"
output_folder = input_folder+"_final"

os.mkdir(output_folder)
for root, dic, file in os.walk(input_folder):
     for f in file:
        name=os.path.join(input_folder,f)
        output_file=os.path.join(output_folder,f)
        video = cv2.VideoCapture(name)

        # Get the video's properties
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video.get(cv2.CAP_PROP_FPS)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, fps, (width-960*2, height))

        # Read and write each frame of the video
        while True:
            ret, frame = video.read()

            if not ret:
                break

            # Process the frame if needed

            # For example, you can perform some operations on the frame using PyTorch
            frame = frame[:, 960:(width - 960), :]

            # Write the processed frame to the output video file
            out.write(frame)

        
            # Exit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video capture and writer objects
        video.release()
        out.release()


