# app.py
import streamlit as st
from streamlit_lottie import st_lottie
import requests

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Oluyale Ezekiel | NLP & ML Portfolio",
                   page_icon="🤖",
                   layout="wide")

# -------------------- LOAD LOTTIE ANIMATION --------------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Example Lottie URLs (you can replace these with others)
lottie_home = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_yd8fbnml.json")
lottie_skills = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tfb3estd.json")
lottie_projects = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_experience = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ydo1amjm.json")
lottie_contact = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")

# -------------------- NAVBAR STYLE --------------------
st.markdown("""
    <style>
        /* NAVBAR */
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

# -------------------- NAVBAR --------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# JS to toggle menu visibility
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

st.markdown("""
<div class="topnav">
    <span class="hamburger" onclick="toggleMenu()">☰</span>
    <a style="font-size:18px;font-weight:600;">Oluyale Ezekiel</a>
</div>
<div class="menu">
    <a href="#" onclick="window.parent.postMessage({type:'streamlit:setPage', page:'Home'}, '*')">🏠 Home</a>
    <a href="#" onclick="window.parent.postMessage({type:'streamlit:setPage', page:'Skills'}, '*')">🧠 Skills</a>
    <a href="#" onclick="window.parent.postMessage({type:'streamlit:setPage', page:'Projects'}, '*')">🚀 Projects</a>
    <a href="#" onclick="window.parent.postMessage({type:'streamlit:setPage', page:'Experience'}, '*')">📚 Experience</a>
    <a href="#" onclick="window.parent.postMessage({type:'streamlit:setPage', page:'Contact'}, '*')">📞 Contact</a>
</div>
""", unsafe_allow_html=True)

# -------------------- HELPER: set/get query param safely --------------------
def set_page_queryparam(page_name: str):
    """Set the 'page' query parameter in the URL."""
    st.set_query_params(page=page_name)

def get_page_from_queryparam() -> str:
    """Read the 'page' query param using the new API. Defaults to 'Home'."""
    params = st.query_params  # new read-only mapping
    page = params.get("page", ["Home"])[0] if params else "Home"
    return page

# If the app was opened without query param, ensure URL shows Home
if not st.query_params:
    set_page_queryparam("Home")

# -------------------- HANDLE POSTMESSAGE FROM NAVBAR (browser -> streamlit) --------------------
# This snippet listens for the window.postMessage from the custom navbar and updates query params.
st.markdown(
    """
<script>
window.addEventListener("message", (event) => {
    try {
        const data = event.data;
        if (data && data.type === "streamlit:setPage") {
            const page = data.page || "Home";
            // update the URL query param without reloading:
            const url = new URL(window.location);
            url.searchParams.set('page', page);
            window.history.pushState({}, '', url);
            // Also send a message back so Streamlit can detect the change (fallback)
            window.parent.postMessage({type:'streamlit:pageChanged'}, '*');
        }
    } catch(e) { /* ignore */ }
});
</script>
""",
    unsafe_allow_html=True,
)

# Small JS-based workaround to notify Streamlit to re-run after URL change
# (Streamlit detects query params automatically on reload; this helps in some embeds)
st.experimental_rerun() if False else None  # no-op placeholder

# -------------------- SIMPLE PAGE ROUTING --------------------
# Read page from query params and set session_state accordingly
page = get_page_from_queryparam()
st.session_state.page = page

# -------------------- HOME PAGE --------------------
if st.session_state.page == "Home":
    col1, col2 = st.columns([1, 1])
    with col1:
        try:
            st.image("profile.jpg", width=300)
        except Exception:
            st.write("Add your profile image to assets/profile.png")
    with col2:
        st.title("👋 Hi, I'm Oluyale Ezekiel")
        st.subheader("NLP & Machine Learning Engineer")
        st.write("Building intelligent systems that understand and process human language. "
                 "I specialize in Natural Language Processing and Machine Learning applications, "
                 "from text summarization to sentiment analysis.")
        if lottie_home:
            st_lottie(lottie_home, height=250, key="home")
        st.markdown("""
        <br>
        <a href="https://github.com/yourgithub" target="_blank">🔗 GitHub</a> |
        <a href="https://linkedin.com/in/yourlinkedin" target="_blank">💼 LinkedIn</a> |
        <a href="Ezekiel_Oluyale_Resume.pdf" target="_blank">📄 Resume</a>
        """, unsafe_allow_html=True)
    st.divider()
    cols = st.columns(2)
    cols[0].metric("Projects", "5+")
    cols[1].metric("Specialization", "NLP & ML")

# -------------------- SKILLS PAGE --------------------
elif st.session_state.page == "Skills":
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
elif st.session_state.page == "Projects":
    st.header("🚀 Projects")
    if lottie_projects:
        st_lottie(lottie_projects, height=200)
    project_data = [
        {"title": "Yorùbá Sentiment Analyzer",
         "desc": "Classifies Yorùbá tweets as positive, negative, or neutral using transformer-based models.",
         "tech": "Python · BERT · NLP",
         "github": "https://github.com/yourgithub"},
        {"title": "Text Summarizer",
         "desc": "Abstractive summarization using transformer models fine-tuned on news datasets.",
         "tech": "Python · Hugging Face · Streamlit",
         "github": "https://github.com/yourgithub"},
        {"title": "Topic Modeling",
         "desc": "Automatically discovers hidden themes in documents using LDA and NMF.",
         "tech": "Python · scikit-learn · NLP",
         "github": "https://github.com/yourgithub"}
    ]
    for p in project_data:
        st.subheader(p["title"])
        st.write(p["desc"])
        st.write(f"**Tech Stack:** {p['tech']}")
        st.markdown(f"[🔗 View Code]({p['github']})")
        st.divider()

# -------------------- EXPERIENCE PAGE --------------------
elif st.session_state.page == "Experience":
    st.header("📚 Experience & Education")
    if lottie_experience:
        st_lottie(lottie_experience, height=200)
    st.write("### 🏢 Elevvo Pathways — NLP Intern")
    st.write("Worked on Named Entity Recognition, Topic Modeling, and Text Summarization systems.")
    st.write("### 🎓 Federal University of Oye-Ekiti")
    st.write("Bachelor of Engineering (B.Eng) in Computer Engineering")
    st.write("### 🎯 Research Interest")
    st.write("Multilingual NLP, Transformer optimization, and applied ML.")

# -------------------- CONTACT PAGE --------------------
elif st.session_state.page == "Contact":
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
                st.warning("Please fill all fields.")

# -------------------- FOOTER --------------------
st.markdown("""
<hr style='margin-top:50px;'>
<center>
    <small>© 2025 Oluyale Ezekiel — NLP & Machine Learning Portfolio</small>
</center>
""", unsafe_allow_html=True)
