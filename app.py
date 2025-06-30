import streamlit as st
from gtts import gTTS
from PIL import Image
import os

# ------------------- Streamlit Config -------------------
st.set_page_config(page_title="Text to Speech", page_icon="🗣️", layout="centered")

# ------------------- Custom CSS -------------------
st.markdown("""
    <style>
    .main-title {
        color: #ffffff;
        background-color: #2e8b57;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 35px;
        margin-bottom: 25px;
    }
    .stButton > button {
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------- Sidebar -------------------
with st.sidebar:
    st.title("🗣️ Text to Speech")
    image = Image.open('text_to_speech-removebg-preview.png')
    st.image(image, width=250)
    st.markdown("**👨‍💻 Made by:** Masood Khan")
    st.markdown("📧 [Contact me](mailto:masoodkhanse884@gmail.com)")
    st.markdown("💻 [GitHub Profile](https://github.com/Masoodkhan884)")

# ------------------- Main Interface -------------------
st.markdown('<div class="main-title">🎙️ Text to Speech Converter</div>', unsafe_allow_html=True)

text = st.text_area("📝 Enter text to convert to speech:", height=150, placeholder="Type your message here...")

voices = ["Alloy", "Echo", "Fable", "Onyx", "Nova", "Shimmer"]
selected_voice = st.selectbox("🎧 Select a voice style (for UI only):", voices)

# ------------------- Convert Button -------------------
if st.button("🔊 Convert to Speech"):
    if not text.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            tts = gTTS(text=text, lang='en', tld='com')
            output_path = "output.mp3"
            tts.save(output_path)
            if os.path.exists(output_path):
                st.success("✅ Speech generated successfully!")
                st.markdown("### ▶️ Listen to the audio:")
                st.audio(output_path, format="audio/mp3")
            else:
                st.error("❌ Audio file could not be found after saving.")
        except Exception as e:
            st.error(f"❌ Failed to convert text to speech.\n**Reason:** {e}")

# ------------------- Footer -------------------
st.markdown("---")
st.markdown("© 2025 Masood Khan | Powered by [gTTS](https://pypi.org/project/gTTS/) & [Streamlit](https://streamlit.io/)")
