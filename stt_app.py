import streamlit as st
import speech_recognition as sr
from PIL import Image
from pydub import AudioSegment
import os
import tempfile

# -------------- Page Configuration --------------
st.set_page_config(page_title="Voice to Text App", page_icon="🎤", layout="centered")

# -------------- Styling --------------
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

# -------------- Sidebar Info --------------
with st.sidebar:
    image = Image.open('voice_to_text-removebg-preview.png')
    st.image(image, width=280)
    st.markdown("## 👨‍💻 Made by: Masood Khan")
    st.markdown("📧 [Email Me](mailto:masoodkhanse884@gmail.com)")
    st.markdown("💻 [GitHub](https://github.com/Masoodkhan884)")

# -------------- Audio Processing Logic --------------
def convert_to_wav(uploaded_file):
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio = AudioSegment.from_file(uploaded_file)
    audio.export(temp.name, format="wav")
    return temp.name

def recognize_uploaded_audio(uploaded_file):
    recognizer = sr.Recognizer()
    wav_path = convert_to_wav(uploaded_file)
    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)
        st.info("🔄 Transcribing...")
        text = recognizer.recognize_google(audio)
        return text

# -------------- Main App --------------
def main_app():
    st.markdown('<div class="title-box">🎤 Voice to Text Converter</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("📂 Upload an audio file (WAV, MP3, FLAC, AIFF)", type=["wav", "mp3", "flac", "aiff"])

    if uploaded_file is not None:
        st.audio(uploaded_file)
        if st.button("📝 Convert to Text"):
            try:
                result_text = recognize_uploaded_audio(uploaded_file)
                st.success("✅ Transcription Complete!")
                st.code(result_text)
                with open("voice_to_text_output.txt", "w", encoding="utf-8") as f:
                    f.write(result_text)
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please upload an audio file to begin.")

    # View saved output
    if st.button("📄 View Saved Output"):
        if os.path.exists("voice_to_text_output.txt"):
            with open("voice_to_text_output.txt", "r", encoding="utf-8") as f:
                st.markdown("### 📄 Output File Content:")
                st.code(f.read())
        else:
            st.error("❌ No saved output found.")

    st.markdown("---")
    st.markdown("© 2025 Masood Khan | Powered by Streamlit & Google Speech Recognition")

if __name__ == "__main__":
    main_app()
