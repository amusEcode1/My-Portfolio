import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ----- PAGE CONFIG -----
st.set_page_config(page_title="Oluyale Ezekiel | NLP & ML Portfolio", layout="wide")

# ----- LOAD LOTTIE -----
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# NLP/ML themed Lottie animation
nlp_ml_lottie = load_lottie_url("https://lottie.host/1aee4318-90d3-4560-b0e9-3d9f94635d2f/QyToM6Sgxt.json")

# ----- SIDEBAR -----
with st.sidebar:
    st.title("🔍 Portfolio Navigation")
    search_query = st.text_input("Search Projects or Skills", placeholder="Type to search...")
    st.markdown("---")
    selected = st.radio(
        "Sections",
        ["About Me", "Projects", "Skills", "Experience", "Contact"],
        index=0
    )

# ----- CUSTOM STYLES -----
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #f7faff;
            color: #004aad;
        }
        div[role="radiogroup"] > label {
            padding: 5px 10px;
            border-radius: 8px;
        }
        div[role="radiogroup"] > label:hover {
            background-color: #dce9ff;
            transition: all 0.3s ease;
        }
        div[role="radiogroup"] > label[data-checked="true"] {
            background-color: #004aad;
            color: white !important;
        }
        div.stButton > button:hover {
            background-color: #0066cc;
            color: white;
            transition: 0.3s ease;
        }
        h1, h2, h3, h4 {
            color: #004aad;
        }
    </style>
""", unsafe_allow_html=True)

# ----- ABOUT ME -----
if selected == "About Me":
    st.header("👋 About Me")
    left, mid, right = st.columns([1, 1.5, 1])

    with left:
        st.image("https://i.imgur.com/qG2H6rD.png", width=250)
    with mid:
        st.write("""
        I'm **Oluyale Ezekiel**, a passionate **Machine Learning and NLP Engineer** dedicated to building 
        intelligent systems that process and understand human language.  
        
        My work focuses on projects involving **Sentiment Analysis**, **Text Summarization**, **NER**, 
        and **Question Answering Systems** using deep learning and transformer-based models.  

        I enjoy turning ideas into functional ML solutions and creating tools that make data talk.
        """)
        st.markdown("🌍 Based in Nigeria | 🤝 Open to remote roles and collaborations")
    with right:
        if nlp_ml_lottie:
            st_lottie(nlp_ml_lottie, height=280, key="nlpml")

# ----- PROJECTS -----
elif selected == "Projects":
    st.header("🧠 Projects")
    st.markdown("Explore some of the NLP & ML projects I’ve worked on.")

    # Filter via search bar
    projects = {
        "Sentiment Analysis": "Built a model to classify text sentiment (positive, negative, neutral) using SVM and BERT.",
        "Question Answering System": "Developed a QA system using fine-tuned transformer models (SQuAD dataset).",
        "Topic Modeling": "Used LDA & NMF to discover hidden themes in news articles.",
        "Text Summarization": "Built an abstractive text summarizer using transformer-based models."
    }

    for title, desc in projects.items():
        if search_query.lower() in title.lower() or search_query.lower() in desc.lower():
            st.subheader(f"📘 {title}")
            st.write(desc)
            st.image("https://i.imgur.com/dR9zGJx.png", use_container_width=True)
            st.markdown("---")

# ----- SKILLS -----
elif selected == "Skills":
    st.header("🧩 Technical Skills")
    st.markdown("Hover over a skill to explore more.")
    skills = {
        "Machine Learning": ["Scikit-learn", "TensorFlow", "PyTorch", "Model Optimization"],
        "Natural Language Processing": ["spaCy", "Hugging Face", "NER", "Text Summarization", "Sentiment Analysis"],
        "Programming": ["Python", "Git", "Streamlit", "Jupyter", "VS Code"]
    }

    for category, items in skills.items():
        with st.expander(f"💡 {category}"):
            st.write(", ".join(items))

# ----- EXPERIENCE -----
elif selected == "Experience":
    st.header("💼 Experience")
    st.subheader("Elevvo Pathways — NLP Intern (2025)")
    st.write("""
    - Applied NLP concepts to real-world datasets, building and deploying production-grade models.  
    - Completed 8 projects: NER, Sentiment Analysis, Topic Modeling, Text Summarization, and QA Systems.  
    - Improved proficiency in data preprocessing, model fine-tuning, and deployment using Streamlit.  
    - Collaborated remotely under expert mentorship and learned best ML practices.
    """)

# ----- CONTACT -----
elif selected == "Contact":
    st.header("📬 Contact Me")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success(f"Thank you, {name}! Your message has been received successfully.")

    st.markdown("---")
    st.markdown("📧 **Email:** oluyaleezekiel@gmail.com")
    st.markdown("📱 **Phone:** +234 812 345 6789")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/oluyaleezekiel)")
    st.download_button(
        label="📄 Download My CV",
        data=open("Ezekiel_Oluyale_Resume.pdf", "rb").read(),
        file_name="Ezekiel_Oluyale_Resume.pdf",
        mime="application/pdf"
    )
