import streamlit as st
from gtts import gTTS
from PIL import Image
import os

# ---------------------------- PAGE CONFIG ----------------------------
st.set_page_config(page_title="Text to Speech App", page_icon="🗣️", layout="centered")

# ---------------------------- STYLES ----------------------------
st.markdown("""
    <style>
    .main-title {
        color: #ffffff;
        background-color: #2e8b57;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 35px;
    }
    .stTextInput > div > div > input {
        font-size: 18px;
    }
    .stTextArea textarea {
        font-size: 18px;
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

# ---------------------------- SIDEBAR ----------------------------
with st.sidebar:
    st.title("🗣️ Text to Speech")
    
    image = Image.open('text_to_speech-removebg-preview.png')
    st.image(image, width=250)
    
    st.markdown("**👨‍💻 Made by:** Masood Khan")
    st.markdown("📧 [Contact me](mailto:masoodkhanse884@gmail.com)")
    st.markdown("💻 [Visit My GitHub](https://github.com/Masoodkhan884)")

# ---------------------------- MAIN APP ----------------------------
st.markdown('<div class="main-title">🎙️ Text to Speech Converter</div>', unsafe_allow_html=True)
st.markdown("### 📝 Enter your text below:")

text = st.text_area("Type something you want to hear", height=150, placeholder="E.g., Hello, welcome to my Streamlit app!")

st.markdown("### 🎧 Choose a voice style (for UI only):")
voices = ["Alloy", "Echo", "Fable", "Onyx", "Nova", "Shimmer"]
selected_voice = st.selectbox("Select a voice", voices)

# Convert Button
if st.button("🔊 Convert to Speech"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text to convert.")
    else:
        with st.spinner("Generating speech..."):
            tts = gTTS(text=text, lang='en', tld='com')
            tts.save("output.mp3")
            st.success("✅ Speech generated successfully!")
            st.markdown("### ▶️ Play the audio below:")
            st.audio("output.mp3", format="audio/mp3")

# Footer
st.markdown("---")
st.markdown("© 2025 Masood Khan | Powered by [gTTS](https://pypi.org/project/gTTS/) & [Streamlit](https://streamlit.io/)")

