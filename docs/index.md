# 🦷 NoteBuddy – AI-Powered Voice-to-Note Dental Assistant

**NoteBuddy is a voice-activated desktop app that transcribes dental consultations and formats them into structured clinical notes — using OpenAI’s Whisper and GPT-3.5.**

Built to reduce repetitive dental documentation and streamline the note-taking process, NoteBuddy helps dentists focus on patients, not paperwork.

---

## 📌 Objective

Dentists often spend a significant portion of their day writing or dictating notes — a time-consuming and repetitive task.

NoteBuddy was designed to:
- **Record consultations in real-time**
- **Transcribe voice to text** using Whisper
- **Format the text** into structured dental notes using GPT-3.5
- **Provide a simple desktop interface** with no browser required

---

## 💡 How It Works

1. **Recording Audio**  
   - Click “Start Recording” to capture patient visit audio via the mic.  
   - Audio is saved as a `.wav` file using `sounddevice` and `scipy`.

2. **Transcription with Whisper**  
   - The `.wav` file is passed to OpenAI Whisper for fast, accurate speech-to-text conversion.

3. **Formatting with GPT**  
   - The raw transcript is structured into dental note fields by GPT-3.5 using prompt templates.
   - Example fields:
     - Patient Number
     - Chief Complaint
     - Tooth Surface
     - Diagnosis
     - X-ray
     - Treatment Plan
     - Procedure
     - Post-Op Instructions

4. **Output + Clipboard Copy**  
   - The generated note is shown in a scrolled text box.
   - One-click “Copy to Clipboard” support for pasting into dental software (e.g. Dentrix).

---

## 🧰 Technologies Used

| Function             | Tools & Libraries           |
|----------------------|-----------------------------|
| Audio Recording      | `sounddevice`, `scipy`      |
| Transcription        | `Whisper` (OpenAI)          |
| AI Formatting        | `GPT-3.5 Turbo` via OpenAI  |
| GUI                  | `tkinter`, `scrolledtext`   |
| Environment Handling | `python-dotenv`             |

---

## 🎯 Key Features

- 💬 **Voice-to-text transcription** in real-time  
- 📋 **Structured GPT output** for common dental note sections  
- 🖥️ **Lightweight desktop UI** with no external dependencies  
- 🔐 **.env support** for API key management  
- ⚡ **Instant clipboard copy** for notes

---

## 🧠 Challenges & Solutions

| Challenge | Solution |
|----------|----------|
| Background noise in audio | Applied aggressive noise suppression and used short recording bursts |
| Variable structure in spoken notes | Prompted GPT with consistent field-based templates |
| Environment variable errors | Provided a `.env.example` and integrated error messaging for missing keys |
| GUI responsiveness | Used `tkinter`’s `after()` loop for smoother updates |

---

## 🧠 Lessons Learned

- Whisper is highly effective for domain-specific vocabulary like dentistry, but **prompt engineering is key** for good GPT formatting.
- A simple GUI can still feel premium with smart UX choices like text wrapping, status indicators, and field-based outputs.
- Dentists want **speed and reliability** — one click, one result, no fluff.

---

## 📽️ Demo

🎥 Demo video coming soon *(will be linked here when ready)*

---

## 📂 GitHub + Assets

- [🔗 GitHub Repository](https://github.com/20mup/NoteBuddy)
- [📸 Interface Preview](../assets/images/notebuddy/interface.png)
- [📄 Engineering Case Study](../docs/notebuddy-case-study.md)

---

> _“NoteBuddy was born from a simple idea: eliminate repetitive note-taking and give dentists their time back.”_
