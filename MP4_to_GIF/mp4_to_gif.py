"""
Excpects a full path to the folder where the mp4 are located.
If no output path is given, it will push the gifs to the folder given
"""

import ffmpy
import sys
import os

input_folder = sys.argv[1]

try:
    output_folder = sys.argv[2]
except: 
    output_folder = input_folder

def convert_mp4_to_gif(input_file, folder, output_folder):
    video_file = folder + input_file + ".mp4"
    gif_file = output_folder + input_file + ".gif"
    print("converting to ", video_file, "to", gif_file)
    ff = ffmpy.FFmpeg(
        inputs = {video_file : None},
        outputs = {gif_file : ["-vf", "fps=10,scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse"]})
    ff.run()
    return

for video in os.listdir(input_folder):
    if video.endswith(".mp4"):
        print(video)
        convert_mp4_to_gif(os.path.splitext(video)[0], input_folder, output_folder)
