from moviepy.editor import VideoFileClip
import os
def remove_audio(video_path, output_path):
    video = VideoFileClip(video_path)
    video_without_audio = video.without_audio()
    video_without_audio.write_videofile(output_path)

# Example usage
video_folder="cuisine"
out_folder="res"
for root,dir,file  in os.walk(video_folder):
    for f in file:
        res_name=os.path.join(out_folder,f)
        remove_audio(os.path.join(video_folder,f), res_name)
        
    
# video_path = "input_video.mp4"
# output_path = "output_video.mp4"

# remove_audio(video_path, output_path)
