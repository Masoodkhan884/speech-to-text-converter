import streamlit as st
from gtts import gTTS
import os
from PIL import Image


st.markdown(
    """
    <style>
    h1 {
        font-family: 'Source Sans Pro', sans-serif;
        font-weight: 700;
        color: rgb(250, 250, 250);
        padding: 1.25rem 0px 1rem;
        margin: 0px;
        line-height: 1.2;
        background:#708090;
    }
    .st-emotion-cache-h4xjwg {
    position: fixed;
    top: 0px;
    left: 0px;
    right: 0px;
    height: 3.75rem;
    background: rgb(14, 17, 23);
    outline: none;
    z-index: 999990;
    display: none;
}
.st-emotion-cache-15hul6a {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color: rgb(32 190 14);
    border: 1px solid rgba(250, 250, 250, 0.2);
} 
.st-emotion-cache-qgowjl p {
    word-break: break-word;
    margin-bottom: 0px;
    font-size: 25px;
}
.st-emotion-cache-1mi2ry5 {
    display: flex;
    -webkit-box-pack: justify;
    justify-content: space-between;
    -webkit-box-align: start;
    align-items: start;
    padding: 0.25rem 1.5rem 1.5rem;
}

    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.title("Text to Speech")
    # Logo insertion
    image =Image.open('text_to_speech-removebg-preview.png')
    st.image(image, width=275, caption=None)
    st.title("Made By: \n MASOOD KHAN")
    st.title("Contact me at \n masoodkhanse884@gmail.com")
    # Title of the app
    st.title("Go To my GitHub")
    # Create a button and check if it is clicked
    st.markdown('[Click here to visit my GitHub](https://github.com/Masoodkhan884)')


# create a function to convert text to speech
def text_to_speech(text, voice):
    tts = gTTS(text=text, lang='en', tld='com')
    tts.save("output.mp3")
    return "output.mp3"

# create a function to display audio
def display_audio(file):
    audio_file = open(file, 'rb')
    st.audio(audio_file, format='audio/mp3')


    # create a function to display the text input
def display_text_input():
    text = st.text_area("Enter text to convert to speech")
    return text


# create a function to display the voice option
def display_voice_option():
    voices = ["alloy", "echo", "fable", "onyx", "nova","shimmer"]
    select = st.selectbox("Select Voice", voices)
    return select

# create a function to display the convert button
def display_convert_button():
    if st.button("Convert to Speech"):
        return True
    return False

# create a function to display the main app
def main_app():
    st.title("Text to Speech App")
    text = display_text_input()
    select_voice = display_voice_option()
    convert = display_convert_button()
    if convert:
        file = text_to_speech(text, select_voice)
        display_audio(file)

if __name__ == "__main__":
    main_app()

    