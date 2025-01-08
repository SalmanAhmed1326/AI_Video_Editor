
# **AI Video Editing Assistant**

An AI-powered tool that streamlines video editing by analyzing content, suggesting cuts with timestamps, and removing redundant sections while retaining essential information. Powered by advanced AI models, this application enables smarter and faster video editing workflows.

---

## **Features**

### **Key Highlights**
- **Upload Video Files**: Supports popular formats like MP4, MOV, and AVI.  
- **AI-Driven Analysis**: Automatically detects redundant content, highlights key moments, and suggests edits.  
- **Custom Editing Goals**: Users can specify editing requirements (e.g., "Remove redundant content," "Highlight key moments").  
- **Timestamped Suggestions**: Provides clear recommendations with timestamps for cuts and highlights.  
- **Interactive Interface**: Built with Streamlit for an intuitive and user-friendly UI.

### **Supported AI Models**
- **Gemini 2.0 Flash**: Multimodal content analysis for video editing.  
- **DuckDuckGo Integration**: Supplementary research for better contextual understanding.

---

## **About**
This multimodal **AI Video Editing Assistant** is created using the **Phidata framework** and **Gemini**. While it is not a fully advanced agentic system, it provides a solid foundation for intelligent video editing assistance. Continuous improvements are being made, and we welcome feedback to enhance its capabilities further.

---

## **Getting Started**

### **Prerequisites**
- **Python**: Version 3.8 or higher.  
- **API Key**: Google Generative AI.  
- **Required Libraries**:
  - `streamlit`
  - `phi`
  - `google-generativeai`
  - `dotenv`

---

### **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ai-video-editing-assistant.git
   cd ai-video-editing-assistant
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the project root.
   - Add your Google API key and Phidata API Key:
     ```plaintext
     PHIDATA_API_KEY=your_phidata_api_key_here
     GOOGLE_API_KEY=your_google_api_key_here
     ```

---

### **Running the Application**

1. **Start the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

2. **Access the Application**:
   - Open your browser at the URL provided by Streamlit (typically `http://localhost:8501`).

---

## **Usage**

### **1. Upload Video**
- Upload a video file in MP4, MOV, or AVI format.
- The video will be displayed in the app interface.

### **2. Specify Editing Goals**
- Enter your goals in the text area, such as:
  - "Remove repeated sections."
  - "Highlight key moments."

### **3. Generate Suggestions**
- Click the **"Analyze and Suggest Edits"** button to start the AI-driven analysis.  
- View the results, including timestamps and actionable editing recommendations.

---

### **Example Output**

#### **Input**
- **Video Goal**: "Remove redundant sections and highlight emotional moments."

#### **Output**
- **Suggestions**:
  - `00:00:30 - 00:00:45`: Remove (repeated introduction).
  - `00:01:10 - 00:01:30`: Keep (important highlight).
  - `00:03:15 - 00:03:45`: Remove (off-topic).

---

## **Contributing**

We welcome contributions to enhance this project. Please follow these steps:

1. **Fork the Repository**:
   ```bash
   git fork https://github.com/yourusername/ai-video-editing-assistant.git
   ```
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit Your Changes**:
   ```bash
   git commit -m "Add your message here"
   ```
4. **Push to the Branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request**.


---

# **Example Questions for AI Video Editing Agent**

Leverage the AI Video Editing Agent to get tailored and actionable insights for improving your videos. Here are some example questions you can ask to receive better and more specific results:

---

## **1. General Editing Suggestions**  
- "Analyze the video and suggest edits to improve clarity and engagement."  
- "What parts of this video should be cut out to improve pacing and keep the viewer's attention?"

---

## **2. Content-Specific Edits**  
- "Can you highlight the key moments in this video and suggest how to make them more impactful?"  
- "Which segments of this video can be trimmed or removed without losing important context?"

---

## **3. Improving Quality**  
- "Suggest edits to improve the audio and video quality, such as color correction or noise reduction."  
- "Identify any visual distractions or inconsistencies and recommend ways to fix them."

---

## **4. Narrative Enhancements**  
- "How can the flow of the video be improved? Are there any parts where the narrative feels disjointed?"  
- "Could you suggest a more engaging intro or outro for this video?"

---

## **5. Cut and Highlight Specific Sections**  
- "Please identify sections of the video that should be shortened or removed for better conciseness."  
- "What parts of the video should be highlighted to create a more powerful message?"

---

## **6. Add Creative Effects**  
- "Suggest creative edits, such as transitions, text overlays, or effects, to make this video more engaging."  
- "Can you recommend special effects or graphics to enhance the visual appeal of this video?"

---

## **7. Improving Audience Engagement**  
- "What are the best parts of this video to highlight for maximum audience engagement?"  
- "Where can I add call-to-action elements in this video to drive more viewer interaction?"

---

## **8. Optimizing for Social Media**  
- "How can this video be optimized for social media platforms (e.g., Instagram, TikTok)?"  
- "Can you suggest edits to make this video more shareable on platforms like YouTube and Instagram?"

---

### **Why Ask These Questions?**
These targeted questions guide the AI agent to provide actionable suggestions for improving your video. Whether you're optimizing for clarity, engagement, or platform-specific requirements, these prompts ensure a more efficient and impactful editing process.

---

Feel free to copy and modify these examples to suit your specific video editing needs! 💻🎥  


---
## **Acknowledgements**
- **Streamlit**: For providing the web application framework.  
- **Google Generative AI**: For advanced video and content analysis.  
- **DuckDuckGo API**: For supplementary information retrieval.

---

## **Contact**
For any questions or feedback, please reach out at **sh13jj2648@gmail.com**.  

---

**Happy Editing!** 🎥✨


