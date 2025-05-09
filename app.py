import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Jason Yang | Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS
def local_css():
    st.markdown("""
    <style>
        .main {
            padding: 2rem 2rem;
        }
        h1, h2, h3 {
            color: #4B2E83;  /* UW Purple */
        }
        .education-entry, .experience-entry {
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid #f0f0f0;
        }
        .date-range {
            color: #666;
            font-weight: bold;
            float: right;
        }
        .edu-container {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            width: 100%;
        }
        .edu-info {
            flex: 3;
        }
        .edu-date {
            flex: 1;
            text-align: right;
        }
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 2rem;
        }
        .contact-info {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
        }
        .social-links a {
            margin-left: 1rem;
            color: #4B2E83;
        }
        .bullet-list li {
            margin-bottom: 0.5rem;
        }
        .profile-pic {
            border-radius: 5px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Header Section
st.markdown("<div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>", unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])

with col1:
    st.title("JASON YANG")
    st.write("AI Product Manager")
    
    contact_info = """
    <div style="display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 0.5rem;">
        <span>📧 itismejy@uw.edu</span>
        <span>📞 425-449-1522</span>
        <a href="https://www.linkedin.com/in/jason-z-yang/" target="_blank">🔗 LinkedIn</a>
    </div>
    """
    st.markdown(contact_info, unsafe_allow_html=True)
    
    # About Me Section
    st.markdown("### About Me")
    st.write("""
    I'm an AI Product Manager with experience in Microsoft, Baidu, and various startups.
    My expertise includes AI product development, user experience optimization, and data-driven decision making.
    Currently focused on building innovative solutions leveraging cutting-edge AI technologies.
    """)

with col2:
    # Profile image with styling
    # Display profile image
    st.image("https://firebasestorage.googleapis.com/v0/b/messengerai-2500f.appspot.com/o/profile_images%2FIMG_0130.JPG?alt=media&token=93951994-cc49-4f0f-a2eb-c2ceaeafe35b", 
             width=200, 
             caption="", 
             use_column_width=True, 
             output_format="JPEG",
             clamp=True)
    
    # Removed UW logo image

st.markdown("</div>", unsafe_allow_html=True)

# Education Section
st.header("Education")

education = [
    {
        "degree": "Master of Science in Technological Innovation",
        "institution": "Global Innovation Exchange Institute, University of Washington", 
        "period": "2023 – 2026"
    },
    {
        "degree": "Master of Science in Engineering (Data Science & IT)",
        "institution": "Global Innovation Exchange Institute, Tsinghua University", 
        "period": "2024 – 2026"
    },
    {
        "degree": "Bachelor of Arts in Management",
        "institution": "Guanghua School of Management, Peking University", 
        "period": "2018 – 2022"
    },
    {
        "degree": "Bachelor of Commerce",
        "institution": "Smith School of Business, Queen's University", 
        "period": "2018 – 2022"
    },
    {
        "degree": "Bilingual International Baccalaureate Diploma",
        "institution": "Interlake High School, Bellevue, WA", 
        "period": "2014 – 2018",
        "notes": "14 AP Exams; 6 IB Exams; National AP Scholar; AP International Diploma; 3.98 GPA; 35 ACT; 1530 SAT"
    }
]

for edu in education:
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"**{edu['degree']}**", unsafe_allow_html=True)
        st.write(edu['institution'])
        if 'notes' in edu:
            st.write(edu['notes'])
    with col2:
        st.markdown(f"<div style='text-align:right; font-weight:bold; color:#666;'>{edu['period']}</div>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 15px 0; opacity: 0.3;'>", unsafe_allow_html=True)

# Professional Experience
st.header("Professional Experience")

experiences = [
    {
        "title": "Product Manager Intern",
        "company": "Microsoft", 
        "location": "Redmond, WA, USA",
        "period": "5.2025 – 9.2025",
        "bullets": [
            "Accepted internship offer to be a product manager for Summer 2025 at Microsoft headquarters in Redmond WA"
        ]
    },
    {
        "title": "Product Manager Intern (Microsoft AI)",
        "company": "Microsoft STCA", 
        "location": "Beijing, China",
        "period": "2.2024 – 6.2024",
        "bullets": [
            "Shipped 2 features and 5 bug fixes to Microsoft Wallet after reviewing 600 user issues, improved DAU 900K to 950K (Edge v127)",
            "Launched new initiative for Windows OS password manager by understanding user behavior with 8 UX interviews in 3 cohorts",
            "Delivered 5 product specification documents to 2 UI designers and 3 developers to execute growth plans for Microsoft Wallet",
            "Enhanced micro-feedback feature using Azure LLM's to intelligently triage and prioritize 3000 user issues from OCV"
        ]
    },
    {
        "title": "AI Product Manager Intern (ERNIE)",
        "company": "Baidu", 
        "location": "Beijing, China",
        "period": "11.2023 – 2.2024",
        "bullets": [
            "Supported Agents for ERNIE by benchmarking quality metrics and organized internal blind A/B test to rank model outputs",
            "Standardized evaluation datasets for NL2SQL (500 queries) and E-Charts (100 queries); monthly competitor benchmarking",
            "Executed PRD to support E-charts in ERNIE and prioritized which charts to support by analyzing real customer queries"
        ]
    },
    {
        "title": "AI Product Management Intern",
        "company": "Kaito.ai", 
        "location": "Shanghai, China",
        "period": "Summer 2023",
        "bullets": [
            "Shipped payment feature for Kaito Metasearch, a Web 3.0 crypto search engine powered by OpenAI GPT4 (Series-A startup)",
            "Optimized LLM with LangChain and prompt engineering, increasing accuracy of answer results and user satisfaction",
            "Organized bi-weekly sprints and bug bash with Asana to streamline and prioritize features for UI design and front-end team"
        ]
    },
    {
        "title": "Global Management Trainee (GMT)",
        "company": "Budweiser APAC", 
        "location": "Shanghai, China",
        "period": "2022 – 2023",
        "bullets": [
            "Selected as 1 of 11 GMT in APAC region for Fortune 500 FMCG ABInBev; 4 months rotating Digital Marketing, Supply, and Sales",
            "Placed 1st in Supply Chain Final, delivered Grafana equipment status dashboard, empowering frontline with real-time PLC data"
        ]
    },
    {
        "title": "Data Product Management Intern",
        "company": "Stably.io", 
        "location": "Renton, WA, USA",
        "period": "Summer 2021",
        "bullets": [
            "Seattle-based startup specializing in Web 3.0 asset tokenization and fiat on-ramp for cryptocurrency (Series-A startup)",
            "Implemented Mixpanel product analytics into Stably Prime to track users experience and plan future features"
        ]
    },
    {
        "title": "Project Management Intern",
        "company": "Launch Consulting - TA Group Holdings", 
        "location": "Bellevue, WA, USA",
        "period": "Summer 2020",
        "bullets": [
            "Led agile technical development, SCRUM stand-ups for an automation project integrating HR's payroll and timesheet software",
            "Leveraged Azure DevOps to organize 3 bi-weekly sprint cycles; delivered 3 Azure functions reducing manual re-entry and error"
        ]
    }
]

for exp in experiences:
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"**{exp['title']}**, {exp['company']}, {exp['location']}", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='text-align:right; font-weight:bold; color:#666;'>{exp['period']}</div>", unsafe_allow_html=True)
    
    for bullet in exp['bullets']:
        st.markdown(f"• {bullet}")
    
    st.markdown("<hr style='margin: 15px 0; opacity: 0.3;'>", unsafe_allow_html=True)

# Extracurricular Experience
st.header("Extracurricular Experience")

extracurriculars = [
    {
        "title": "Product Manager & Frontend Mobile Developer",
        "company": "Hestia: Copilot for Parents", 
        "location": "Bellevue, WA, USA",
        "period": "10.2024 - Present",
        "bullets": [
            "Leading the development of a parenting copilot to guide parents overcome temper tantrums for toddlers with autism (ASD)",
            "Awarded with $1000 Azure credits by Microsoft for Startups to spend on OpenAI endpoint and Neo4J GraphRAG through Azure",
            "Submitted to Microsoft Imagine Cup 2025 with this professional pitch video and product demo of the MVP's core features"
        ]
    },
    {
        "title": "Product Manager & Full Stack Developer",
        "company": "EasyBites: AI Recipes", 
        "location": "Bellevue, WA, USA",
        "period": "Summer 2024",
        "bullets": [
            "Developed an MVP for a mobile app with personalized AI chefs which suggest meal plans for gym-goers with strict diets",
            "Shipped on iOS and Google Play Store, applied to YC Fall 2024 batch with the following in-depth product demo"
        ]
    },
    {
        "title": "Product Manager & Frontend Mobile Developer",
        "company": "Gather Mobile App", 
        "location": "Bellevue, WA, USA",
        "period": "2019 – 2023",
        "bullets": [
            "Co-founded and managed a startup to build and market an app to easily organize hangouts with friends",
            "Shipped on iOS and Google Play Store with 30K+ downloads: https://play.google.com/store/apps/details?id=com.gather123"
        ]
    },
    {
        "title": "Product Manager",
        "company": "Queen's Technology Media Association (QTMA)", 
        "location": "Kingston, ON, Canada",
        "period": "2019 – 2023",
        "bullets": [
            "Hired as 1 of 4 PMs, shipped a mobile meal generator named Stocked which suggests recipes based on available ingredients",
            "Managed 3 business analysts and 4 developers through JIRA, developed app with Flutter and Dart front-end, Firebase backend",
            "Placed 1st at Queen's University 2019 Demo Day, 1st at QTMA 2020 Final Pitch Competition; view the product on QTMA website"
        ]
    }
]

for extra in extracurriculars:
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"**{extra['title']}**, {extra['company']}, {extra['location']}", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='text-align:right; font-weight:bold; color:#666;'>{extra['period']}</div>", unsafe_allow_html=True)
    
    for bullet in extra['bullets']:
        st.markdown(f"• {bullet}")
    
    st.markdown("<hr style='margin: 15px 0; opacity: 0.3;'>", unsafe_allow_html=True)

# Skills Section
st.header("Skills & Interests")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Technical Skills")
    st.markdown("""
    - **Programming**: Dart, Python, C#, JavaScript
    - **Frameworks**: Flutter, AWS, Firebase, Unity, GCloud, Azure
    - **Other Tools**: JIRA, Asana, Figma, Azure DevOps
    """)

with col2:
    st.subheader("Interests")
    st.markdown("""
    - Bodybuilding (7 Years)
    - Reading (Psychology, Philosophy, Leadership)
    - MBTI: ENTJ
    - Favorite Book: Start With Why
    """)

# Footer
st.markdown("""
---
<div style="text-align: center; margin-top: 2rem; color: #666;">
    © 2024 Jason Yang | Portfolio created with Streamlit
</div>
""", unsafe_allow_html=True) 