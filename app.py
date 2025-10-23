import streamlit as st
from streamlit_lottie import st_lottie
import requests

# PAGE CONFIG
st.set_page_config(page_title="Oluyale Ezekiel | NLP & ML Portfolio", page_icon="🤖", layout="wide")

# LOAD ANIMATIONS
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

nlp_anim = load_lottie("https://assets9.lottiefiles.com/packages/lf20_jtbfg2nb.json")
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
a {
    color: #0055cc;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
input, textarea {
    width: 100%;
    border-radius: 10px;
    border: 1px solid #cce0ff;
    padding: 10px;
}
button {
    background-color: #003366 !important;
    color: white !important;
    border-radius: 10px !important;
}
button:hover {
    background-color: #0055cc !important;
}
</style>
""", unsafe_allow_html=True)

# HEADER SECTION
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("👋 Hi, I’m Oluyale Ezekiel")
        st.title("Machine Learning & NLP Enthusiast")
        st.write(
            "I'm passionate about building intelligent NLP applications that make human–language interaction smoother and more accessible. "
            "My focus areas include text classification, summarization, and multilingual NLP."
        )
        st.write("📍 Based in Nigeria | 🌐 Open to Remote Roles")

        # Contact Buttons
        st.markdown("""
        **📧 Email:** [oluyale.ezekiel@example.com](mailto:oluyale.ezekiel@example.com)
        **📞 Phone:** +234 812 345 6789
        **🔗 LinkedIn:** [linkedin.com/in/oluyaleezekiel](https://linkedin.com/in/oluyaleezekiel)
        """)
        cv_path = "Ezekiel_Oluyale_Resume.pdf"
        st.download_button(
            label="📄 Download My CV",
            data=open(cv_path, "rb").read(),
            file_name="Oluyale_Ezekiel_CV.pdf",
            mime="application/pdf",
        )
    with col2:
        st_lottie(nlp_anim, height=250, key="nlp")

# PROJECTS SECTION
st.markdown("---")
st.header("🚀 Featured Projects")

project_data = [
    {
        "title": "Text Summarization App",
        "desc": "Built an abstractive text summarization app using fine-tuned transformer models for concise, meaningful summaries.",
        "tech": "Python, Hugging Face, Streamlit",
        "link": "https://github.com/amusEcode/summarizer_model"
    },
    {
        "title": "Question Answering System",
        "desc": "Developed a QA system that answers questions based on provided context using BERT fine-tuned on SQuAD.",
        "tech": "Python, Transformers, Streamlit",
        "link": "#"
    },
    {
        "title": "Named Entity Recognition (NER)",
        "desc": "Implemented a model that identifies people, organizations, and locations using SpaCy and custom rule-based approaches.",
        "tech": "SpaCy, Python",
        "link": "#"
    }
]

cols = st.columns(3)
for i, proj in enumerate(project_data):
    with cols[i]:
        st.markdown(f"### {proj['title']}")
        st.write(proj['desc'])
        st.caption(f"**Tech Used:** {proj['tech']}")
        st.link_button("🔗 View Project", proj['link'])

# SKILLS SECTION
st.markdown("---")
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

# EXPERIENCE SECTION
st.markdown("---")
st.header("💼 Experience")

st.subheader("NLP Intern — Elevvo Pathways (Remote)")
st.write("""
During my internship, I developed and deployed **8 end-to-end NLP projects** applying text preprocessing, model fine-tuning,
and evaluation. These projects covered NER, summarization, topic modeling, and sentiment analysis — helping me grow into a
hands-on NLP practitioner.
""")
st.caption("Jan 2025 – Oct 2025 | Remote Internship")

# CONTACT SECTION
st.markdown("---")
st.header("📬 Get In Touch")

col1, col2 = st.columns([1, 1])
with col1:
    st_lottie(contact_anim, height=200, key="contact")
with col2:
    st.markdown("""
    <form action="https://formsubmit.co/oluyale.ezekiel@example.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required><br><br>
        <input type="email" name="email" placeholder="Your Email" required><br><br>
        <textarea name="message" placeholder="Your Message" required></textarea><br><br>
        <button type="submit">Send Message</button>
    </form>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#666;'>© 2025 Oluyale Ezekiel | Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
