import streamlit as st
from streamlit_lottie import st_lottie
import requests
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Ezekiel Oluyale Portfolio",
    page_icon="logo.png",
    layout="wide"
)

# ---------- LOAD ANIMATIONS ----------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

contact_anim = load_lottie("https://assets9.lottiefiles.com/packages/lf20_t24tpvcu.json")

# ---------- CUSTOM CSS ----------
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

# ---------- SIDEBAR NAVIGATION ----------
st.sidebar.image("logo.png", width=120)
st.sidebar.title("Ezekiel Oluyale")
st.sidebar.markdown("**NLP Researcher & Machine Learning Engineer**")

pages = [
    "About Me",
    "Projects",
    "Skills",
    "Experience",
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

# ---------- PAGE CONTENT ----------

# ABOUT ME PAGE
if selected == "About Me":
    is_mobile = st.session_state.get("is_mobile", False)

    if is_mobile:
        st.image("profile.jpg", width=200)
        st.title("👋 Hi, I'm Ezekiel Oluyale")
        st.subheader("NLP Researcher & Machine Learning Engineer")

        # Compact LinkedIn + GitHub buttons (same line)
        st.markdown(
            """
            <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 20px;">
                <a href="https://www.linkedin.com/in/ezekiel-oluyale" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
                </a>
                <a href="https://github.com/amusEcode1" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:    
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("profile.jpg", width=200)
        with col2:
            st.title("👋 Hi, I'm Ezekiel Oluyale")
            st.subheader("NLP Researcher & Machine Learning Engineer")

            # Compact LinkedIn + GitHub buttons (same line)
            st.markdown(
                """
                <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 20px;">
                    <a href="https://www.linkedin.com/in/ezekiel-oluyale" target="_blank">
                        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
                    </a>
                    <a href="https://github.com/amusEcode1" target="_blank">
                        <img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write(
        """
        I'm a passionate developer focused on building **intelligent NLP applications** that make human–language interaction
        smarter and more accessible.  
            
        My journey began with curiosity about how machines understand text — and over time, I’ve worked on projects like **Sentiment Analysis**, 
        **Named Entity Recognition**, **Topic Modelling**, **Question Answering**, **Text Summarization**, and **Resume Screening**.

        I hold a Bachelor’s degree in **Computer Engineering** from the **Federal University of Oye-Ekiti**, Nigeria, where I developed a strong interest in **Natural Language Processing**.
            
        I enjoy transforming raw data into meaningful insights and currently exploring **Multilingual AI**, **Speech-Processing** and **Transformer-Based Models**
        to build smarter AI systems.
        """
        )

# PROJECTS PAGE
elif selected == "Projects":
    st.header("🚀 Featured NLP Projects")
    project_data = [
        {
            "title": "Text Summarization App",
            "desc": "Built an abstractive summarization app using fine-tuned transformer models to generate concise summaries.",
            "tech": "Python, Hugging Face, Streamlit",
            "link": "https://github.com/amusEcode/summarizer_model"
        },
        {
            "title": "Question Answering System",
            "desc": "Developed a system that answers questions from context using BERT fine-tuned on the SQuAD dataset.",
            "tech": "Transformers, Python, Streamlit",
            "link": "#"
        },
        {
            "title": "Named Entity Recognition",
            "desc": "Implemented a custom model for identifying entities such as people, organizations, and places in text.",
            "tech": "SpaCy, Rule-based Matching",
            "link": "#"
        }
    ]

    for proj in project_data:
        st.subheader(proj["title"])
        st.write(proj["desc"])
        st.caption(f"**Tech Used:** {proj['tech']}")
        st.link_button("🔗 View Project", proj["link"])
        st.markdown("---")

# SKILLS PAGE
elif selected == "Skills":
    st.header("🧠 Skills & Tools")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Programming:** Python, JavaScript")
        st.markdown("**ML Frameworks:** PyTorch, scikit-learn")
    with col2:
        st.markdown("**NLP Libraries:** SpaCy, NLTK, Transformers")
        st.markdown("**Tools:** Streamlit, Hugging Face, Git")
    with col3:
        st.markdown("**Concepts:** Tokenization, Embeddings, Fine-tuning, Topic Modeling")
    st.markdown("---")
    st.success("Always learning — expanding into Multilingual NLP & LLM fine-tuning.")

# EXPERIENCE PAGE
elif selected == "Experience":
    st.header("💼 Experience")
    st.subheader("NLP Intern — Elevvo Pathways (Remote)")
    st.write(
        """
        During my internship at **Elevvo Pathways**, I developed and deployed **8 end-to-end NLP projects** applying real-world
        concepts like text preprocessing, model fine-tuning, and evaluation.  
        
        My tasks spanned multiple domains — from **Named Entity Recognition** to **Topic Modeling**, **Summarization**, and 
        **Sentiment Analysis** — helping me transition from learner to hands-on NLP practitioner.
        """
    )
    st.caption("Jan 2025 – Oct 2025 | Remote Internship")

# CONTACT PAGE
elif selected == "Contact":
    st.header("📬 Get In Touch")
    col1, col2 = st.columns([1, 1])
    with col1:
        st_lottie(contact_anim, height=250, key="contact")
    with col2:
        st.markdown("""
        <form action="https://formsubmit.co/ezekieloluyale@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Your Name" required><br><br>
            <input type="email" name="email" placeholder="Your Email" required><br><br>
            <textarea name="message" placeholder="Your Message" required></textarea><br><br>
            <button type="submit">Send Message</button>
        </form>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.write("📞 **Phone:** +234 812 345 6789")
    st.write("📧 **Email:** [ezekieloluyale@gmail.com](mailto:ezekieloluyale@gmail.com)")
    st.write("🔗 **LinkedIn:** [Ezekiel Oluyale](https://www.linkedin.com/in/ezekiel-oluyale)")
    st.write("🔗 **GitHub:** [@amusEcode1](https://github.com/amusEcode1)")

# FOOTER
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#666;'>© 2025 Oluyale Ezekiel | Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
