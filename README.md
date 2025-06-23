# 🦷 NoteBuddy — Voice-to-Note Dental Assistant

**NoteBuddy is a voice-activated desktop assistant built with Whisper and GPT to streamline dental note-taking.**  
Record patient visits, and the app automatically transcribes the audio and formats it into structured dental notes — all in one click.

---

## 📺 Demo

🎥 Demo coming soon *(or link here if you have one)*

---

## 🧠 Why I Built This

Writing dental notes manually is repetitive and time-consuming. NoteBuddy solves this by:
- Recording real-time audio during consultations
- Transcribing speech with OpenAI Whisper
- Structuring notes into dental fields using GPT

> Built as a standalone desktop app with a simple interface — no browser, no hassle.

---

## ✨ Key Features

✅ Voice recording from within the app  
✅ Automatic transcription using Whisper  
✅ GPT-3.5 formats transcription into dental note fields  
✅ Copy formatted notes to clipboard instantly  
✅ Lightweight desktop GUI using Tkinter  

---

## 🧰 Tech Stack

| Component           | Tool / Library                  |
|--------------------|---------------------------------|
| Voice Recording     | `sounddevice`, `scipy`          |
| Speech-to-Text      | OpenAI `Whisper`                |
| AI Formatting       | OpenAI `GPT-3.5 Turbo`          |
| UI                  | `tkinter` + `scrolledtext`      |
| Environment Vars    | `python-dotenv`                 |
| Audio Format        | `.wav` using `scipy.io.wavfile` |

---

## ⚙️ How It Works

1. **Click “Start Recording”** to begin capturing audio  
2. **Click “Stop Recording”** to save the recording as `recorded.wav`  
3. **Click “Transcribe + Format with GPT”** to get dental notes structured into fields:
   - Patient Number
   - Chief Complaint
   - Tooth Surface
   - Diagnosis
   - X-ray
   - Treatment Plan
   - Procedure
   - Post-Op  
4. **Click “Copy to Clipboard”** to paste notes into Dentrix or any system

---

## 📁 Project Structure

\`\`\`
notebuddy/
├── main.py            # Main app with UI, recording, transcription, and GPT formatting
├── .env.example       # Sample env file for OpenAI key
├── requirements.txt   # Python dependencies
└── README.md
\`\`\`

---

## 🚀 Getting Started

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/yourusername/notebuddy.git
cd notebuddy
\`\`\`

### 2. Create a Virtual Environment (optional but recommended)

\`\`\`bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
\`\`\`

### 3. Install Requirements

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Set Up Environment Variables

Create a \`.env\` file in the root directory:

\`\`\`
OPENAI_API_KEY=your-openai-key-here
\`\`\`

### 5. Run the App

\`\`\`bash
python main.py
\`\`\`

---

## 📫 Contact

Built with ❤️ by [Mousa Pirzada](https://www.linkedin.com/in/mousa-pirzada/)  
Open to feedback, collaboration, and improvements.
