import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
from PIL import ImageTk, Image, ImageDraw
import math
import os

def generate_image():
    # Create a new image with a white background
    image = Image.new("RGB", (300, 200), "white")
    draw = ImageDraw.Draw(image)

    # Draw a curve pattern
    for x in range(300):
        y = int(50 * math.sin(x / 30) + 100)
        draw.point((x, y), fill="black")

    return image

def extract_audio():
    input_file = filedialog.askopenfilename(title="Select Video File")
    if input_file:
        input_filename = os.path.basename(input_file)
        output_file = filedialog.asksaveasfilename(title="Save Audio File", initialfile=input_filename +'audio', defaultextension=".mp3", filetypes=[("Audio Files", "*.mp3")])
        if output_file:
            try:
                video_clip = VideoFileClip(input_file)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(output_file)
                audio_clip.close()
                video_clip.close()
                print("Audio extracted successfully!")
            except Exception as e:
                print(f"Error extracting audio: {e}")

window = tk.Tk()
window.title("Audio Extractor")
window.geometry("400x400")  # Set the window size to 400x400 pixels

# Generate and display the image
image = generate_image()
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(window, image=photo)
label_image.pack()

button_extract = tk.Button(window, text="Extract Audio", command=extract_audio)
button_extract.pack()

window.mainloop()
