# app.py
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import os

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Oluyale Ezekiel | NLP & ML Portfolio",
    page_icon="🤖",
    layout="wide",
)

# -------------------- COLORS --------------------
PRIMARY = "#004aad"
HOVER = "#005fcc"
ACCENT = "#e8f1ff"
BG = "#f9fbff"
TEXT = "#1f2a44"

# -------------------- LOTTIE HELPERS --------------------
def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=6)
        if r.status_code == 200:
            return r.json()
    except Exception:
        return None
    return None

nlp_lottie_url = "https://lottie.host/f3a325cf-9441-4df9-b22b-52ac0b9bb8a3/tBbTgoUQ8r.json"  # NLP/ML themed animation
contact_lottie_url = "https://lottie.host/8b67e0d4-fdd3-479b-9f2d-fec8d1af7fc4/nfE4vO1y4g.json"
nlp_anim = load_lottie(nlp_lottie_url)
contact_anim = load_lottie(contact_lottie_url)

# -------------------- STYLES --------------------
st.markdown(
    f"""
<style>
:root {{
  --primary: {PRIMARY};
  --hover: {HOVER};
  --accent: {ACCENT};
  --bg: {BG};
  --text: {TEXT};
}}

html, body, [class*="stApp"] {{
  background-color: var(--bg);
  color: var(--text);
  font-family: "Inter", sans-serif;
}}

h1, h2, h3 {{
  color: var(--primary);
  font-weight: 700;
}}

hr {{
  border: none;
  border-top: 1px solid rgba(0,0,0,0.06);
  margin: 25px 0;
}}

/* Sidebar */
[data-testid="stSidebar"] {{
  background: white;
  border-right: 1px solid rgba(0,0,0,0.05);
  padding-top: 18px;
}}

[data-testid="stSidebar"] label {{
  padding: 8px 10px;
  display: block;
  border-radius: 6px;
  transition: all 0.2s ease;
  cursor: pointer;
}}

[data-testid="stSidebar"] label:hover {{
  background-color: rgba(0,74,173,0.07);
  color: var(--primary);
}}

[data-testid="stSidebar"] input[type="radio"]:checked + label {{
  background-color: rgba(0,74,173,0.10);
  color: var(--primary);
  font-weight: 600;
  box-shadow: 0 2px 6px rgba(0,74,173,0.15);
}}

[data-testid="stSidebar"] input[type="radio"] {{
  accent-color: var(--primary);
}}

.stButton>button {{
  background-color: var(--primary);
  color: white;
  border: none;
  border-radius: 8px;
  padding: 8px 16px;
  font-weight: 600;
  transition: all 0.2s ease;
}}
.stButton>button:hover {{
  background-color: var(--hover);
  transform: translateY(-2px);
}}

.project-card {{
  background: white;
  border-radius: 12px;
  padding: 18px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.03);
  border: 1px solid rgba(0,0,0,0.05);
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}}
.project-card:hover {{
  transform: translateY(-3px);
  box-shadow: 0 8px 18px rgba(0,0,0,0.06);
}}

.skill-badge {{
  background-color: var(--accent);
  color: var(--primary);
  padding: 6px 10px;
  border-radius: 999px;
  margin: 4px;
  font-size: 13px;
  font-weight: 600;
  display: inline-block;
}}

.profile-img {{
  border-radius: 50%;
  border: 4px solid rgba(0,0,0,0.05);
}}
</style>
""",
    unsafe_allow_html=True,
)

# -------------------- SIDEBAR --------------------
st.sidebar.image(
    "https://i.imgur.com/9QpP2hZ.png",
    width=150,
    caption="Oluyale Ezekiel",
    use_container_width=False
)
st.sidebar.markdown("**NLP & Machine Learning Enthusiast** 🤖")
st.sidebar.divider()

all_skills = ["Transformers", "NLP", "Summarization", "QA", "NER", "Topic Modeling", "Sentiment"]
skill_filter = st.sidebar.selectbox("🔍 Filter Projects by Skill", options=["All"] + all_skills, index=0)

st.sidebar.divider()
st.sidebar.markdown("📧 [oluyale.ezekiel@example.com](mailto:oluyale.ezekiel@example.com)")
st.sidebar.markdown("🔗 [LinkedIn](https://linkedin.com/in/oluyaleezekiel)")
st.sidebar.markdown("🐙 [GitHub](https://github.com/amusEcode)")
st.sidebar.divider()

cv_path = "Ezekiel_Oluyale_Resume.pdf"
if os.path.exists(cv_path):
    with open(cv_path, "rb") as f:
        st.sidebar.download_button("📄 Download CV", f.read(), file_name="Ezekiel_Oluyale_Resume.pdf", mime="application/pdf")
else:
    st.sidebar.info("Upload your CV to enable this button.")

st.sidebar.divider()

pages = ["About", "Projects", "Skills", "Experience", "Contact"]
page = st.sidebar.radio("Navigate", pages)

# -------------------- PAGE CONTENT --------------------
if page == "About":
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.markdown('<img class="profile-img" src="https://i.imgur.com/9QpP2hZ.png" width="200"/>', unsafe_allow_html=True)
        st.markdown("**📍 Nigeria**")
        st.markdown("**💼 Open to:** Remote Roles / MSc Supervision")
    with col2:
        st.title("Hi, I'm Oluyale Ezekiel")
        st.subheader("Machine Learning & NLP Enthusiast")
        st.write(
            """
            I build intelligent NLP systems that turn text into actionable insights.
            My focus areas include **summarization**, **question answering**, **NER**, and **sentiment analysis** —
            with a growing interest in multilingual NLP applications.
            """
        )
        st.markdown("**Quick highlights:**")
        st.markdown("""
        - 🎓 From learning tokenization to fine-tuning transformers  
        - 🛠 Delivering end-to-end NLP projects (data → deployment)  
        - 🌍 Advocating for multilingual NLP accessibility
        """)
    st.divider()
    if nlp_anim:
        st_lottie(nlp_anim, height=320)
    else:
        st.info("Animation failed to load — you can replace the Lottie URL.")

elif page == "Projects":
    st.header("🚀 Featured Projects")
    projects = [
        {"title": "Abstractive Text Summarizer", "summary": "Fine-tuned a transformer model to generate concise summaries.", "skills": ["Summarization", "Transformers", "NLP"], "repo": "https://github.com/amusEcode/summarizer_model"},
        {"title": "Question Answering System", "summary": "Built a contextual QA system using BERT fine-tuned on SQuAD.", "skills": ["QA", "Transformers"], "repo": "https://github.com/amusEcode/qa_system"},
        {"title": "Named Entity Recognition", "summary": "Hybrid rule-based + SpaCy NER for domain-specific extraction.", "skills": ["NER"], "repo": "https://github.com/amusEcode/ner_project"},
        {"title": "Yorùbá Sentiment Classifier", "summary": "Developed multilingual sentiment model using SVM + BERT.", "skills": ["Sentiment", "NLP"], "repo": "https://github.com/amusEcode/yoruba_sentiment"},
    ]

    filtered = [p for p in projects if skill_filter == "All" or skill_filter in p["skills"]]
    cols = st.columns(2, gap="large")
    for i, proj in enumerate(filtered):
        with cols[i % 2]:
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.subheader(proj["title"])
            st.write(proj["summary"])
            st.markdown("".join([f"<span class='skill-badge'>{s}</span>" for s in proj["skills"]]), unsafe_allow_html=True)
            st.markdown(f"[🔗 View Repository]({proj['repo']})")
            st.markdown("</div>", unsafe_allow_html=True)

elif page == "Skills":
    st.header("🧠 Technical Skills")
    st.markdown("Explore my toolkit for NLP & ML development.")
    cols = st.columns(3)
    skills = ["Transformers", "SpaCy", "Scikit-learn", "PyTorch", "Pandas", "Streamlit", "Hugging Face", "Matplotlib", "Numpy"]
    for i, skill in enumerate(skills):
        with cols[i % 3]:
            st.markdown(f"<div class='project-card'><b>{skill}</b></div>", unsafe_allow_html=True)

elif page == "Experience":
    st.header("💼 Professional Experience")
    st.markdown("""
    **NLP Intern — Elevvo Pathways (Remote)**  
    *Jan 2025 – Oct 2025*  
    - Built 8 end-to-end NLP projects (Summarization, QA, NER, Sentiment)  
    - Worked on data cleaning, fine-tuning, and Streamlit deployment  
    ---
    **Freelance NLP Developer**  
    *2024 – Present*  
    - Built prototype NLP tools for content analysis and moderation  
    """)

elif page == "Contact":
    st.header("📬 Get in Touch")
    col1, col2 = st.columns([1, 1])
    with col1:
        if contact_anim:
            st_lottie(contact_anim, height=260)
    with col2:
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            msg = st.text_area("Message")
            submitted = st.form_submit_button("Send (Demo)")
            if submitted:
                st.success("Thanks! This is a demo. Connect with me on LinkedIn or email.")

st.divider()
st.markdown("<p style='text-align:center; color:gray;'>© 2025 Oluyale Ezekiel — Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
