# app.py
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Oluyale Ezekiel | NLP & ML Portfolio",
    page_icon="🤖",
    layout="wide"
)

# ---------- LOAD ANIMATIONS ----------
def load_lottie(url):
    try:
        r = requests.get(url, timeout=6)
        if r.status_code == 200:
            return r.json()
    except Exception:
        return None
    return None

nlp_anim = load_lottie("https://assets9.lottiefiles.com/packages/lf20_jtbfg2nb.json")
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
    background-color: #0055cc !important;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* make the thin left column look like a sidebar when visible */
.left-sidebar {
  padding: 12px 14px;
  background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(255,255,255,0.95));
  border-right: 1px solid rgba(0,0,0,0.04);
  height: 100%;
}

/* hamburger button style (small) */
.hamburger-btn > button {
  background: transparent !important;
  color: #003366 !important;
  border: none !important;
  font-size: 26px !important;
  padding: 4px 8px !important;
}
.hamburger-btn > button:hover {
  color: #0055cc !important;
  transform: translateY(-1px);
}
</style>
""", unsafe_allow_html=True)

# --------- session state for toggle ----------
if "show_sidebar" not in st.session_state:
    st.session_state.show_sidebar = True

def toggle_sidebar():
    st.session_state.show_sidebar = not st.session_state.show_sidebar

# ---------- TOP BAR (hamburger) ----------
top_cols = st.columns([0.04, 0.96])
with top_cols[0]:
    # small hamburger button (keeps it visible top-left)
    if st.button("☰", key="hamburger_toggle"):
        toggle_sidebar()

with top_cols[1]:
    # placeholder so top layout doesn't shift
    st.markdown("")

# ---------- MAIN LAYOUT ----------
# if sidebar visible, give first column ~22% width, otherwise small
if st.session_state.show_sidebar:
    layout_cols = st.columns([0.22, 0.78])
else:
    layout_cols = st.columns([0.03, 0.97])

left_col = layout_cols[0]
main_col = layout_cols[1]

# ---------- SIDEBAR CONTENT (render inside left_col) ----------
with left_col:
    if st.session_state.show_sidebar:
        st.markdown('<div class="left-sidebar">', unsafe_allow_html=True)
        st.image("https://i.imgur.com/8Km9tLL.png", width=140)
        st.title("Oluyale Ezekiel")
        st.markdown("**NLP & ML Enthusiast** 🤖")
        st.markdown("---")

        pages = [
            "About Me",
            "Projects",
            "Skills",
            "Experience",
            "Contact"
        ]
        # Use a radio inside the left column to mirror previous behavior
        selected = st.radio("Navigate", pages, index=0)

        st.markdown("---")
        st.markdown("📧 [oluyale.ezekiel@example.com](mailto:oluyale.ezekiel@example.com)")
        st.markdown("🔗 [LinkedIn](https://linkedin.com/in/oluyaleezekiel)")
        st.markdown("🐙 [GitHub](https://github.com/amusEcode)")

        cv_path = "Ezekiel_Oluyale_Resume.pdf"
        if os.path.exists(cv_path):
            with open(cv_path, "rb") as pdf_file:
                st.download_button(
                    label="📄 Download CV",
                    data=pdf_file.read(),
                    file_name="Ezekiel_Oluyale_Resume.pdf",
                    mime="application/pdf",
                )
        else:
            st.warning("⚠️ CV not found. Upload it later.")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # keep this column empty when hidden (so layout balances)
        st.write("")

# ---------- PAGE CONTENT (render inside main_col) ----------
with main_col:
    # make sure `selected` exists even if sidebar hidden (default to About Me)
    try:
        selected
    except NameError:
        selected = "About Me"

    # ABOUT ME PAGE
    if selected == "About Me":
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://i.imgur.com/4ZQZ9l5.png", width=230)  # placeholder image
        with col2:
            st.title("👋 Hi, I'm Oluyale Ezekiel")
            st.subheader("Machine Learning & NLP Enthusiast")
            st.write(
                """
                I'm a passionate developer focused on building **intelligent NLP applications** that make human–language interaction
                smarter and more accessible.  
                
                My journey began with curiosity about how machines understand text — and over time, I’ve worked on projects like 
                **Text Summarization**, **Question Answering**, **Named Entity Recognition**, and **Sentiment Analysis**.
                
                I enjoy turning raw data into real insights, and I’m currently expanding into **multilingual NLP** and 
                **transformer-based systems**.
                """
            )
        st.markdown("---")
        if nlp_anim:
            st_lottie(nlp_anim, height=250, key="nlp")
        else:
            st.info("NLP animation failed to load — replace the Lottie URL if needed.")

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
            <form action="https://formsubmit.co/oluyale.ezekiel@example.com" method="POST">
                <input type="text" name="name" placeholder="Your Name" required><br><br>
                <input type="email" name="email" placeholder="Your Email" required><br><br>
                <textarea name="message" placeholder="Your Message" required></textarea><br><br>
                <button type="submit">Send Message</button>
            </form>
            """, unsafe_allow_html=True)
        st.markdown("---")
        st.write("📞 **Phone:** +234 812 345 6789")
        st.write("🔗 **LinkedIn:** [linkedin.com/in/oluyaleezekiel](https://linkedin.com/in/oluyaleezekiel)")
        st.write("🐙 **GitHub:** [github.com/amusEcode](https://github.com/amusEcode)")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#666;'>© 2025 Oluyale Ezekiel | Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
