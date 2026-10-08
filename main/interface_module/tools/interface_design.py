import tkinter as tk

def create_design():
    window = tk.Tk()
    window.title("Video Upload Screen")
    window.geometry("500x250")

    instruction_label = tk.Label(window, text="Please select the video to be processed", font = ("Arial", 12))
    instruction_label.pack(pady = 40)

    upload_button = tk.Button(window, text="📁 Upload video", font = ("Arial", 14))
    upload_button.pack()

    return window, instruction_label, upload_button