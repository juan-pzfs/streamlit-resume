import streamlit as st
import pandas as pd
import os

# Custom CSS for Dark & Light Mode + Fix Light Mode Input Visibility
def apply_custom_styles():
    dark_mode = st.session_state.get("dark_mode", False)

    if dark_mode:
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #1E1E1E;
                color: white;
            }
            .stButton>button {
                background-color: #444 !important;
                color: white !important;
                border: 2px solid white !important;
            }
            .stDownloadButton>button {
                background-color: #555 !important;
                color: white !important;
                border: 2px solid white !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #F5F5F5;
                color: black;
            }
            .stButton>button {
                background-color: #0078D4 !important;
                color: white !important;
                border: 2px solid #005A9E !important;
                border-radius: 8px !important;
                font-weight: bold !important;
            }
            .stDownloadButton>button {
                background-color: #004C99 !important;
                color: white !important;
                border: 2px solid #003366 !important;
                border-radius: 8px !important;
                font-weight: bold !important;
            }
            label {
                color: black !important;
                font-weight: bold !important;
            }
            input, textarea {
                background-color: white !important;
                color: black !important;
                border: 1px solid #ccc !important;
                border-radius: 5px !important;
                padding: 8px !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

# Page Config
st.set_page_config(page_title="Juan Pablo Perez | Data & BI Analyst", page_icon="📊", layout="wide")

# Theme Toggle
col1, col2 = st.columns([0.8, 0.2])
with col2:
    if st.button("🌙 Toggle Dark Mode"):
        st.session_state.dark_mode = not st.session_state.get("dark_mode", False)
apply_custom_styles()  # Apply custom styles

# Title and Introduction
st.title("Juan Pablo Perez Flores")  
st.write("### Data & Business Intelligence Analyst | Python | Power BI | SQL | Tableau")  
st.write("Transforming data into insights to drive efficiency, optimize decision-making, and uncover strategic opportunities.")  
st.write("[📧 Email](mailto:juanp.pzfs@gmail.com) | [🔗 LinkedIn](https://www.linkedin.com/in/juan-pablo-perez-flores/)")

# Resume Download Buttons
st.write("📄 **Download My Resumes:**")
col1, col2 = st.columns(2)
with col1:
    with open("Juan_Pablo_Perez_Resume_Data_Analyst.pdf", "rb") as data_analyst_resume:
        st.download_button(label="📥 Download Data Analyst Resume", 
                            data=data_analyst_resume, 
                            file_name="Juan_Pablo_Perez_Resume_Data_Analyst.pdf", 
                            mime="application/pdf")

with col2:
    with open("Juan_Pablo_Perez_Resume_BI_Analyst.pdf", "rb") as bi_analyst_resume:
        st.download_button(label="📥 Download BI Analyst Resume", 
                            data=bi_analyst_resume, 
                            file_name="Juan_Pablo_Perez_Resume_BI_Analyst.pdf", 
                            mime="application/pdf")

st.write("---")

# Why Hire Me Section
st.header("🌟 Why Hire Me?")
st.write("""
I am passionate about **data analytics and business intelligence**, thriving in environments  
where I can **learn, adapt, and solve complex problems**.  

With experience **automating processes using Python** and **designing interactive dashboards in Power BI**,  
I have worked on diverse projects that strengthened my ability to **turn raw data into meaningful insights**.  

What excites me most is the opportunity to **collaborate with teams, tackle real-world challenges,  
and continuously refine my skills**. I believe that **growth comes from taking on new challenges**,  
and I am eager to explore **new industries, technologies, and perspectives**.  

I am looking to contribute to a **team that values innovation, efficiency, and continuous improvement**.  
I bring **a strong work ethic, analytical expertise, and a deep commitment to delivering high-impact results**.  
""")

st.write("---")


# Work Experience Section
st.header("💼 Work Experience")

with st.expander("📊 Supply Chain Data Analyst Intern - CHRISTUS Health"):
    st.write("📅 **June 2023 - Present | Irving, TX**")
    st.write("")  # Forces a line break
    st.write("""
    During my internship at CHRISTUS Health, I worked on **optimizing data processes**  
    to support supply chain operations across Latin America. I developed **Python scripts**  
    that automated data extraction for over **20,000+ medical supplies**, reducing manual  
    work by **94%**. I also cleaned and structured **150,000+ records** using **SQL and Python**,  
    ensuring data accuracy for strategic decision-making.  

    To enhance financial transparency, I built an **automated Power BI dashboard** that  
    dynamically tracks **savings, costs, and inflation impact**, providing real-time visibility  
    to executives. Additionally, I led **process automation projects** using **Python and Knime**,  
    which reduced data processing time by **98%**, allowing for faster and more efficient analysis.  

    This experience strengthened my ability to work in **fast-paced environments, collaborate  
    with stakeholders, and implement automation solutions that drive real business impact.**  
    """)

with st.expander("📁 Lead Student Worker - University of Texas at Arlington"):
    st.write("📅 **Feb 2021 - June 2023 | Arlington, TX**")
    st.write("")  # Forces a line break
    st.write("""
    During my time as a Lead Student Worker at UTA, I was responsible for managing  
    and maintaining **student immigration records**, ensuring **compliance and accuracy**  
    for over **4,000+ students**. To streamline operations, I built an **Excel-based tracking system**  
    that improved organization and efficiency in document management.  

    Recognizing the need to **reduce manual tasks**, I automated workflows using **Excel functions  
    and Power Query**, significantly reducing processing time and improving overall accuracy.  
    This experience strengthened my ability to **work independently, manage high-volume data,  
    and implement process improvements** in a fast-paced environment.
    """)

st.write("---")

# Projects Section
st.header("📊 Business Intelligence & Data Analytics Projects")

with st.expander("📌 Automated Inventory & Spend Analysis - Python, Excel"):
    st.write("""
    To improve efficiency in supply chain management, I developed a **Python script**  
    that automated the extraction and analysis of inventory data for **35,000+ medical supplies**.  
    This significantly reduced processing time by **99%**, allowing for faster decision-making.  

    Additionally, I cleaned and merged datasets to analyze **spending trends, stock turnover,  
    and risk categories**, providing better visibility into supply chain operations. The project  
    also included an **automated KPI report generation system**, exporting reports in Excel with  
    **color-coded risk categorization** to highlight high-priority inventory items.
    """)

with st.expander("📊 Latin America Project Dashboard - Power BI"):
    st.write("""
    I developed an **interactive Power BI dashboard** to track **key financial metrics**  
    across **Chile, Colombia, and Mexico**. The dashboard provided insights into **savings,  
    cost trends, and inflation impact**, helping executives make data-driven decisions.  

    To ensure real-time accuracy, I automated data updates by linking **Power BI to Excel**,  
    enabling seamless integration and reporting.
    """)

with st.expander("🤖 Facial Recognition Model - Orange Analytics, ML"):
    st.write("""
    Using **Orange Analytics**, I built a **facial recognition model** trained to classify images  
    of **Cillian Murphy, Emma Stone, and Matt Damon**. I tested multiple machine learning models,  
    including **KNN, Random Forest, Logistic Regression, and Neural Networks**, with  
    **Logistic Regression and Neural Networks achieving the highest accuracy of 94%**.  

    This project provided hands-on experience in **classification algorithms, model validation,  
    and performance evaluation**.
    """)

with st.expander("📊 Home Credit Prediction Analysis - Python, Scikit-Learn"):
    st.write("""
    In this project, I developed a **machine learning model** to predict loan approval outcomes,  
    helping financial institutions assess **credit risk**. The process involved **data preprocessing,  
    exploratory data analysis (EDA), and feature engineering** to enhance model performance.  

    I tested different ML models, including **logistic regression and decision trees**,  
    achieving **74% accuracy**. The project strengthened my skills in **data cleaning,  
    model selection, and predictive analytics**.
    """)

with st.expander("🔎 Web Scraping for Medical Products - Python, Selenium, BeautifulSoup"):
    st.write("""  
    To automate data collection for **medical product information**, I developed a  
    **web scraping script** using **Selenium and BeautifulSoup**.  

    This script reduced the data extraction time from **15 minutes per 10 records to just 1 minute**,  
    significantly improving efficiency. The project involved **handling dynamic web elements,  
    processing scraped data in Pandas, and exporting structured datasets for further analysis**.
    """)

with st.expander("⚽ AI-Powered Soccer Chatbot - Botpress"):
    st.write("""
    I developed a **chatbot using Botpress** to provide real-time information on  
    **European soccer leagues, teams, and players**. The chatbot allows users to  
    request details on **league standings, top scorers, and upcoming fixtures**  
    for specific teams and competitions.  

    Using **workflow automation in Botpress**, I structured conversations so users  
    could naturally interact with the chatbot. The system retrieves **live data from  
    a structured SQL database**, ensuring accurate and up-to-date responses.  

    This project enhanced my skills in **automating user interactions, integrating databases  
    into chatbot systems, and designing structured conversation flows** to improve  
    accessibility to sports data.
    """)

st.write("---")

# Skills Section with Strength Scale
st.header("🛠️ Skills & Competencies")

# Technical Skills
st.subheader("📌 Technical Skills")
technical_skills = {
    "Python": 91,
    "Excel": 90,
    "Dashboard Design": 90,
    "Automation (Knime, Python, Selenium)": 85,
    "Power BI": 82,
    "Web Scraping (Selenium, BeautifulSoup)": 68,
    "Tableau": 63,
    "SQL": 60,
    "Database Management (SQL, Informatica)": 60,
    "AI Development (Chatbots)": 55,
    "ETL Processes (Informatica, Knime)": 50
}

for skill, level in technical_skills.items():
    st.write(f"**{skill}**")
    st.progress(level / 100)

st.write("---")  # Separator

# Statistical & Analytical Skills
st.subheader("📊 Statistical & Analytical Skills")
statistical_skills = {
    "Data Cleaning & Transformation": 87,
    "Exploratory Data Analysis (EDA)": 75,
    "Feature Engineering": 70,
    "Data Modeling & Structuring": 73,
    "Time-Series Analysis": 62,
    "Machine Learning": 65,
    "A/B Testing & Experimentation": 60
}

for skill, level in statistical_skills.items():
    st.write(f"**{skill}**")
    st.progress(level / 100)

st.write("---")  # Separator

# Business & Soft Skills
st.subheader("📈 Business & Soft Skills")
business_skills = {
    "Adaptability & Learning Agility": 95,
    "Cross-Functional Collaboration": 90,
    "Communication & Data Storytelling": 90,
    "Attention to Detail": 92,
    "Time Management & Prioritization": 92,
    "Problem-Solving": 85,
    "Business Process Optimization": 87,
    "Data-Driven Decision Making": 89,
    "Critical Thinking": 88
}

for skill, level in business_skills.items():
    st.write(f"**{skill}**")
    st.progress(level / 100)


# Education
st.header("🎓 Education")
st.write("""
**📍 The University of Texas at Arlington**  
- **Degree:** Bachelor of Science in Business Analytics  
- **Minor:** Information Systems  
- **Expected Graduation:** May 2025  
""")


st.write("---")

# Contact Form with CSV Storage
st.header("📬 Contact Me")
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

def save_message(name, email, message):
    new_message = pd.DataFrame([[name, email, message]], columns=["Name", "Email", "Message"])
    
    if os.path.exists("messages.csv"):
        existing_messages = pd.read_csv("messages.csv")
        updated_messages = pd.concat([existing_messages, new_message], ignore_index=True)
    else:
        updated_messages = new_message
    
    updated_messages.to_csv("messages.csv", index=False)

if st.button("📩 Send Message"):
    if name and email and message:
        save_message(name, email, message)
        st.success("✅ Message saved! Thank you for reaching out, I'll get back to you ASAP")
    else:
        st.warning("⚠️ Please fill out all fields before sending.")

# Display Messages Inside the Website
if os.path.exists("messages.csv"):
    st.write("📩 **View Received Messages**")
    df = pd.read_csv("messages.csv")
    st.dataframe(df)

st.write("© 2025 Juan Pablo Perez Flores | All Rights Reserved")