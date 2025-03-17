import streamlit as st
from PIL import Image

# App Configuration
st.set_page_config(page_title="Steve Njoroge Macharia - Portfolio", page_icon="", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
    /* Apply background color to the entire app */
    .stApp {
        background-color: #d8cee6;
    }
    .main-title {
        font-size: 48px;
        font-family: sanserif
        font-weight: bold;
        color: #004080;
        text-align: center;
    }
    
    .subtitle {
        font-size: 24px;
        font-weight: bold;
        color: maroon;
        text-align: center;
    }
    
    .section-header {
        font-size: 22px;
        font-weight: bold;
        color: #004080;
        margin-top: 30px;
        border-bottom: 3px solid maroon;
        padding-bottom: 5px;
    }
    .sidebar-text {
        font-size: 18px;
        font-weight: bold;
        color: maroon;
    }
    
    @keyframes pop {
        0% { transform: scale(1); }
        50% { transform: scale(1.5); }
        100% { transform: scale(1); }
    }
    .main-title span {
        display: inline-block;
        animation: pop 0.5s ease-in-out;
        animation-delay: calc(var(--delay) * 0.2s);
    }

    /* Card Styling */
    .card {
        background-color: white; /* Ensure cards have a white background */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        padding: 20px;
        margin: 10px 0;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }
    .card-title {
        font-size: 20px;
        font-weight: bold;
        color: #004080;
        margin-bottom: 10px;
    }
    .card-content {
        font-size: 16px;
        color: #333;
    }
    .skills-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    .skill-chip {
        background-color: #004080;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
    }
    .education-card {
        background-color: white; /* Ensure education cards have a white background */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        padding: 20px;
        margin: 10px 0;
    }
    .education-title {
        font-size: 20px;
        font-weight: bold;
        color: #004080;
    }
    .education-subtitle {
        font-size: 16px;
        color: maroon;
        margin-bottom: 10px;
    }
    .education-content {
        font-size: 14px;
        color: #333;
    }

    /* Remove alternating card colors */
    /* .card:nth-child(3n+1) {
        background-color: #72435c;
    }
    .card:nth-child(3n+2) {
        background-color: #b4f8c8;
    }
    .card:nth-child(3n+3) {
        background-color: #424651;
    } */
    </style>
    """,
    unsafe_allow_html=True
)

# Display animated name
name = "Steven Njoroge Macharia"
animated_name = "".join(
    f"<span style='--delay:{i}; animation-delay: {i * 0.2}s'>{char}</span>" if char != " " else " " for i, char in enumerate(name)
)

# Create two columns for the layout
col1, col2 = st.columns([3, 1])

# Display the main title and subtitle in the left column
with col1:
    st.markdown(f"<div class='main-title'>{animated_name}</div>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Android Developer | Web Designer | Software Engineer | Tech Enthusiast |  Data Storytelling expert</p>", unsafe_allow_html=True)
    st.write("Aspiring Android Developer and Software Engineer with a strong determination to build innovative and impactful digital experiences. Highly skilled in Kotlin, Node.js, and Firebase, with a relentless drive to learn, adapt, and master new technologies. Committed to continuous growth and pushing the boundaries of mobile app development.")

# Display the image in the right column
with col2:
    image_top_right = Image.open("top_right.png")  # Replace with your image file
    st.image(image_top_right, width=150)

# Sidebar with profile image
image = Image.open("profile.JPG")  
st.sidebar.image(image, caption="Steven Njoroge Macharia", width=200)
st.sidebar.markdown("<p class='sidebar-text'>Email: stevenmacharia2003@gmail.com</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p class='sidebar-text'><a href='https://www.linkedin.com/in/steven-nj-272615300/' target='_blank'>Visit my LinkedIn account</a></p>", unsafe_allow_html=True)
st.sidebar.markdown("<p class='sidebar-text'><a href='https://github.com/Sty-vin003' target='_blank'>Visit my GitHub account</a></p>", unsafe_allow_html=True)

# Skills Section
st.markdown("<p class='section-header'>Technical Skills</p>", unsafe_allow_html=True)

# Display skills in a card with chips
skills = ["Kotlin", "Node.js", "SQLite", "Firebase", "Git/GitHub", "Google Sheet Expert", "Creativity", "Problem Solving", "javascript"]
skills_html = "<div class='skills-container'>"
for skill in skills:
    skills_html += f"<div class='skill-chip'>{skill}</div>"
skills_html += "</div>"

st.markdown(f"<div class='card'><div class='card-title'>Skills</div><div class='card-content'>{skills_html}</div></div>", unsafe_allow_html=True)

# Projects Section
st.markdown("<p class='section-header'>Projects : Visit my github to see this and more projects.</p>", unsafe_allow_html=True)

# Display projects in cards
projects = {
    "Drawing App": {
        "description": "An Android app for sketching and drawing.",
        "skills_earned": ["UI/UX Design", "Android Development",
                          "Bitmap and Image Processing – Converting drawings to images and exporting them.",
                          "Kotlin Programming – Working with classes, functions, and coroutines.",
                          "Android Canvas API – Drawing shapes, paths, and handling touch events. ETC"]
    },
    "Workout App": {
        "description": "A fitness tracking application for managing workouts.",
        "skills_earned": [ "SharedPreferences & Databases – Storing user progress and workout history.", 
                        "RecyclerView & Adapters – Displaying exercises in lists/grids.",
                        "Media & Audio Handling – Playing workout timers, voice guidance, or background music. ETC"]
    },
    "Calculator": {
        "description": "A simple yet functional Android calculator.",
        "skills_earned": ["Android UI Development – Designing a responsive layout using XML.", 
                          "Event Handling – Handling button clicks and user inputs",
                          "Error Handling – Preventing crashes due to division by zero or invalid inputs. ETC"]
    },
    "Digital Farmers": {
        "description": "A platform for urban farming and gardening enthusiasts. Built with HTML, CSS, and Node.js.",
        "skills_earned": ["Web Development", "Database Management", "Node.js"]
    },
    "Storytelling": {
        "description": "A project showcasing data storytelling skills.",
        "skills_earned": ["Data Visualization", "Storytelling", "Google Sheets"]
    }
}

for title, details in projects.items():
    skills_earned_html = "<ul>"
    for skill in details["skills_earned"]:
        skills_earned_html += f"<li>{skill}</li>"
    skills_earned_html += "</ul>"

    st.markdown(
        f"""
        <div class='card'>
            <div class='card-title'>{title}</div>
            <div class='card-content'>{details["description"]}</div>
            <div class='card-content'><strong>Skills Earned:</strong>{skills_earned_html}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Data Storytelling Section
st.markdown("<p class='section-header'>Data Storytelling</p>", unsafe_allow_html=True)
st.write("Here are some examples of my data storytelling work:")

# Add your images here
data_storytelling_images = ["students dashb.png", "story1.png"]  # Replace with your image files
for image_path in data_storytelling_images:
    image = Image.open(image_path)
    st.image(image, caption="Data Storytelling Example", width=600)

# Education & Achievements
st.markdown("<p class='section-header'>Education & Achievements</p>", unsafe_allow_html=True)

# Display education and achievements in cards
education = [
    {
        "title": "Bachelor of Science in Software Engineering",
        "subtitle": "Zetech University",
        "content": "Expected Graduation: 2025"
    },
    {
        "title": "PLP Hackathon Participant",
        "subtitle": "Certificate of Participation",
        "content": "Earned a certificate for outstanding participation."
    }
]

for edu in education:
    st.markdown(
        f"""
        <div class='education-card'>
            <div class='education-title'>{edu["title"]}</div>
            <div class='education-subtitle'>{edu["subtitle"]}</div>
            <div class='education-content'>{edu["content"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.write("---")
st.markdown("<p style='text-align:center; font-size:18px; color:#004080;'>Let's connect and build amazing things together!</p>", unsafe_allow_html=True)
