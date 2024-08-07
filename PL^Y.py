import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
import os

def convert_video_to_gif(video_path, output_path):
    try:
        clip = VideoFileClip(video_path)
        clip = clip.subclip(0, min(clip.duration, 10))  
        clip.write_gif(output_path)
    except Exception as e:
        print(f"Error during conversion: {e}")
        messagebox.showerror("Error", f"Failed to convert video to GIF: {e}")

def select_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
    if file_path:
        entry_video_path.delete(0, tk.END)
        entry_video_path.insert(0, file_path)

def convert():
    video_path = entry_video_path.get()
    if not video_path:
        messagebox.showwarning("Warning", "Please select a video file.")
        return
    
    output_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")])
    if output_path:
        convert_video_to_gif(video_path, output_path)
        messagebox.showinfo("Success", "Video converted to GIF successfully!")

# Ccreate the main window
root = tk.Tk()
root.title("Video to GIF Converter") # Joana :)

# Create and place widgets
tk.Label(root, text="Select Video:").pack(pady=5)

entry_video_path = tk.Entry(root, width=50)
entry_video_path.pack(pady=5)

tk.Button(root, text="Browse", command=select_video).pack(pady=5)
tk.Button(root, text="Convert to GIF", command=convert).pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
