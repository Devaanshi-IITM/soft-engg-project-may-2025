import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
from streamlit_webrtc import WebRtcMode
#import openai
import numpy as np
import queue
import tempfile

# openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="AI Voice Assistant", layout="wide")
st.sidebar.markdown("## 🎙️ Voice AI Assistant Dashboard")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("### Talk to your AI Assistant")

# show conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# voice recorder
class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.q = queue.Queue()

    def recv_audio(self, frame):
        # get PCM audio
        pcm_data = frame.to_ndarray()
        self.q.put(pcm_data)
        return frame



webrtc_ctx = webrtc_streamer(
    key="speech",
    mode=WebRtcMode.SENDONLY,
    audio_receiver_size=256,
    media_stream_constraints={"audio": True, "video": False},
    audio_processor_factory=AudioProcessor,
)


# after recording
if webrtc_ctx and webrtc_ctx.state.playing:
    audio_frames = []
    while not webrtc_ctx.audio_receiver.queue.empty():
        audio_frames.append(webrtc_ctx.audio_receiver.queue.get())

    if audio_frames:
        # convert PCM data to wav
        pcm = np.concatenate(audio_frames)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(pcm.tobytes())
            tmp_filename = f.name

        # use Whisper:
        # transcript = openai.Audio.transcribe("whisper-1", open(tmp_filename, "rb"))
        transcript = {"text": "This is a test transcription"}  # simulate

        user_text = transcript["text"]
        st.session_state.messages.append({"role": "user", "content": user_text})

        # get LLM reply
        # response = openai.ChatCompletion.create(...)
        # assistant_text = response["choices"][0]["message"]["content"]
        assistant_text = f"🤖 You said: {user_text}"
        st.session_state.messages.append({"role": "assistant", "content": assistant_text})

        with st.chat_message("user"):
            st.markdown(user_text)
        with st.chat_message("assistant"):
            st.markdown(assistant_text)

        st.rerun()

# clear
if st.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()
