from moviepy.editor import VideoFileClip
import os
# Specify the input and output video file paths
input_folder = "res"
output_folder = "final"
count=960
left_crop = count

# Load the video clip
for root, dic, file in os.walk(input_folder):
    for f in file:
        name=os.path.join(input_folder,f)
        video = VideoFileClip(name)
        right_crop = video.w - count
        cropped_video = video.crop(x1=left_crop, x2=right_crop)
        cropped_video.write_videofile(os.path.join(output_folder,f), codec="libx264", audio_codec="aac")
