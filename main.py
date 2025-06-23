import tkinter as tk
from tkinter import scrolledtext, messagebox
import sounddevice as sd
import scipy.io.wavfile as wav
import openai
import os
from dotenv import load_dotenv
import threading
import numpy as np

# Load .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# Globals
recording_data = []
is_recording = False

def start_recording():
    global is_recording, recording_data
    is_recording = True
    recording_data = []
    status_label.config(text="Recording... Click 'Stop Recording' to finish.")
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    threading.Thread(target=record_audio).start()

def record_audio():
    global recording_data, is_recording
    with sd.InputStream(samplerate=44100, channels=1, callback=callback):
        while is_recording:
            sd.sleep(100)

def callback(indata, frames, time, status):
    if is_recording:
        recording_data.append(indata.copy())

def stop_recording():
    global is_recording, recording_data
    is_recording = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    status_label.config(text="Saving recording...")
    audio = np.concatenate(recording_data, axis=0)
    wav.write("recorded.wav", 44100, audio)
    status_label.config(text="Recording saved as recorded.wav")

def transcribe_and_format():
    try:
        filename = "recorded.wav"
        with open(filename, "rb") as audio_file:
            whisper_response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        raw_text = whisper_response.text
        print("RAW TRANSCRIPTION:")
        print(raw_text)

        prompt = f"""
Extract and fill the following dental fields from the text below.
If any fields are missing, leave them blank.

Fields:
- Patient Number
- Chief Complaint
- Tooth Surface
- Diagnosis
- X-ray
- Treatment Plan
- Procedure
- Post-Op

Text:
\"\"\"
{raw_text}
\"\"\"

Format your response like:
Patient Number: ...
Chief Complaint: ...
Tooth Surface: ...
Diagnosis: ...
X-ray: ...
Treatment Plan: ...
Procedure: ...
Post-Op: ...
"""

        chat_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a dental assistant helping to structure notes."},
                {"role": "user", "content": prompt}
            ]
        )

        structured_output = chat_response.choices[0].message.content
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, structured_output)
        status_label.config(text="Transcription + GPT formatting complete")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

def copy_to_clipboard():
    try:
        text = output_text.get(1.0, tk.END)
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Structured notes copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy: {e}")

# Tkinter setup
root = tk.Tk()
root.title("Dentrix Transcriber - Whisper + GPT")

# Start Recording button
start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(pady=5)

# Stop Recording button (disabled initially)
stop_button = tk.Button(root, text="Stop Recording", command=stop_recording, state=tk.DISABLED)
stop_button.pack(pady=5)

# Transcribe + GPT button
process_button = tk.Button(root, text="Transcribe + Format with GPT", command=transcribe_and_format)
process_button.pack(pady=5)

# Copy to Clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

# Output window
output_text = scrolledtext.ScrolledText(root, height=15, width=60)
output_text.pack(pady=10)

root.mainloop()
