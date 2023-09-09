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

def convert_webm_to_gif(webm_input, folder, output_folder=""):
    webm_file = folder + webm_input + ".webm"
    gif_file = output_folder + webm_input + ".gif"
    ff = ffmpy.FFmpeg(
        inputs = {webm_file: None},
        outputs = {gif_file: ["-vf", "fps=10,scale=350:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse"]}
    )
    ff.run()
    return

for webm in os.listdir(input_folder):
    if webm.endswith(".webm"):
        print(webm)
        convert_webm_to_gif(os.path.splitext(webm)[0], input_folder, output_folder)