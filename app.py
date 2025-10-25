# app.py
import streamlit as st
from streamlit_lottie import st_lottie
import requests

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="Oluyale Ezekiel | NLP & ML Portfolio",
    page_icon="🤖",
    layout="wide",
)

# -------------------- SESSION STATE --------------------
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

# Ensure a page query param exists
if "page" not in st.query_params:
    st.query_params["page"] = "Home"

# -------------------- LOTTIE LOADER --------------------
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.json()
    except Exception:
        return None
    return None

lottie_home = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_yd8fbnml.json")
lottie_skills = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tfb3estd.json")
lottie_projects = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_experience = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ydo1amjm.json")
lottie_contact = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")

# -------------------- CSS --------------------
st.markdown(
    """
    <style>
    /* NAVBAR */
    .navbar {
        background: #004aad;
        color: white;
        padding: 12px 20px;
        border-radius: 0 0 12px 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .nav-title {
        font-weight: 700;
        font-size: 20px;
    }
    .hambutton {
        background: none;
        border: none;
        color: white;
        font-size: 24px;
        cursor: pointer;
        padding: 6px 10px;
        border-radius: 8px;
    }
    .hambutton:hover { background: rgba(255,255,255,0.06); }

    /* Menu - by default hidden on small screens (we control visibility inline via style attr) */
    .menu {
        display: flex;
        gap: 14px;
        padding: 10px 18px;
        background: #004aad;
        color: white;
        border-radius: 0 0 12px 12px;
        flex-wrap: wrap;
    }
    .menu button {
        background: none;
        border: none;
        color: white;
        font-size: 15px;
        cursor: pointer;
        padding: 8px 12px;
        border-radius: 8px;
    }
    .menu button:hover { background: rgba(255,255,255,0.06); }

    /* active style for current page */
    .menu .active {
        color: #bfe6ff;
        font-weight: 700;
    }

    /* On wide screens always show the menu as a horizontal row */
    @media (min-width: 900px) {
        .menu { display: flex !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- NAVBAR (pure Streamlit controls) --------------------
col1, col2 = st.columns([8, 1])
with col1:
    st.markdown("<div class='navbar'><div class='nav-title'>Oluyale Ezekiel</div></div>", unsafe_allow_html=True)
with col2:
    # This button toggles the menu on small screens
    if st.button("☰", key="hamburger"):
        st.session_state.menu_open = not st.session_state.menu_open

# Decide menu inline style: visible if menu_open or wide screens (CSS will force visible on wide)
menu_style = "display:flex;" if st.session_state.menu_open else "display:none;"

# Render the menu div; CSS media query makes it visible automatically on wide screens
st.markdown(f"<div class='menu' style='{menu_style}'>", unsafe_allow_html=True)

# Navigation buttons (using st.button so clicks trigger a rerun and we react in Python)
def nav_to(p):
    st.query_params["page"] = p
    # close menu on small screens for better UX
    st.session_state.menu_open = False

current_page = st.query_params.get("page", "Home")

# We use st.columns to layout the buttons inside the menu area nicely
# But for simplicity here we render them one by one
if st.button("🏠 Home", key="nav_home"):
    nav_to("Home")
if st.button("🧠 Skills", key="nav_skills"):
    nav_to("Skills")
if st.button("🚀 Projects", key="nav_projects"):
    nav_to("Projects")
if st.button("📚 Experience", key="nav_experience"):
    nav_to("Experience")
if st.button("📞 Contact", key="nav_contact"):
    nav_to("Contact")

st.markdown("</div>", unsafe_allow_html=True)

# After rendering menu and possible clicks, read the current page and render content
page = st.query_params.get("page", "Home")

# -------------------- PAGES --------------------
if page == "Home":
    col1, col2 = st.columns([1, 1])
    with col1:
        try:
            st.image("assets/profile.png", width=300)
        except Exception:
            st.warning("Add your profile image at assets/profile.png")
    with col2:
        st.title("👋 Hi, I'm Oluyale Ezekiel")
        st.subheader("NLP & Machine Learning Engineer")
        st.write(
            "I build intelligent systems that process and understand human language. "
            "My work spans Text Summarization, Sentiment Analysis, NER, and transformer fine-tuning."
        )
        if lottie_home:
            st_lottie(lottie_home, height=260)
    st.divider()
    c1, c2 = st.columns(2)
    c1.metric("Projects", "5+")
    c2.metric("Focus", "NLP & ML")

elif page == "Skills":
    st.header("🧠 Skills")
    if lottie_skills:
        st_lottie(lottie_skills, height=220)
    st.subheader("Languages & Libraries")
    st.write("- Python\n- NumPy, Pandas\n- scikit-learn\n- Transformers (Hugging Face)\n- spaCy, NLTK")
    st.subheader("Tools")
    st.write("- Streamlit, Git, Hugging Face Hub, Jupyter")

elif page == "Projects":
    st.header("🚀 Projects")
    if lottie_projects:
        st_lottie(lottie_projects, height=200)
    st.subheader("Yorùbá Sentiment Analyzer")
    st.write("Classifies Yorùbá tweets as Positive / Negative / Neutral using transformer models.")
    st.divider()
    st.subheader("Abstractive Text Summarizer")
    st.write("Fine-tuned transformer-based abstractive summarizer.")
    st.divider()
    st.subheader("Topic Modeling Dashboard")
    st.write("Interactive LDA & NMF topic modeling exploration.")

elif page == "Experience":
    st.header("📚 Experience & Education")
    if lottie_experience:
        st_lottie(lottie_experience, height=200)
    st.write("🏢 Elevvo Pathways — NLP Intern (Jun 2025 - Oct 2025)")
    st.write("🎓 Federal University of Oye-Ekiti — B.Eng")
    st.write("Research interests: low-resource language NLP, model efficiency, explainability.")

elif page == "Contact":
    st.header("📞 Contact")
    if lottie_contact:
        st_lottie(lottie_contact, height=200)
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Send"):
            if name and email and message:
                st.success("Message received (demo).")
            else:
                st.warning("Please fill all fields.")

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("<div style='text-align:center;color:#6b859e;'>Built with Streamlit • Blue & White theme</div>", unsafe_allow_html=True)
