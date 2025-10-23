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

# -------------------- THEME COLORS --------------------
PRIMARY = "#004aad"   # main blue
HOVER = "#0066cc"     # hover blue (softer)
ACCENT = "#cfe8ff"    # light blue accents
BG = "#f7faff"        # page background

# -------------------- HELPERS --------------------
def load_lottie(url: str):
    """Load a Lottie animation from a URL (returns parsed json or None)."""
    try:
        r = requests.get(url, timeout=6)
        if r.status_code == 200:
            return r.json()
    except Exception:
        return None
    return None

# NLP/ML Lottie (placeholder — feel free to replace with another Lottie JSON URL)
nlp_lottie_url = "https://assets9.lottiefiles.com/packages/lf20_jtbfg2nb.json"
nlp_anim = load_lottie(nlp_lottie_url)

contact_lottie_url = "https://assets9.lottiefiles.com/packages/lf20_t24tpvcu.json"
contact_anim = load_lottie(contact_lottie_url)

# -------------------- STYLES (CSS) --------------------
st.markdown(
    f"""
<style>
:root {{
  --primary: {PRIMARY};
  --hover: {HOVER};
  --accent: {ACCENT};
  --bg: {BG};
}}

html, body, [class*="stApp"], .main {{
  background-color: var(--bg);
}}

/* Headings */
h1, h2, h3, h4 {{
  color: var(--primary);
}}

/* Make placeholder profile image circular */
.profile-img {{
  border-radius: 50%;
  border: 5px solid rgba(0,0,0,0.04);
}}

/* Buttons */
.stButton>button, .st-download-button>button {{
  background-color: var(--primary) !important;
  color: white !important;
  border-radius: 10px !important;
  padding: 8px 14px !important;
  transition: background-color 0.18s ease, transform 0.08s ease;
}}
.stButton>button:hover, .st-download-button>button:hover {{
  background-color: var(--hover) !important;
  transform: translateY(-2px);
}}

/* Sidebar container look */
[data-testid="stSidebar"] {{
  background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(255,255,255,0.95));
  border-right: 1px solid rgba(0,0,0,0.04);
  padding-top: 16px;
}}

/* Radio / sidebar items styling: make them blue and nicer */
[data-testid="stSidebar"] input[type="radio"] {{
  accent-color: var(--primary); /* modern browsers */
}}
/* Label hover effect in sidebar */
[data-testid="stSidebar"] label {{
  display: block;
  padding: 8px 10px;
  border-radius: 8px;
  transition: background-color 0.15s ease, color 0.15s ease, transform 0.06s ease;
  cursor: pointer;
  color: #0b2540;
}}
[data-testid="stSidebar"] label:hover {{
  background-color: rgba(0, 74, 173, 0.06);
  color: var(--primary);
  transform: translateX(4px);
}}
/* Active/checked label */
[data-testid="stSidebar"] input[type="radio"]:checked + label {{
  background-color: rgba(0, 74, 173, 0.10);
  color: var(--primary);
  font-weight: 600;
  box-shadow: 0 4px 18px rgba(0, 74, 173, 0.08);
}}

/* Project card look */
.project-card {{
  background: white;
  border-radius: 12px;
  padding: 16px;
  border: 1px solid rgba(0,0,0,0.04);
  transition: box-shadow 0.12s ease, transform 0.08s ease;
}}
.project-card:hover {{
  box-shadow: 0 10px 30px rgba(0,0,0,0.06);
  transform: translateY(-4px);
}}
.skill-badge {{
  display:inline-block;
  padding:6px 10px;
  margin:4px 6px 4px 0;
  border-radius:999px;
  background-color: var(--accent);
  color: var(--primary);
  font-weight:600;
  font-size: 13px;
}}

.timeline-entry {{
  padding: 12px 14px;
  border-left: 4px solid var(--primary);
  background: white;
  border-radius: 8px;
  margin-bottom: 14px;
}}
</style>
""",
    unsafe_allow_html=True,
)

# -------------------- SIDEBAR --------------------
st.sidebar.image("https://i.imgur.com/4ZQZ9l5.png", width=140, caption="(placeholder image)", use_column_width=False)
st.sidebar.title("Oluyale Ezekiel")
st.sidebar.markdown("**NLP & ML Enthusiast** 🤖")
st.sidebar.markdown("---")

# skill filter (interactive)
all_skills = ["Transformers", "NLP", "Summarization", "QA", "NER", "Topic Modeling", "Sentiment"]
# selected skill filter - acts as a simple project filter
st.sidebar.markdown("### 🔎 Filter projects by skill")
skill_filter = st.sidebar.selectbox("Skill (Optional)", options=["All"] + all_skills, index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("📧 [oluyale.ezekiel@example.com](mailto:oluyale.ezekiel@example.com)")
st.sidebar.markdown("📞 +234 812 345 6789")
st.sidebar.markdown("🔗 [LinkedIn](https://linkedin.com/in/oluyaleezekiel)")
st.sidebar.markdown("🐙 [GitHub](https://github.com/amusEcode)")

# safe CV download
cv_path = "Ezekiel_Oluyale_Resume.pdf"
if os.path.exists(cv_path):
    with open(cv_path, "rb") as f:
        st.sidebar.download_button("📄 Download CV", f.read(), file_name="Ezekiel_Oluyale_Resume.pdf", mime="application/pdf")
else:
    st.sidebar.info("CV not found in folder. Add `Ezekiel_Oluyale_Resume.pdf` to enable download.")

st.sidebar.markdown("---")

# navigation using Streamlit radio (keeps default hamburger icon)
pages = ["About", "Projects", "Skills", "Experience", "Contact"]
page = st.sidebar.radio("Navigate", pages, index=0)

# -------------------- PAGE CONTENT --------------------
# ABOUT
if page == "About":
    col_left, col_right = st.columns([1, 2], gap="medium")
    with col_left:
        # circular image (placeholder)
        st.markdown('<img class="profile-img" src="https://i.imgur.com/4ZQZ9l5.png" width="200"/>', unsafe_allow_html=True)
        st.write("")
        st.markdown("**Location:** Nigeria")
        st.markdown("**Open to:** Remote Roles / MSc Supervision")
        st.write("")
        # contact mini buttons
        c1, c2 = st.columns([1, 1])
        with c1:
            st.markdown("[💼 GitHub](https://github.com/amusEcode)")
        with c2:
            st.markdown("[🔗 LinkedIn](https://linkedin.com/in/oluyaleezekiel)")

    with col_right:
        st.title("Hi — I'm Oluyale Ezekiel")
        st.subheader("Machine Learning & NLP Enthusiast")
        st.write(
            """
            I build NLP systems that convert messy text into actionable insights.
            My work spans text summarization, question-answering, named entity recognition,
            and sentiment analysis. I enjoy crafting models that solve real user problems —
            especially in multilingual settings.
            """
        )
        st.markdown("**Short stories (micro):**")
        st.markdown(
            "- 🎓 *From learning tokenization to fine-tuning transformers, I love turning research into products.*\n"
            "- 🛠 *I deliver end-to-end projects — from data cleaning and model training to deployment and UX.*\n"
            "- 🌍 *I’m passionate about making NLP accessible across languages.*"
        )

    st.markdown("---")
    # nice Lottie about NLP/ML
    if nlp_anim:
        st_lottie(nlp_anim, height=320)
    else:
        st.info("NLP animation failed to load — replace the Lottie URL if needed.")

# PROJECTS
elif page == "Projects":
    st.header("🚀 Projects — interactive showcase")
    st.write("Click an item to expand. Use the skill filter in the sidebar to narrow projects.")

    # sample project data (you have 8 at Elevvo — replace entries as needed)
    projects = [
        {
            "title": "Abstractive Text Summarizer",
            "summary": "Fine-tuned a transformer to generate concise summaries for long text.",
            "skills": ["Transformers", "Summarization", "NLP"],
            "repo": "https://github.com/amusEcode/summarizer_model"
        },
        {
            "title": "Question Answering System",
            "summary": "A BERT-based QA system fine-tuned on SQuAD-style datasets to answer contextual questions.",
            "skills": ["Transformers", "QA", "NLP"],
            "repo": "https://github.com/amusEcode/qa_system"
        },
        {
            "title": "Named Entity Recognition (NER)",
            "summary": "Hybrid SpaCy + rule-based NER for domain-specific entity extraction.",
            "skills": ["NER", "NLP"],
            "repo": "https://github.com/amusEcode/ner_project"
        },
        {
            "title": "Yorùbá Sentiment Classifier",
            "summary": "Built a sentiment classifier for Yorùbá tweets using SVM and transformers ensembles.",
            "skills": ["NLP", "Sentiment", "Transformers"],
            "repo": "https://github.com/amusEcode/yoruba_sentiment"
        },
        {
            "title": "Topic Modeling Dashboard",
            "summary": "Interactive topic modeling with LDA & NMF; visualized top terms and document assignments.",
            "skills": ["Topic Modeling", "NLP"],
            "repo": "#"
        },
    ]

    # filter projects by sidebar selection
    filtered = []
    for p in projects:
        if skill_filter == "All" or skill_filter in p["skills"]:
            filtered.append(p)

    # layout projects in two columns, with nice card style and expander for details
    cols = st.columns(2, gap="large")
    for i, proj in enumerate(filtered):
        col = cols[i % 2]
        with col:
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.subheader(proj["title"])
            st.write(proj["summary"])
            # skill badges
            skill_html = "".join([f'<span class="skill-badge">{s}</span>' for s in proj["skills"]])
            st.markdown(skill_html, unsafe_allow_html=True)
            # action buttons
            b1, b2 = st.columns([1, 1])
            with b1:
                if st.button(f"View Repo ▶ {i}", key=f"repo_{i}"):
                    st.experimental_set_query_params(view=proj["title"].replace(" ", "_"))
                    st.write(f"[Repository]({proj['repo']})")
            with b2:
                with st.expander("Details & Notes"):
                    st.write("Detailed description, model choices, dataset info, evaluation metrics, and demo link go here.")
            st.markdown("</div>", unsafe_allow_html=True)

    if len(filtered) == 0:
        st.info("No projects match this filter. Try selecting 'All' or another skill.")

# SKILLS
elif page == "Skills":
    st.header("🧠 Skills & Tools")
    st.write("Click a skill to see related projects (interactive).")

    # skill cards with simple interactivity
    skill_cols = st.columns(3)
    skill_list = ["Transformers", "SpaCy", "Topic Modeling", "QA", "NER", "Sentiment", "Streamlit", "Hugging Face"]
    for i, skill in enumerate(skill_list):
        c = skill_cols[i % 3]
        with c:
            if st.button(skill, key=f"skill_{i}"):
                # set the sidebar selectbox to reflect filter (use query params as hint)
                # (we can't programmatically change the sidebar selectbox from here easily)
                st.success(f"Try filtering projects by **{skill}** from the left sidebar.")
            st.markdown(f"<div style='height:8px'></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Tooling")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("- Python\n- NumPy\n- Pandas")
    with col2:
        st.markdown("- PyTorch\n- scikit-learn\n- Transformers")
    with col3:
        st.markdown("- SpaCy\n- Hugging Face\n- Streamlit")

# EXPERIENCE
elif page == "Experience":
    st.header("💼 Experience")
    st.write("Timeline of relevant roles & achievements")

    st.markdown('<div class="timeline-entry">', unsafe_allow_html=True)
    st.subheader("NLP Intern — Elevvo Pathways (Remote)")
    st.markdown("**Jan 2025 – Oct 2025**")
    st.write(
        "- Built 8 end-to-end NLP projects including Summarization, QA, NER and Sentiment Analysis.\n"
        "- Responsibilities: data cleaning, model fine-tuning, evaluation, deployment & UX."
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="timeline-entry">', unsafe_allow_html=True)
    st.subheader("Freelance NLP Projects")
    st.markdown("**2024 – Present**")
    st.write("- Prototype NLP tools for content summarization and moderation.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("Tip: Add more experience entries or publications here. This layout scales well for multiple cards.")

# CONTACT
elif page == "Contact":
    st.header("📬 Contact")
    st.write("Shoot me a message — either send an email, download my CV, or use the form below.")

    c1, c2 = st.columns([1, 1])
    with c1:
        if contact_anim:
            st_lottie(contact_anim, height=260)
        else:
            st.write("Contact animation failed to load.")
    with c2:
        # responsive contact form — uses FormSubmit to email; also shows a demo in-app submit
        st.markdown("**Prefer email?** [oluyale.ezekiel@example.com](mailto:oluyale.ezekiel@example.com)")
        st.markdown("**Phone:** +234 812 345 6789")
        st.markdown("---")

        # Streamlit form (local demo)
        with st.form("contact_form"):
            name = st.text_input("Your name")
            email = st.text_input("Your email")
            message = st.text_area("Message", height=150)
            submitted = st.form_submit_button("Send (demo)")
            if submitted:
                st.success("Thanks — this is a demo submit. Replace with FormSubmit or a backend to receive messages.")
        st.markdown("---")
        # HTML form using formsubmit (uncomment / edit email)
        st.markdown(
            """
            <form action="https://formsubmit.co/oluyale.ezekiel@example.com" method="POST" target="_blank">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required style="width:100%;padding:8px;margin-bottom:8px;border-radius:8px;border:1px solid #ddeeff;">
                <input type="email" name="email" placeholder="Your email" required style="width:100%;padding:8px;margin-bottom:8px;border-radius:8px;border:1px solid #ddeeff;">
                <textarea name="message" placeholder="Your message" required style="width:100%;padding:8px;border-radius:8px;border:1px solid #ddeeff;height:120px"></textarea>
                <div style='height:10px'></div>
                <button type="submit" style="background-color:{p};color:#fff;padding:10px 14px;border-radius:10px;border:none;cursor:pointer">Send Message</button>
            </form>
            """.replace("{p}", PRIMARY),
            unsafe_allow_html=True,
        )

# FOOTER
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#566;'>© 2025 Oluyale Ezekiel | Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True,
)
