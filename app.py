# app.py
import streamlit as st
from streamlit_lottie import st_lottie
import requests

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Oluyale Ezekiel | NLP & ML Portfolio",
    page_icon="🤖",
    layout="wide",
)

# -------------------- LOAD LOTTIE ANIMATION --------------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Example Lottie URLs (replace with others if you wish)
lottie_home = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_yd8fbnml.json")
lottie_skills = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tfb3estd.json")
lottie_projects = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_experience = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ydo1amjm.json")
lottie_contact = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")

# -------------------- NAVBAR STYLE --------------------
st.markdown("""
    <style>
        .topnav {
            background-color: #004aad;
            overflow: hidden;
            padding: 10px 20px;
            border-radius: 0 0 12px 12px;
        }
        .topnav a {
            float: left;
            color: white;
            text-align: center;
            padding: 10px 16px;
            text-decoration: none;
            font-size: 17px;
            font-weight: 500;
        }
        .topnav a:hover {
            background-color: #0056d1;
            color: #fff;
            border-radius: 8px;
        }
        .hamburger {
            font-size: 22px;
            cursor: pointer;
            color: white;
            padding: 0 16px;
            float: left;
        }
        .menu {
            display: none;
            flex-direction: column;
            background-color: #004aad;
            border-radius: 0 0 10px 10px;
        }
        .menu a {
            color: white;
            padding: 10px 16px;
            text-decoration: none;
            font-size: 16px;
            text-align: left;
        }
        .menu a:hover {
            background-color: #0056d1;
            border-radius: 6px;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- JAVASCRIPT (TOGGLE MENU) --------------------
st.markdown("""
<script>
function toggleMenu() {
    var menu = window.parent.document.querySelector('.menu');
    if (menu.style.display === 'flex') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'flex';
    }
}
</script>
""", unsafe_allow_html=True)

# -------------------- NAVBAR HTML --------------------
st.markdown("""
<div class="topnav">
    <span class="hamburger" onclick="toggleMenu()">☰</span>
    <a style="font-size:18px;font-weight:600;">Oluyale Ezekiel</a>
</div>
<div class="menu">
    <a href="?page=Home">🏠 Home</a>
    <a href="?page=Skills">🧠 Skills</a>
    <a href="?page=Projects">🚀 Projects</a>
    <a href="?page=Experience">📚 Experience</a>
    <a href="?page=Contact">📞 Contact</a>
</div>
""", unsafe_allow_html=True)

# -------------------- HELPER: SET/GET PAGE --------------------
def get_page():
    """Return current active page from query parameters."""
    if "page" in st.query_params:
        return st.query_params["page"]
    else:
        st.query_params["page"] = "Home"
        return "Home"

page = get_page()

# -------------------- HOME PAGE --------------------
if page == "Home":
    col1, col2 = st.columns([1, 1])
    with col1:
        try:
            st.image("assets/profile.png", width=300)
        except Exception:
            st.write("⚠️ Add your profile image to `assets/profile.png`")
    with col2:
        st.title("👋 Hi, I'm Oluyale Ezekiel")
        st.subheader("NLP & Machine Learning Engineer")
        st.write("""
            I build intelligent systems that understand and process human language.  
            My work spans Natural Language Processing (NLP) and Machine Learning — from **Text Summarization** to **Sentiment Analysis**.
        """)
        if lottie_home:
            st_lottie(lottie_home, height=250, key="home")
        st.markdown("""
        <br>
        <a href="https://github.com/yourgithub" target="_blank">🔗 GitHub</a> |
        <a href="https://linkedin.com/in/yourlinkedin" target="_blank">💼 LinkedIn</a> |
        <a href="assets/resume.pdf" target="_blank">📄 Resume</a>
        """, unsafe_allow_html=True)
    st.divider()
    cols = st.columns(2)
    cols[0].metric("Projects", "5+")
    cols[1].metric("Specialization", "NLP & ML")

# -------------------- SKILLS PAGE --------------------
elif page == "Skills":
    st.header("🧠 Skills")
    if lottie_skills:
        st_lottie(lottie_skills, height=200)
    st.write("### Languages")
    st.progress(90)
    st.text("Python (Advanced)")
    st.write("### Frameworks & Libraries")
    st.text("Transformers · Scikit-learn · PyTorch · Pandas · NumPy")
    st.write("### Tools & Platforms")
    st.text("Streamlit · Git · Hugging Face · Jupyter")

# -------------------- PROJECTS PAGE --------------------
elif page == "Projects":
    st.header("🚀 Projects")
    if lottie_projects:
        st_lottie(lottie_projects, height=200)
    project_data = [
        {
            "title": "Yorùbá Sentiment Analyzer",
            "desc": "Classifies Yorùbá tweets as positive, negative, or neutral using transformer-based models.",
            "tech": "Python · BERT · NLP",
            "github": "https://github.com/yourgithub",
        },
        {
            "title": "Text Summarizer",
            "desc": "Abstractive summarization using transformer models fine-tuned on news datasets.",
            "tech": "Python · Hugging Face · Streamlit",
            "github": "https://github.com/yourgithub",
        },
        {
            "title": "Topic Modeling",
            "desc": "Automatically discovers hidden themes in documents using LDA and NMF.",
            "tech": "Python · scikit-learn · NLP",
            "github": "https://github.com/yourgithub",
        },
    ]
    for p in project_data:
        st.subheader(p["title"])
        st.write(p["desc"])
        st.write(f"**Tech Stack:** {p['tech']}")
        st.markdown(f"[🔗 View Code]({p['github']})")
        st.divider()

# -------------------- EXPERIENCE PAGE --------------------
elif page == "Experience":
    st.header("📚 Experience & Education")
    if lottie_experience:
        st_lottie(lottie_experience, height=200)
    st.write("### 🏢 Elevvo Pathways — NLP Intern")
    st.write("""
        Worked on Named Entity Recognition, Topic Modeling, and Text Summarization systems.  
        Applied transformer-based models and preprocessing pipelines to real-world text data.
    """)
    st.write("### 🎓 Federal University of Oye-Ekiti")
    st.write("Bachelor of Engineering (B.Eng) in Computer Engineering")
    st.write("### 🎯 Research Interests")
    st.write("Multilingual NLP, Transformer optimization, and applied ML.")

# -------------------- CONTACT PAGE --------------------
elif page == "Contact":
    st.header("📞 Contact Me")
    if lottie_contact:
        st_lottie(lottie_contact, height=200)
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Send"):
            if name and email and message:
                st.success("✅ Message sent successfully!")
            else:
                st.warning("Please fill all fields before sending.")

# -------------------- FOOTER --------------------
st.markdown("""
<hr style='margin-top:50px;'>
<center>
    <small>© 2025 Oluyale Ezekiel — NLP & Machine Learning Portfolio</small>
</center>
""", unsafe_allow_html=True)
