import streamlit as st
from streamlit_lottie import st_lottie
import requests
import os

# PAGE CONFIG 
st.set_page_config(
    page_title="Ezekiel Oluyale Portfolio",
    page_icon="logo.png",
    layout="wide"
)

# LOAD ANIMATIONS 
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

contact_anim = load_lottie("https://assets9.lottiefiles.com/packages/lf20_t24tpvcu.json")

# CUSTOM CSS 
st.markdown("""
<style>

body {
    background-color: #f7faff;
}

h1, h2, h3, h4 {
    color: #003366;
}

img {
    border-radius: 20px;
}

button {
    background-color: #003366 !important;
    color: white !important;
    border-radius: 10px !important;
}

button:hover {
    background-color: #05c !important;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR NAVIGATION 
st.sidebar.image("logo.png", width=120)
st.sidebar.title("Ezekiel Oluyale")
st.sidebar.markdown("**NLP Researcher & Machine Learning Engineer**")

pages = [
    "About Me",
    "Projects",
    "Contact"
]
selected = st.sidebar.radio("Navigate", pages)

st.sidebar.markdown("---")

cv_path = "Ezekiel_Oluyale_Resume.pdf"
if os.path.exists(cv_path):
    with open(cv_path, "rb") as pdf_file:
        st.sidebar.download_button(
            label="📄 Download CV",
            data=pdf_file.read(),
            file_name="Ezekiel_Oluyale_Resume.pdf",
            mime="application/pdf",
        )
else:
    st.sidebar.warning("⚠️ CV not found. Upload it later.")

import streamlit as st

# ABOUT ME PAGE 
if selected == "About Me":
    # Main container
    with st.container():
        st.markdown(
            """
            <style>
                /* Make social buttons inline and add hover */
                .social-links {
                    display: flex;
                    gap: 10px;
                    align-items: center;
                    margin-top: 8px;
                    margin-bottom: 25px;
                }
                .social-links img {
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                    border-radius: 6px;
                }
                .social-links img:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 4px 10px rgba(0,0,0,0.25);
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Use adaptive columns
        col1, col2 = st.columns([1, 2], gap="medium")

        with col1:
            st.markdown(
                """
                <div style="display: flex; justify-content: center;">
                    <img src="https://raw.githubusercontent.com/amusEcode1/My-Portfolio/main/profile.jpg" 
                         style="width: 250px; height: 250px; object-fit: cover; border-radius: 50%; border: 3px solid #ddd;" alt="Ezekiel Oluyale">
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.title("Ezekiel Oluyale")
            st.subheader("NLP Researcher & Machine Learning Engineer")

            # Social buttons
            st.markdown(
                """
                <div class="social-links">
                    <a href="https://www.linkedin.com/in/ezekiel-oluyale" target="_blank">
                        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="35" height="35" style="border-radius: 5px;">
                    </a>
                    <a href="https://github.com/amusEcode1" target="_blank">
                        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="35" height="35" style="border-radius: 5px;">  
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.write(
                """
                I'm a passionate developer focused on building **intelligent NLP applications** that make human–language interaction
                smarter and more accessible.  
                
                My journey began with curiosity about how machines understand text — and over time, I’ve worked on projects like 
                **Sentiment Analysis**, **Named Entity Recognition**, **Topic Modelling**, **Question Answering**, **Text Summarization**, 
                and **Resume Screening**.

                I hold a First-Class Bachelor’s degree in **Computer Engineering** from the **Federal University of Oye-Ekiti**, Nigeria, where I developed 
                a strong interest in **Natural Language Processing**.
                
                I enjoy transforming raw data into meaningful insights and currently exploring **Multilingual AI**, **Speech-Processing**, 
                and **Transformer-Based Models** to build smarter AI systems.
                """
            )

# PROJECTS PAGE
elif selected == "Projects":
    st.header("🚀 Featured NLP Projects")
    project_data = [
         {
            "title": "Product Review — Sentiment Analysis",
            "desc": "A Sentiment Analysis System using the IMDb reviews dataset to classify product reviews as positive or negative.",
            "tech": "Python, NumPy, Pandas, Matplotlib, Seaborn, WordCloud, BeautifulSoup, NLTK, Scikit-learn, Streamlt, Colab",
            "link": "https://reviewpredictor.streamlit.app/"
        },
         {
            "title": "Fake News Detection System",
            "desc": "A Fake News Detection System using the Fake and Real News dataset designed to detect fake news by classifying news articles as real or fake.",
            "tech": "Python, NumPy, Pandas, Matplotlib, Seaborn, WordCloud, BeautifulSoup, spaCy, Scikit-learn, Streamlt, Colab",
            "link": "https://news-verifier.streamlit.app/"
        },
         {
            "title": "Named Entity Recognition",
            "desc": "A Named Entity Recognition (NER) System for News Articles using the CoNLL003 dataset to automatically extract and categorize entities like people, locations, organizations, et.c from real-world text.",
            "tech": "Python, Pandas, spaCy, Streamlt, Colab",
            "link": "https://named-entity-extraction-news.streamlit.app/"
        },
         {
            "title": "Topic Modelling System",
            "desc": "A Topic Modeling System for News Articles using the BBC News Dataset to discover hidden topics or themes in a collection of News Articles or Blog posts.",
            "tech": "Python, NumPy, Pandas, Matplotlib, Seaborn, WordCloud, BeautifulSoup, NLTK, Scikit-learn, pyLDAvis, Streamlit, Colab",
            "link": "https://news-articles-modelling.streamlit.app/"
        },
         {
            "title": "Question Answering System",
            "desc": "A Question Answering System that answers questions based on a given passage or context using pre-trained transformer models fine-tuned on the Stanford Question Answering dataset",
            "tech": "Python, Pandas, PyTorch, Evaluate, Transformers, Streamlit, Colab",
            "link": "https://ask-me-ai.streamlit.app/"
        },
         {
            "title": "Text Summarization App",
            "desc": "An Abstractive and Extractive summarization app that generates concise summaries from long articles using pre-trained transformer model (T5) fine-tuned on the CNN/DailyMail Dataset.",
            "tech": "Python, Pandas, NLTK, spaCy, BeautifulSoup4, pytextrank, Datasets, rouge-score, Transformers, Streamlit, Colab",
            "link": "https://concise-ai.streamlit.app/"
        },
         {
            "title": "Resume Screening & Matching System",
            "desc": "A Resume Screening System that screen and rank resumes based on Job descriptions using both Resume and Job Dataset.",
            "tech": "Python, Pandas, NumPy, Sentence-Transformers, BeautifulSoup4, pdfplumber, python-docs, tqdm, spaCy, Streamlit, Colab",
            "link": "https://resume-qualify.streamlit.app/"
        }
    ]

    for proj in project_data:
        st.subheader(proj["title"])
        st.write(proj["desc"])
        st.caption(f"**Tech Stack & Tools:** {proj['tech']}")
        st.link_button("🌐 View Project", proj["link"])
        st.markdown("---")

# CONTACT PAGE
elif selected == "Contact":
    st.header("📩 Get In Touch")
    col1, col2 = st.columns([1, 1])
    with col1:
        st_lottie(contact_anim, height=250, key="contact")
    with col2:
        st.markdown("""
        <form action="https://formspree.io/f/mblpdjll" method="POST" target="_blank">
            <input type="text" name="name" placeholder="Your Name" required><br><br>
            <input type="email" name="email" placeholder="Your Email" required><br><br>
            <textarea name="message" placeholder="Your Message" required></textarea><br><br>
            <button type="submit">Send Message</button>
        </form>
        """, unsafe_allow_html=True)
    st.markdown("---")
    
    # Socials with logos + names
    st.markdown(
        """
        <div style='display: flex; flex-direction: column; gap: 10px; margin-top: 10px;'>
            <div>📲&nbsp;&nbsp;&nbsp;<b>Phone:</b> (+234) 814 829 9173</div>
            <div>📧&nbsp;&nbsp;&nbsp;<b>Email:</b> <a href='mailto:ezekieloluyale@gmail.com'>ezekieloluyale@gmail.com</a></div>
            <div style='display: flex; align-items: center; gap: 10px;'>
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn", width=20>
                <span><b>LinkedIn:</b> <a href='https://www.linkedin.com/in/ezekiel-oluyale' target='_blank'>Ezekiel Oluyale</a></span>
            </div>
            <div style='display: flex; align-items: center; gap: 10px;'>
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub", width=20>
                <span><b>GitHub:</b> <a href='https://github.com/amusEcode1' target='_blank'>@amusEcode1</a></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
# FOOTER
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#666;'>© 2025 Ezekiel Oluyale — All rights reserved.</p>",
    unsafe_allow_html=True
)
