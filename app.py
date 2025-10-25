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

# -------------------- SESSION STATE --------------------
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

# -------------------- HELPER FUNCTION --------------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -------------------- LOAD ANIMATIONS --------------------
lottie_home = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_yd8fbnml.json")
lottie_skills = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tfb3estd.json")
lottie_projects = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_experience = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ydo1amjm.json")
lottie_contact = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")

# -------------------- NAVBAR STYLING --------------------
st.markdown("""
    <style>
        .navbar {
            background-color: #004aad;
            padding: 10px 25px;
            border-radius: 0 0 12px 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .navbar-title {
            color: white;
            font-size: 20px;
            font-weight: 600;
        }
        .hamburger {
            color: white;
            background: none;
            border: none;
            font-size: 25px;
            cursor: pointer;
        }
        .menu {
            background-color: #004aad;
            display: flex;
            flex-direction: column;
            margin-top: 5px;
            border-radius: 0 0 12px 12px;
        }
        .menu button {
            background: none;
            border: none;
            color: white;
            text-align: left;
            padding: 10px 25px;
            font-size: 16px;
            cursor: pointer;
        }
        .menu button:hover {
            background-color: #0056d1;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- NAVBAR --------------------
col1, col2 = st.columns([5, 1])
with col1:
    st.markdown("<div class='navbar-title'>Oluyale Ezekiel</div>", unsafe_allow_html=True)
with col2:
    if st.button("☰", key="menu_btn", help="Toggle menu", use_container_width=True):
        st.session_state.menu_open = not st.session_state.menu_open

# -------------------- MENU --------------------
if st.session_state.menu_open:
    st.markdown("<div class='menu'>", unsafe_allow_html=True)
    if st.button("🏠 Home"):
        st.query_params["page"] = "Home"
        st.session_state.menu_open = False
    if st.button("🧠 Skills"):
        st.query_params["page"] = "Skills"
        st.session_state.menu_open = False
    if st.button("🚀 Projects"):
        st.query_params["page"] = "Projects"
        st.session_state.menu_open = False
    if st.button("📚 Experience"):
        st.query_params["page"] = "Experience"
        st.session_state.menu_open = False
    if st.button("📞 Contact"):
        st.query_params["page"] = "Contact"
        st.session_state.menu_open = False
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------- GET ACTIVE PAGE --------------------
if "page" not in st.query_params:
    st.query_params["page"] = "Home"
page = st.query_params["page"]

# -------------------- HOME PAGE --------------------
if page == "Home":
    col1, col2 = st.columns([1, 1])
    with col1:
        try:
            st.image("profile.jpg", width=300)
        except:
            st.warning("⚠️ Add your photo in `profile.jpg`.")
    with col2:
        st.title("👋 Hi, I'm Oluyale Ezekiel")
        st.subheader("NLP & Machine Learning Engineer")
        st.write("""
        I build intelligent systems that process and understand human language.  
        My focus areas are **Natural Language Processing** and **Machine Learning** — from Sentiment Analysis to Text Summarization.
        """)
        if lottie_home:
            st_lottie(lottie_home, height=250)
    st.divider()
    col1, col2 = st.columns(2)
    col1.metric("Projects", "5+")
    col2.metric("Specialization", "NLP & ML")

# -------------------- SKILLS PAGE --------------------
elif page == "Skills":
    st.header("🧠 Skills")
    if lottie_skills:
        st_lottie(lottie_skills, height=200)
    st.write("### Languages")
    st.text("Python (Advanced)")
    st.write("### Frameworks & Libraries")
    st.text("Transformers · PyTorch · scikit-learn · NumPy · Pandas")
    st.write("### Tools & Platforms")
    st.text("Streamlit · Hugging Face · Git · Jupyter")

# -------------------- PROJECTS PAGE --------------------
elif page == "Projects":
    st.header("🚀 Projects")
    if lottie_projects:
        st_lottie(lottie_projects, height=200)
    projects = [
        {
            "title": "Yorùbá Sentiment Analyzer",
            "desc": "Classifies Yorùbá tweets as positive, negative, or neutral using transformer models.",
            "tech": "Python · BERT · NLP",
        },
        {
            "title": "Text Summarizer",
            "desc": "Abstractive summarization using transformer models fine-tuned on news datasets.",
            "tech": "Python · Hugging Face · Streamlit",
        },
        {
            "title": "Topic Modeling",
            "desc": "Discovers hidden themes in documents using LDA and NMF.",
            "tech": "Python · scikit-learn · NLP",
        },
    ]
    for p in projects:
        st.subheader(p["title"])
        st.write(p["desc"])
        st.write(f"**Tech Stack:** {p['tech']}")
        st.divider()

# -------------------- EXPERIENCE PAGE --------------------
elif page == "Experience":
    st.header("📚 Experience & Education")
    if lottie_experience:
        st_lottie(lottie_experience, height=200)
    st.write("### 🏢 Elevvo Pathways — NLP Intern")
    st.write("""
    Worked on Named Entity Recognition, Topic Modeling, and Summarization projects  
    using transformer-based models and preprocessing pipelines.
    """)
    st.write("### 🎓 Federal University of Oye-Ekiti")
    st.write("Bachelor of Engineering (B.Eng) in Computer Engineering")
    st.write("### 🎯 Research Interests")
    st.write("Multilingual NLP, Transformer optimization, Applied ML.")

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
