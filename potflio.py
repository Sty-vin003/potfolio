import streamlit as st
from PIL import Image
import base64
from pathlib import Path
import webbrowser
import time
import random

# App Configuration
st.set_page_config(
    page_title="Steve Njoroge Macharia - Portfolio", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling with cinematic effects
st.markdown(
    """
    <style>
    /* Main app styling with dark theme */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
        color: #f0f0f0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Sidebar styling with red-black gradient */
    .css-1d391kg, .css-1d391kg > div:first-child {
        background: linear-gradient(to bottom, #000000 0%, #800000 30%, #800000 70%, #000000 100%) !important;
        border-right: 1px solid #ff0000;
    }
    
    /* Sidebar styling with dark red-black gradient */
    [data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(to bottom, #1a0000 0%, #300000 30%, #200000 70%, #0a0000 100%);
    border-right: 1px solid #ff3333;
    }

    
    .sidebar .sidebar-content {
        background: linear-gradient(to bottom, #000000 0%, #800000 30%, #800000 70%, #000000 100%) !important;
        border-right: 1px solid #ff0000;
    }
    
    /* Sidebar text styling */
    .sidebar-text {
        color: #ffffff !important;
    }
    
    .sidebar-text a {
        color: #ffcc00 !important;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    .sidebar-text a:hover {
        color: #ffffff !important;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }
    
    /* Sidebar buttons */
    .stButton button {
        background: linear-gradient(135deg, #800000 0%, #600000 100%) !important;
        color: white !important;
        border: 1px solid #ff0000 !important;
        border-radius: 8px;
        padding: 0.7rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        margin-bottom: 0.8rem;
        text-align: center;
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.2);
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%) !important;
        color: white !important;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.4);
        transform: translateY(-2px);
    }
    
    /* Main title with cinematic effect */
    .main-title {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ff0000 0%, #cc0000 50%, #ff3333 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
    }
    
    /* Subtitle styling */
    .subtitle {
        font-size: 1.5rem;
        font-weight: 500;
        color: #bbb;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
    }
    
    /* Section headers */
    .section-header {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #ff0000 0%, #cc0000 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 2.5rem;
        padding-bottom: 0.5rem;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px;
        border-left: 5px solid #ff0000;
        padding-left: 15px;
    }
    
    /* Card styling */
    .card {
        background: rgba(20, 20, 20, 0.8);
        border-radius: 10px;
        padding: 1.8rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        border: 1px solid #333;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.2);
        backdrop-filter: blur(10px);
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 25px rgba(255, 0, 0, 0.4);
        border: 1px solid #ff0000;
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ff3333;
        margin-bottom: 1rem;
        font-family: 'Orbitron', sans-serif;
    }
    
    .card-content {
        font-size: 1rem;
        color: #ccc;
        line-height: 1.6;
    }
    
    /* Skills container */
    .skills-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        margin-top: 1rem;
    }
    
    .skill-chip {
        background: linear-gradient(135deg, #ff0000 0%, #800000 100%);
        color: white;
        padding: 0.5rem 1.2rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .skill-chip:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
    }
    
    /* Floating WhatsApp button */
    .whatsapp-float {
        position: fixed;
        width: 60px;
        height: 60px;
        bottom: 40px;
        right: 40px;
        background-color: #25d366;
        color: #FFF;
        border-radius: 50px;
        text-align: center;
        font-size: 30px;
        box-shadow: 2px 2px 3px rgba(0, 0, 0, 0.3);
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
        animation: pulse 2s infinite;
        transition: all 0.3s ease;
    }
    
    .whatsapp-float:hover {
        transform: scale(1.1) rotate(5deg);
        box-shadow: 0 0 20px rgba(37, 211, 102, 0.8);
        background-color: #128C7E;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
        70% { box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
        100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
    }
    
    /* Matrix rain animation container */
    .matrix-rain {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        opacity: 0.1;
        pointer-events: none;
    }
    
    /* Dashboard buttons */
    .dashboard-btn {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
        color: #ff3333;
        border: 1px solid #ff0000;
        border-radius: 8px;
        padding: 0.7rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        margin-bottom: 0.8rem;
        text-align: center;
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.2);
    }
    
    .dashboard-btn:hover {
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
        color: white;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.4);
    }
    
    /* Matrix rain animation */
    .matrix-char {
        position: absolute;
        color: #00ff00;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        animation: matrix-rain 5s linear infinite;
        opacity: 0;
        text-shadow: 0 0 5px #00ff00;
    }
    
    @keyframes matrix-rain {
        0% {
            transform: translateY(-100px);
            opacity: 1;
        }
        100% {
            transform: translateY(calc(100vh + 100px));
            opacity: 0;
        }
    }
    
    /* Typewriter effect */
    .typewriter {
        overflow: hidden;
        border-right: 3px solid #ff0000;
        white-space: wrap;
        margin: 0 auto;
        letter-spacing: 0.15em;
        animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
    }
    
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: #ff0000 }
    }
    
    /* Particle animation */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        pointer-events: none;
    }
    
    .particle {
        position: absolute;
        background: rgba(255, 0, 0, 0.5);
        border-radius: 50%;
        animation: float 15s infinite linear;
    }
    
    @keyframes float {
        0% {
            transform: translateY(0) translateX(0) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(-100vh) translateX(100vw) rotate(360deg);
            opacity: 0;
        }
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Matrix rain animation
def create_matrix_rain():
    matrix_html = """
    <div style="width:100%; max-width:900px; margin:auto;">
        <canvas id="matrixCanvas"></canvas>
    </div>

    <script>
        const canvas = document.getElementById("matrixCanvas");
        const ctx = canvas.getContext("2d");

        function resizeCanvas() {
            canvas.width = canvas.parentElement.offsetWidth;  // responsive width
            canvas.height = 200;  // fixed height (you can change or make % of width)
        }

        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        const letters = "01STEVE0101NJOROGE0101MACHARIA".split("");
        const fontSize = 14;
        let columns, drops;

        function initDrops() {
            columns = Math.floor(canvas.width / fontSize);
            drops = Array(columns).fill(1);
        }

        initDrops();

        function draw() {
            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = "#0F0";
            ctx.font = fontSize + "px monospace";

            for (let i = 0; i < drops.length; i++) {
                const text = letters[Math.floor(Math.random() * letters.length)];
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }
                drops[i]++;
            }
        }

        setInterval(draw, 33);
        window.addEventListener('resize', initDrops);
    </script>

    <style>
        #matrixCanvas {
            display: block;
            width: 100%;   /* responsive */
            height: auto;  /* keeps aspect ratio */
            background: black;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,255,0,0.5);
        }
    </style>
    """
    st.components.v1.html(matrix_html, height=220)  # just needs enough space



# Particle animation
def create_particles():
    particles_html = """
    <div class="particles" id="particles"></div>
    <script>
        function createParticles() {
            const container = document.getElementById('particles');
            const particleCount = 50;
            
            for (let i = 0; i < particleCount; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                
                // Random size between 2 and 5 pixels
                const size = Math.random() * 3 + 2;
                particle.style.width = size + 'px';
                particle.style.height = size + 'px';
                
                // Random position
                particle.style.left = Math.random() * 100 + 'vw';
                particle.style.top = Math.random() * 100 + 'vh';
                
                // Random animation duration
                const duration = Math.random() * 10 + 10;
                particle.style.animationDuration = duration + 's';
                
                // Random delay
                particle.style.animationDelay = Math.random() * 5 + 's';
                
                container.appendChild(particle);
            }
        }
        
        // Initialize particles
        createParticles();
    </script>
    """
    st.components.v1.html(particles_html, height=0)

# Function to create a download link for files
def create_download_link(file_path, file_label):
    with open(file_path, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{Path(file_path).name}">{file_label}</a>'
    return href

# Function to open WhatsApp
def open_whatsapp():
    webbrowser.open_new_tab("https://wa.me/254712345678")  # Replace with your actual number

# Initialize session state
if 'current_dashboard' not in st.session_state:
    st.session_state.current_dashboard = None
if 'show_floating_buttons' not in st.session_state:
    st.session_state.show_floating_buttons = True

# Create matrix rain background
create_matrix_rain()

# Create particle animation
create_particles()

# Display animated name
name = "STEVEN NJOROGE MACHARIA"
animated_name = f"""
<div class="main-title" style="animation: fadeIn 2s ease-out;">
    {name}
</div>
"""

# Create two columns for the layout (replicating your original layout)
col1, col2 = st.columns([3, 1])

# Display the main title and subtitle in the left column
with col1:
    st.markdown(animated_name, unsafe_allow_html=True)
    st.markdown("""
    <div class="typewriter subtitle">
        Android Developer | Web Designer | Software Engineer | Tech Enthusiast
    </div>
    """, unsafe_allow_html=True)
    st.write("""
    <div style='color: #ccc; line-height: 1.6;'>
    A passionate software engineer with expertise in creating innovative digital experiences. 
    Specializing in Android development, web design, and data storytelling with a keen eye for 
    aesthetics and functionality. Committed to pushing the boundaries of technology and design.
    </div>
    """, unsafe_allow_html=True)

# Display the image in the right column (your original placement)
with col2:
    try:
        image_top_right = Image.open("top_right.png")  # Your original image name
        st.image(image_top_right, width=150, output_format="PNG")
    except:
        st.info("Add your image as 'top_right.png'")

# Sidebar with profile image and buttons (your original placement)
try:
    image = Image.open("profile.JPG")  # Your original image name
    st.sidebar.image(image, caption="Steven Njoroge Macharia", width=200)
except:
    st.sidebar.info("Add your profile image as 'profile.jpg'")

st.sidebar.markdown("""
<div style='text-align: center; 
            margin-bottom: 2rem;
            background: linear-gradient(135deg, #ff0000, #000000);
            '>
    <h2 style='color: #ffcc00; font-family: Orbitron, sans-serif;'>CONTACT</h2>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<p class='sidebar-text'>📧 <strong>Email:</strong> stevenmacharia2003@gmail.com</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p class='sidebar-text'><a href='https://www.linkedin.com/in/steven-nj-272615300/' target='_blank'>🔗 LinkedIn Profile</a></p>", unsafe_allow_html=True)
st.sidebar.markdown("<p class='sidebar-text'><a href='https://github.com/Sty-vin003' target='_blank'>🐱 GitHub Profile</a></p>", unsafe_allow_html=True)

# Dashboard buttons in sidebar


# Skills Section
st.markdown("<p class='section-header'>TECHNICAL SKILLS</p>", unsafe_allow_html=True)

# Updated skills including Python, PHP, and design skills
skills = ["Kotlin", "Node.js", "Python", "PHP", "MySQL / Postgres", "database", "Git/GitHub", 
          "Google Sheet Expert", "JavaScript", "Business Card Design",
          "Flyer Design", "Data Visualization","API usage", "creativity", "critical thinking",  "adaptability"]

skills_html = "<div class='skills-container'>"
for skill in skills:
    skills_html += f"<div class='skill-chip'>{skill}</div>"
skills_html += "</div>"

st.markdown(f"<div class='card'><div class='card-title'>CORE COMPETENCIES</div><div class='card-content'>{skills_html}</div></div>", unsafe_allow_html=True)

# Design Portfolio Section (Business Cards & Flyers)
st.markdown("<p class='section-header'>DESIGN PORTFOLIO</p>", unsafe_allow_html=True)
st.markdown("### BUSINESS CARDS & FLYERS")

# Create a gallery for design work
design_col1, design_col2, design_col3 = st.columns(3)

with design_col1:
    try:
        design1 = Image.open("design1.jpg")
        st.image(design1, caption="Business Card Design", use_container_width=True)
    except:
        st.info("Add your design work as 'design1.jpg'")

with design_col2:
    try:
        design2 = Image.open("design2.jpg")
        st.image(design2, caption="Business Card Design", use_container_width=True)
    except:
        st.info("Add your design work as 'design2.jpg'")

with design_col3:
    try:
        design3 = Image.open("design3.jpg")
        st.image(design3, caption="Marketing Material / flyer", use_container_width=True)
    except:
        st.info("Add your design work as 'design3.jpg'")


# Projects Section
st.markdown("<p class='section-header'>PROJECT SHOWCASE</p>", unsafe_allow_html=True)
st.markdown("Visit my GitHub to see these and more projects.")

# Real World Client Projects with Anchor Links
st.markdown("<p class='section-header'>REAL WORLD CLIENT PROJECTS</p>", unsafe_allow_html=True)

# Project data - replace with your actual projects
client_projects = [
    {
        "name": "THERAPY CENTRE WEBSITE",
        "description": "A full-featured online website for a therapy centre",
        "url": "https://kazimind-website-1.onrender.com",
        "technologies": ["php", "database / postgres", "javascript", "APIs", "mailer", "git/github"]
    },
    {
        "name": "CONSULTANCY FIRM WEBSITE",
        "description": "a very asthetic website for a consultacy firm with all relevant content",
        "url": "https://bellwickllp.com",
        "technologies": ["mailer", "javascript", "git/github", "php"]
    }
]

# Create project cards with anchor links
for project in client_projects:
    technologies_html = "<div class='skills-container'>"
    for tech in project["technologies"]:
        technologies_html += f"<div class='skill-chip'>{tech}</div>"
    technologies_html += "</div>"
    
    st.markdown(
        f"""
        <div class='card'>
            <div class='card-title'>
                <a href="{project['url']}" target="_blank" style="color: #ff3333; text-decoration: none;">
                    {project['name']} ↗
                </a>
            </div>
            <div class='card-content'>{project['description']}</div>
            <div class='card-content'><strong style='color: #ff3333;'>Technologies Used:</strong>{technologies_html}</div>
            <div class='card-content'>
                <a href="{project['url']}" target="_blank" class="project-link">
                    Visit Live Website
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Additional CSS styling for project links
st.markdown(
    """
    <style>
    .project-link {
        display: inline-block;
        background: linear-gradient(135deg, #ff0000 0%, #800000 100%);
        color: white;
        padding: 0.7rem 1.5rem;
        border-radius: 5px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
        margin-top: 1rem;
    }
    
    .project-link:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
        color: white;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<p class='section-header'>OTHER FUN PROJECTS</p>", unsafe_allow_html=True)

# Display projects in cards
projects = {
    "Drawing App": {
        "description": "An Android app for sketching and drawing with advanced features and export capabilities.",
        "skills_earned": ["UI/UX Design", "Android Development", "Bitmap Processing", "Kotlin Programming"]
    },
    "Workout App": {
        "description": "A fitness tracking application with personalized workout plans and progress analytics.",
        "skills_earned": ["Database Management", "RecyclerView & Adapters", "Media Handling", "User Experience Design"]
    },
    "Calculator App": {
        "description": "A functional Android calculator with advanced features and elegant design.",
        "skills_earned": ["Android UI Development", "Event Handling", "Error Handling", "Mathematical Operations"]
    },
    "Digital Farmers": {
        "description": "An e-commerce platform for urban farming enthusiasts with inventory management.",
        "skills_earned": ["Web Development", "Database Management", "Node.js"]
    },
    "Data Storytelling Platform": {
        "description": "An interactive platform for creating and sharing data stories with visualization tools.",
        "skills_earned": ["Data Visualization", "Storytelling", "Google Sheets API", "Dashboard Design"]
    }
}

for title, details in projects.items():
    skills_earned_html = "<ul style='padding-left: 20px; color: #ccc;'>"
    for skill in details["skills_earned"]:
        skills_earned_html += f"<li>{skill}</li>"
    skills_earned_html += "</ul>"

    st.markdown(
        f"""
        <div class='card'>
            <div class='card-title'>{title}</div>
            <div class='card-content'>{details["description"]}</div>
            <div class='card-content'><strong style='color: #ff3333;'>Technologies Used:</strong>{skills_earned_html}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Data Storytelling Section
st.markdown("<p class='section-header'>DATA STORYTELLING</p>", unsafe_allow_html=True)
st.write("Examples of my data visualization and storytelling work:")

# Add your original images here
data_storytelling_images = ["students dashb.PNG", "story1.png"]  # Your original image names
for image_path in data_storytelling_images:
    try:
        image = Image.open(image_path)
        st.image(image, caption="Data Storytelling Example", width=600)
    except:
        st.info(f"Add your data visualization as '{image_path}'")

# Education & Achievements
st.markdown("<p class='section-header'>EDUCATION & ACHIEVEMENTS</p>", unsafe_allow_html=True)

# Display education and achievements in cards
education = [
    {
        "title": "Bachelor of Science in Software Engineering",
        "subtitle": "Zetech University",
        "content": "Expected Graduation: 2025"
    },
    {
        "title": "PLP Software Development Program Participant",
        "subtitle": "Certificate of Participation",
        "content": "Earned a certificate for outstanding participation and innovative solution development."
    },
]

for edu in education:
    st.markdown(
        f"""
        <div class='card'>
            <div class='card-title'>{edu["title"]}</div>
            <div class='card-content' style='color: #ff3333; font-weight: 600;'>{edu["subtitle"]}</div>
            <div class='card-content'>{edu["content"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# Floating WhatsApp button
whatsapp_button = """
<style>
.whatsapp-float {
    position: fixed;
    width: 60px;
    height: 60px;
    bottom: 40px;
    right: 40px;
    background-color: #25d366;
    color: #FFF;
    border-radius: 50px;
    text-align: center;
    font-size: 30px;
    box-shadow: 2px 2px 3px rgba(0, 0, 0, 0.3);
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
    70% { box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
    100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
}
</style>

<a href="https://wa.me/254758844476" class="whatsapp-float" target="_blank">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="30" height="30" fill="white">
        <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/>
    </svg>
</a>
"""

st.markdown(whatsapp_button, unsafe_allow_html=True)
# Fancy download buttons for CV and Resume
# Load your files
with open("Steven_CV.pdf", "rb") as cv_file:
    cv_bytes = cv_file.read()

with open("Steven_Resume.pdf", "rb") as resume_file:
    resume_bytes = resume_file.read()

# Encode files in base64 for CSS/HTML positioning
cv_b64 = base64.b64encode(cv_bytes).decode()
resume_b64 = base64.b64encode(resume_bytes).decode()

# Custom floating buttons with real downloads
download_buttons = f"""
<style>
.download-float {{
    position: fixed;
    width: 60px;
    height: 60px;
    background-color: #ff3333;
    color: #FFF;
    border-radius: 50px;
    text-align: center;
    font-size: 30px;
    box-shadow: 2px 2px 3px rgba(0, 0, 0, 0.3);
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: pulse-red 2s infinite;
    transition: all 0.3s ease;
    cursor: pointer;
    border: none;
    text-decoration: none;
}}

.download-float:hover {{
    transform: scale(1.1) rotate(5deg);
    box-shadow: 0 0 20px rgba(255, 51, 51, 0.8);
    background-color: #cc0000;
}}

.cv-download {{
    bottom: 120px;
    right: 40px;
}}

.resume-download {{
    bottom: 200px;
    right: 40px;
}}

@keyframes pulse-red {{
    0% {{ box-shadow: 0 0 0 0 rgba(255, 51, 51, 0.7); }}
    70% {{ box-shadow: 0 0 0 15px rgba(255, 51, 51, 0); }}
    100% {{ box-shadow: 0 0 0 0 rgba(255, 51, 51, 0); }}
}}
</style>

<a href="data:application/pdf;base64,{resume_b64}" download="Steven_Resume.pdf" class="download-float resume-download" title="Download / View Resume">📝</a>
<a href="data:application/pdf;base64,{cv_b64}" download="Steven_CV.pdf" class="download-float cv-download" title="Download / View CV">📄</a>
"""

st.markdown(download_buttons, unsafe_allow_html=True)
# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #ff3333; font-size: 1.1rem; padding: 1.5rem;'>
        <p style='font-weight: 600; margin-bottom: 0.5rem; text-shadow: 0 0 10px rgba(255, 0, 0, 0.5);'>LET'S CONNECT AND BUILD AMAZING THINGS TOGETHER! ⚡</p>
        <div style='display: flex; justify-content: center; gap: 1.5rem;'>
            <a href='https://www.linkedin.com/in/steven-nj-272615300/' target='_blank' style='color: #ff3333; text-decoration: none; text-shadow: 0 0 5px rgba(255, 0, 0, 0.3);'>LINKEDIN</a>
            <a href='https://github.com/Sty-vin003' target='_blank' style='color: #ff3333; text-decoration: none; text-shadow: 0 0 5px rgba(255, 0, 0, 0.3);'>GITHUB</a>
            <a href='mailto:stevenmacharia2003@gmail.com' style='color: #ff3333; text-decoration: none; text-shadow: 0 0 5px rgba(255, 0, 0, 0.3);'>EMAIL</a>
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)