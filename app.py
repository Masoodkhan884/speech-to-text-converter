import streamlit as st
import speech_recognition as sr
from PIL import Image
import os

# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="Voice to Text App", page_icon="🎤", layout="centered")

# ------------------- STYLING -------------------
st.markdown("""
    <style>
    .title-box {
        background-color: #1f7a8c;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stButton>button {
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 10px;
        background-color: #198754;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------- SIDEBAR -------------------
with st.sidebar:
    image = Image.open('voice_to_text-removebg-preview.png')
    st.image(image, width=280)
    st.markdown("## 👨‍💻 Made by: Masood Khan")
    st.markdown("📧 [Email Me](mailto:masoodkhanse884@gmail.com)")
    st.markdown("💻 [Visit GitHub](https://github.com/Masoodkhan884)")

# ------------------- FUNCTION: Voice to Text -------------------
def voice_to_text(source):
    r = sr.Recognizer()
    st.info("🎤 Listening... Please speak clearly")
    audio = r.listen(source, phrase_time_limit=5)
    try:
        text = r.recognize_google(audio)
        return text, False
    except sr.UnknownValueError:
        return "❌ Could not understand the audio.", False
    except sr.RequestError as e:
        return f"❌ API Error: {e}", False

# ------------------- FUNCTION: Save and Display Output -------------------
def display_voice_to_text_output(text):
    st.success("✅ Transcription complete!")
    st.markdown("### 📝 Transcribed Text:")
    st.code(text)
    with open("voice_to_text_output.txt", "w") as f:
        f.write(text)

# ------------------- MAIN FUNCTION -------------------
def main_app():
    st.markdown('<div class="title-box">🎤 Voice to Text Converter</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    recording_stopped = False

    try:
        microphone = sr.Microphone()
    except Exception as e:
        st.error(f"⚠️ Could not access your microphone.\n**Reason:** {e}")
        return

    with col1:
        if st.button("🎙️ Start Recording"):
            with microphone as source:
                text, recording_stopped = voice_to_text(source)
            st.session_state.text = text
            recording_stopped = False

    with col2:
        if st.button("🛑 Stop Recording"):
            recording_stopped = True
            st.info("⏹️ Recording stopped.")

    with col3:
        if st.button("💬 Convert to Text"):
            if 'text' in st.session_state:
                display_voice_to_text_output(st.session_state.text)
            else:
                st.warning("⚠️ Please record your voice first.")

    with col4:
        if st.button("📂 View Saved Output"):
            try:
                with open("voice_to_text_output.txt", "r") as f:
                    st.markdown("### 📄 Output File Content:")
                    st.code(f.read())
            except FileNotFoundError:
                st.error("❌ No output file found yet.")

    st.markdown("---")
    st.markdown("© 2025 Masood Khan | Powered by Streamlit & Google Speech Recognition")

if __name__ == "__main__":
    main_app()
