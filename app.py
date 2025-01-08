import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai

import time
from pathlib import Path
import tempfile
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

# Page configuration
st.set_page_config(
    page_title="AI Video Editing Assistant",
    page_icon="✂️",
    layout="wide"
)

# Title and header
st.title("AI Video Editor Assistant ✂️🎥")
st.header("Powered by Gemini 2.0 Flash Experience")

# Cache the agent initialization to enhance performance
@st.cache_resource
def initialize_editor_agent():
    return Agent(
        name="AI Video Editor",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True,
    )

# Initialize the agent
video_editor_agent = initialize_editor_agent()

# File uploader for video
uploaded_video = st.file_uploader(
    "Upload your video file (mp4, mov, avi):",
    type=['mp4', 'mov', 'avi'],
    help="Choose a video file for AI-assisted editing."
)

if uploaded_video:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
        temp_file.write(uploaded_video.read())
        video_temp_path = temp_file.name
        
    st.markdown(
    """
    <style>
    video {
width: 70px; /* Adjust the width a needed */
        height: 400px;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Display the uploaded video
    st.video(video_temp_path, format="video/mp4", start_time=0)

    # User input for desired outcome
    editing_goal = st.text_area(
        "What is your goal for this video edit?",
        placeholder="E.g., Remove redundant content, highlight key moments, etc.",
        help="Provide specific goals for the AI to analyze and recommend edits."
    )

    # Button to trigger analysis
    if st.button("✂️ Analyze and Suggest Edits", key="analyze_video_button"):
        if not editing_goal:
            st.warning("Please enter your editing goals.")
        else:
            try:
                with st.spinner("Analyzing video and generating editing suggestions..."):
                    # Upload and process the video file
                    uploaded_video_data = upload_file(video_temp_path)
                    while uploaded_video_data.state.name == "PROCESSING":
                        time.sleep(1)
                        uploaded_video_data = get_file(uploaded_video_data.name)

                    # Generate editing suggestions prompt
                    edit_request = (
                        f"""
                        Analyze the uploaded video for redundant content, key moments, and actionable editing suggestions.
                        Respond to the following goal with timestamps and clear guidance:
                        {editing_goal}

                        Provide detailed timestamps for cuts, redundant sections, and highlight key segments to retain.
                        """
                    )

                    # Run the agent for analysis
                    edit_suggestions = video_editor_agent.run(
                        edit_request, videos=[uploaded_video_data]
                    )

                # Display the result
                st.subheader("Editing Suggestions")
                st.markdown(edit_suggestions.content)

            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
            finally:
                # Cleanup temporary file
                Path(video_temp_path).unlink(missing_ok=True)
else:
    st.info("Upload a video to start editing suggestions.")

# Custom CSS for text area height
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 120px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
