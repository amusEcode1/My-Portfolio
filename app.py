import streamlit as st
from streamlit_option_menu import streamlit_option_menu
import base64

# Page config
st.set_page_config(
    page_title="Your Name - ML/NLP Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    /* Color scheme - Blue and White */
    :root {
        --primary-blue: #1e3a8a;
        --light-blue: #3b82f6;
        --accent-blue: #60a5fa;
        --white: #ffffff;
        --light-gray: #f8fafc;
    }
    
    /* Hide default streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
    
    /* Hero section */
    .hero-section {
        animation: fadeInUp 1s ease-out;
        padding: 3rem 0;
        text-align: center;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: slideIn 1s ease-out;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #3b82f6;
        margin-bottom: 2rem;
        animation: fadeInUp 1.2s ease-out;
    }
    
    /* Section styling */
    .section-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 2rem;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 0.5rem;
        animation: slideIn 0.8s ease-out;
    }
    
    /* Profile image */
    .profile-img {
        border-radius: 50%;
        border: 5px solid #3b82f6;
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.3);
        animation: pulse 2s infinite;
        max-width: 250px;
        margin: 0 auto;
    }
    
    /* Project cards */
    .project-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #3b82f6;
        margin-bottom: 2rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: fadeInUp 0.6s ease-out;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.2);
    }
    
    /* Buttons */
    .custom-button {
        background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem;
        transition: transform 0.3s ease;
        font-weight: 600;
    }
    
    .custom-button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(59, 130, 246, 0.4);
    }
    
    /* Skill bars */
    .skill-bar {
        background: #e5e7eb;
        border-radius: 10px;
        height: 30px;
        margin: 1rem 0;
        overflow: hidden;
    }
    
    .skill-progress {
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        height: 100%;
        display: flex;
        align-items: center;
        padding-left: 1rem;
        color: white;
        font-weight: 600;
        animation: slideIn 1.5s ease-out;
    }
    
    /* Contact form */
    .contact-form {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Social links */
    .social-links {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin-top: 2rem;
    }
    
    .social-icon {
        font-size: 2rem;
        color: #3b82f6;
        transition: color 0.3s ease, transform 0.3s ease;
    }
    
    .social-icon:hover {
        color: #1e3a8a;
        transform: scale(1.2);
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2rem;
        }
        .hero-subtitle {
            font-size: 1.2rem;
        }
        .section-header {
            font-size: 1.8rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Navigation menu (Hamburger menu for mobile)
selected = streamlit_option_menu(
    menu_title=None,
    options=["Home", "About", "Projects", "Skills", "Contact"],
    icons=["house", "person", "briefcase", "star", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#1e3a8a"},
        "icon": {"color": "white", "font-size": "20px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "color": "white",
            "--hover-color": "#3b82f6",
        },
        "nav-link-selected": {"background-color": "#3b82f6"},
    }
)

# HOME SECTION
if selected == "Home":
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<h1 class="hero-title">👋 Hi, I\'m [Your Name]</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Machine Learning Engineer | NLP Specialist</p>', unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 1.2rem; color: #64748b; animation: fadeInUp 1.4s ease-out;">
        Transforming data into intelligent solutions. Passionate about building cutting-edge ML models 
        and NLP systems that solve real-world problems.
        </p>
        """, unsafe_allow_html=True)
        
        # Social links
        st.markdown("""
        <div class="social-links">
            <a href="https://github.com/yourusername" target="_blank" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
            </a>
            <a href="https://linkedin.com/in/yourusername" target="_blank" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                </svg>
            </a>
            <a href="https://kaggle.com/yourusername" target="_blank" class="social-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M18.825 23.859c-.022.092-.117.141-.281.141h-3.139c-.187 0-.351-.082-.492-.248l-5.178-6.589-1.448 1.374v5.111c0 .235-.117.352-.351.352H5.505c-.236 0-.354-.117-.354-.352V.353c0-.233.118-.353.354-.353h2.431c.234 0 .351.12.351.353v14.343l6.203-6.272c.165-.165.33-.246.495-.246h3.239c.144 0 .236.06.285.18.046.149.034.255-.036.315l-6.555 6.344 6.836 8.507c.095.104.117.208.07.358"/>
                </svg>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # CTA Buttons
        st.markdown("<br>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        with col_btn2:
            st.markdown("""
            <div style="text-align: center;">
                <a href="#projects" class="custom-button">View Projects</a>
                <a href="#contact" class="custom-button">Get In Touch</a>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Animated ML/NLP illustration using Lottie
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
            <lottie-player src="https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json" 
                background="transparent" speed="1" style="width: 500px; height: 500px; margin: 0 auto;" 
                loop autoplay>
            </lottie-player>
        </div>
        """, unsafe_allow_html=True)

# ABOUT SECTION
elif selected == "About":
    st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Profile image placeholder
        st.markdown("""
        <div style="text-align: center; animation: fadeInUp 0.8s ease-out;">
            <img src="https://via.placeholder.com/250" class="profile-img" alt="Profile Picture">
            <p style="margin-top: 1rem; color: #64748b; font-style: italic;">Replace with your photo</p>
        </div>
        """, unsafe_allow_html=True)
        
        # AI animation
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
            <lottie-player src="https://assets9.lottiefiles.com/packages/lf20_5tl1xxnz.json" 
                background="transparent" speed="1" style="width: 200px; height: 200px; margin: 0 auto;" 
                loop autoplay>
            </lottie-player>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="animation: slideIn 1s ease-out;">
            <p style="font-size: 1.1rem; line-height: 1.8; color: #475569;">
            I'm a passionate Machine Learning Engineer specializing in Natural Language Processing with 
            experience in building and deploying intelligent systems. My journey in AI began during my 
            undergraduate studies, where I discovered the fascinating world of teaching machines to understand 
            and generate human language.
            </p>
            
            <p style="font-size: 1.1rem; line-height: 1.8; color: #475569; margin-top: 1.5rem;">
            I thrive on transforming complex data into actionable insights and creating ML solutions that 
            make a real-world impact. From text summarization to topic modeling and sentiment analysis, 
            I've worked on diverse projects that push the boundaries of what's possible with NLP.
            </p>
            
            <p style="font-size: 1.1rem; line-height: 1.8; color: #475569; margin-top: 1.5rem;">
            When I'm not training models or fine-tuning transformers, you'll find me exploring the latest 
            research papers, contributing to open-source projects, or writing technical blogs about my 
            learnings in the ML community.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Key highlights
        st.markdown("""
        <div style="background: linear-gradient(135deg, #1e3a8a, #3b82f6); padding: 1.5rem; border-radius: 15px; margin-top: 2rem; animation: fadeInUp 1.2s ease-out;">
            <h3 style="color: white; margin-bottom: 1rem;">🎯 Key Highlights</h3>
            <ul style="color: white; font-size: 1.1rem; line-height: 2;">
                <li>5+ Machine Learning projects deployed in production</li>
                <li>Specialized in Transformer models and Large Language Models</li>
                <li>Strong foundation in Deep Learning and Statistical NLP</li>
                <li>Active contributor to ML open-source community</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# PROJECTS SECTION
elif selected == "Projects":
    st.markdown('<h2 class="section-header">Featured Projects</h2>', unsafe_allow_html=True)
    
    # Project 1: Text Summarization
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #1e3a8a; font-size: 1.8rem; margin-bottom: 1rem;">📝 Intelligent Text Summarization System</h3>
        <p style="color: #64748b; font-size: 1.1rem; line-height: 1.6;">
        Built an advanced text summarization model using transformer-based architecture (T5/BART) that generates 
        concise and coherent summaries from long documents. The system handles both extractive and abstractive 
        summarization approaches, achieving high ROUGE scores on benchmark datasets.
        </p>
        <div style="margin-top: 1rem;">
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">Python</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">PyTorch</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">Transformers</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">FastAPI</span>
        </div>
        <div style="margin-top: 1.5rem;">
            <strong style="color: #1e3a8a;">Key Metrics:</strong> ROUGE-1: 0.45 | ROUGE-L: 0.38 | Inference Speed: <100ms
        </div>
        <div style="margin-top: 1.5rem;">
            <a href="https://your-demo-link.com" target="_blank" class="custom-button">🚀 Live Demo</a>
            <a href="https://github.com/yourusername/project" target="_blank" class="custom-button">💻 View Code</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 2: Topic Modeling
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #1e3a8a; font-size: 1.8rem; margin-bottom: 1rem;">🔍 Advanced Topic Modeling Engine</h3>
        <p style="color: #64748b; font-size: 1.1rem; line-height: 1.6;">
        Developed a scalable topic modeling system using BERTopic and LDA that automatically discovers hidden 
        themes in large text corpora. Implemented dynamic topic tracking over time and integrated visualization 
        dashboards for interpretable insights. Successfully applied to analyze customer feedback and social media data.
        </p>
        <div style="margin-top: 1rem;">
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">Python</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">BERTopic</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">Gensim</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">Streamlit</span>
        </div>
        <div style="margin-top: 1.5rem;">
            <strong style="color: #1e3a8a;">Performance:</strong> Processed 500K+ documents | 95% topic coherence | Real-time updates
        </div>
        <div style="margin-top: 1.5rem;">
            <a href="https://your-demo-link.com" target="_blank" class="custom-button">🚀 Live Demo</a>
            <a href="https://github.com/yourusername/project" target="_blank" class="custom-button">💻 View Code</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 3: Sentiment Analysis
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #1e3a8a; font-size: 1.8rem; margin-bottom: 1rem;">💭 Multi-lingual Sentiment Analysis</h3>
        <p style="color: #64748b; font-size: 1.1rem; line-height: 1.6;">
        Created a robust sentiment analysis system supporting 10+ languages using multilingual BERT models. 
        The system classifies text into positive, negative, and neutral sentiments with fine-grained emotion 
        detection. Deployed as a REST API handling 1000+ requests per second with 92% accuracy across languages.
        </p>
        <div style="margin-top: 1rem;">
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">Python</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">TensorFlow</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">BERT</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">Docker</span>
        </div>
        <div style="margin-top: 1.5rem;">
            <strong style="color: #1e3a8a;">Accuracy:</strong> 92% F1-Score | 10+ Languages | Production-Ready API
        </div>
        <div style="margin-top: 1.5rem;">
            <a href="https://your-demo-link.com" target="_blank" class="custom-button">🚀 Live Demo</a>
            <a href="https://github.com/yourusername/project" target="_blank" class="custom-button">💻 View Code</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 4: Named Entity Recognition
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #1e3a8a; font-size: 1.8rem; margin-bottom: 1rem;">🏷️ Custom NER System</h3>
        <p style="color: #64748b; font-size: 1.1rem; line-height: 1.6;">
        Developed a domain-specific Named Entity Recognition system using spaCy and fine-tuned BERT models 
        to extract entities like people, organizations, locations, and custom business entities from unstructured 
        text. Achieved state-of-the-art performance on domain-specific datasets with interactive visualization.
        </p>
        <div style="margin-top: 1rem;">
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">Python</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">spaCy</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">BERT</span>
            <span style="background: #dbeafe; color: #1e3a8a; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem; font-size: 0.9rem;">Flask</span>
        </div>
        <div style="margin-top: 1.5rem;">
            <strong style="color: #1e3a8a;">Results:</strong> 94% Precision | 91% Recall | 15+ Entity Types
        </div>
        <div style="margin-top: 1.5rem;">
            <a href="https://your-demo-link.com" target="_blank" class="custom-button">🚀 Live Demo</a>
            <a href="https://github.com/yourusername/project" target="_blank" class="custom-button">💻 View Code</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# SKILLS SECTION
elif selected == "Skills":
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="animation: fadeInUp 0.8s ease-out;">
            <h3 style="color: #1e3a8a; margin-bottom: 1.5rem;">🤖 Machine Learning & NLP</h3>
            
            <div>
                <p style="font-weight: 600; color: #475569; margin-bottom: 0.5rem;">Deep Learning</p>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: 90%">90%</div>
                </div>
            </div>
            
            <div>
                <p style="font-weight: 600; color: #475569; margin-bottom: 0.5rem;">Natural Language Processing</p>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: 95%">95%</div>
                </div>
            </div>
            
            <div>
                <p style="font-weight: 600; color: #475569; margin-bottom: 0.5rem;">Transformers & LLMs</p>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: 88%">88%</div>
                </div>
            </div>
            
            <div>
                <p style="font-weight: 600; color: #475569; margin-bottom: 0.5rem;">Computer Vision</p>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: 75%">75%</div>
                </div>
            </div>
            
            <div>
                <p style="font-weight: 600; color: #475569; margin-bottom: 0.5rem;">Statistical Machine Learning</p>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: 85%">85%</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="animation: fadeInUp 1s ease-out;">
            <h3 style="color: #1e3a8a; margin-bottom: 1.5rem;">🛠️ Frameworks & Libraries</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 0.8rem;">
                <span style="background: linear-gradient(135deg, #1e3a8a, #3b82f6); color: white; padding: 0.6rem 1.2rem; border-radius: 20
