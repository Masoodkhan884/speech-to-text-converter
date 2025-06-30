import streamlit as st
import speech_recognition as sr
from PIL import Image

st.markdown(
    """
    <style>
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
    background-color: rgb(9, 171, 59);
    border: 1px solid rgba(250, 250, 250, 0.2);
}

  
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar content
with st.sidebar:
    # Logo insertion
    image = Image.open('voice_to_text-removebg-preview.png')
    st.image(image, width=300, caption=None)

    # Personal information
    st.title("Made By: \n MASOOD KHAN")

    # Contact Us button (for email)
    st.markdown(
        '<a href="mailto:masoodkhanse884@gmail.com" style="text-decoration:none;"><button style="background-color:#4CAF50; color:white; padding:10px 20px; border:none; border-radius:5px;">Contact Us</button></a>',
        unsafe_allow_html=True
    )

    # GitHub Button with link opening in a new tab
    st.title("Go To my GitHub")
    st.markdown(
        '<a href="https://github.com/Masoodkhan884" target="_blank" style="text-decoration:none;"><button style="background-color:#4CAF50; color:white; padding:10px 20px; border:none; border-radius:5px;">GitHub</button></a>',
        unsafe_allow_html=True
    )


def voice_to_text(source):
    r = sr.Recognizer()
    st.write("Say something!")
    audio = r.listen(source, phrase_time_limit=5)  # set a phrase time limit
    try:
        text = r.recognize_google(audio)
        return text, False  # return text and a flag indicating recording is not stopped
    except sr.UnknownValueError:
        return "Sorry, I didn't understand what you said", False
    except sr.RequestError as e:
        return "Error; {0}".format(e), False


def display_voice_to_text_output(text):
    st.write("You said: ", text)
    with open("voice_to_text_output.txt", "w") as f:
        f.write(text)


def main_app():
    st.title("Voice to Text App")

    # Create buttons for each functionality
    col1, col2, col3, col4 = st.columns(4)  # add a new column for the Stop Recording button
    recording_stopped = False  # initialize a flag to track recording status
    microphone = sr.Microphone()  # create a Microphone object
    with col1:
        if st.button("Start Recording"):
            with microphone as source:  # use the Microphone object
                text, recording_stopped = voice_to_text(source)
            st.session_state.text = text
            recording_stopped = False  # reset the flag
    with col2:
        if st.button("Stop Recording"):
            recording_stopped = True  # set the flag to stop recording
            st.write("Recording stopped")
    with col3:
        if st.button("Convert to Text"):
            if 'text' in st.session_state:
                display_voice_to_text_output(st.session_state.text)
            else:
                st.write("Please start recording first")
    with col4:
        if st.button("View Output File"):
            with open("voice_to_text_output.txt", "r") as f:
                st.write(f.read())


if __name__ == "__main__":
    main_app()