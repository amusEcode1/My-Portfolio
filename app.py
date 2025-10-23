import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ----- Page Config -----
st.set_page_config(page_title="Oluyale Ezekiel | NLP & ML Portfolio", layout="wide")

# ----- Load Lottie Animation -----
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# NLP/ML-themed Lottie animation
nlp_lottie = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_kyu7xb1v.json")

# ----- Sidebar -----
with st.sidebar:
    st.image("https://i.imgur.com/qG2H6rD.png", width=150)
    st.title("Oluyale Ezekiel")
    st.markdown("**Machine Learning & NLP Engineer**")
    st.markdown("---")

    selected = st.radio(
        "Navigate",
        ["About Me", "Projects", "Skills", "Experience", "Contact"],
        index=0
    )

# ----- Custom CSS -----
st.markdown("""
    <style>
        /* Sidebar style */
        [data-testid="stSidebar"] {
            background-color: #f8fbff;
            color: #004aad;
        }
        /* Radio button hover and active styles */
        div[role="radiogroup"] > label:hover {
            background-color: #dce9ff;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        div[role="radiogroup"] > label {
            padding: 5px 10px;
        }
        div[role="radiogroup"] > label[data-checked="true"] {
            background-color: #004aad;
            color: white !important;
            border-radius: 8px;
        }
        /* Button hover effect */
        div.stButton > button:hover {
            background-color: #0066cc;
            color: white;
            transition: 0.3s ease;
        }
        /* Global layout tweaks */
        h1, h2, h3 {
            color: #004aad;
        }
    </style>
""", unsafe_allow_html=True)

# ----- About Me -----
if selected == "About Me":
    left, right = st.columns([1, 1.2])
    with left:
        st.header("👋 About Me")
        st.write("""
        I'm **Oluyale Ezekiel**, a passionate **Machine Learning and NLP Engineer** 
        focused on building intelligent systems that understand and process human language.  
        I enjoy transforming text data into actionable insights through deep learning and 
        transformer-based models.

        My interests span **text summarization**, **sentiment analysis**, 
        **question answering**, and **multilingual NLP**.
        """)
        st.markdown("📍 Based in Nigeria | 🌐 Open to remote collaborations")
    with right:
        if nlp_lottie:
            st_lottie(nlp_lottie, height=300, key="about")

# ----- Projects -----
elif selected == "Projects":
    st.header("🧠 My Projects")
    st.markdown("Here are some of the projects I’ve worked on — each focused on real-world NLP & ML problems.")

    cols = st.columns(2)
    with cols[0]:
        st.subheader("1️⃣ Sentiment Analysis on Tweets")
        st.write("Built a model to classify text as positive, negative, or neutral using SVM and BERT.")
        st.image("https://i.imgur.com/dR9zGJx.png", use_container_width=True)

    with cols[1]:
        st.subheader("2️⃣ Question Answering System")
        st.write("Developed a QA system that answers questions based on a given passage using fine-tuned transformer models.")
        st.image("https://i.imgur.com/RC7nJ2y.png", use_container_width=True)

    st.markdown("*(More projects coming soon...)*")

# ----- Skills -----
elif selected == "Skills":
    st.header("🧩 Technical Skills")
    st.markdown("""
    ### 🧠 Machine Learning
    - Scikit-learn, TensorFlow, PyTorch  
    - Model Evaluation & Hyperparameter Tuning  

    ### 💬 Natural Language Processing
    - spaCy, Hugging Face Transformers  
    - Text Preprocessing, Named Entity Recognition (NER)  
    - Sentiment Analysis, Topic Modeling, Summarization  

    ### 💻 Programming & Tools
    - Python, Streamlit, Git, GitHub  
    - VS Code, Jupyter Notebook  
    """)

# ----- Experience -----
elif selected == "Experience":
    st.header("💼 Experience")
    st.subheader("Elevvo Pathways — NLP Intern")
    st.write("""
    - Gained hands-on experience applying NLP concepts to real-world datasets.  
    - Built and deployed projects including **NER**, **Sentiment Analysis**, **Topic Modeling**, and **Text Summarization**.  
    - Learned how to preprocess text, fine-tune transformer models, and evaluate performance.  
    - Worked in a collaborative, remote-based environment with mentorship.
    """)

# ----- Contact -----
elif selected == "Contact":
    st.header("📬 Contact Me")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success(f"Thank you, {name}! Your message has been sent successfully.")

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
