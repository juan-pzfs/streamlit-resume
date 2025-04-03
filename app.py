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
I’m a data professional with a passion for **transforming raw data into clarity, insight, and action**.  
With hands-on experience in **automation, dashboard development, and structured data pipelines**,  
I’ve helped organizations optimize decision-making and improve reporting workflows.

My strengths lie in building **end-to-end solutions**—from **data extraction and cleaning** in Python and SQL,  
to **visualizing key metrics in Power BI** and creating scalable workflows using tools like **Knime and Selenium**.  
I’ve even built a chatbot that pulls real-time sports data from a SQL database, combining **user-friendly design** with automation.

I’m a fast learner and love jumping into new tools, teams, or challenges.  
Whether it's contributing to a high-level BI project or engineering clean, usable datasets,  
I bring **adaptability, precision, and a builder's mindset** to every role.

If you’re looking for someone who can **collaborate across teams**, think critically, and help turn  
complex data into results that matter—I’d love to bring that energy and skillset to your team.
""")


st.write("---")


# Work Experience Section
st.header("💼 Work Experience")

with st.expander("📊 Supply Chain Data Analyst Intern - CHRISTUS Health"):
    st.write("📅 **June 2023 - Present | Irving, TX**")
    st.write("")  # Forces a line break
    st.write("""
    During my internship at CHRISTUS Health, I worked on **optimizing data workflows and automating reporting processes**  
    to support supply chain operations across Latin America. I collaborated closely with **supply chain managers, finance teams,  
    and regional executives** to understand reporting needs and streamline critical processes.  

    I developed **Python scripts** that automated data extraction for **20,000+ medical supplies**, replacing manual workflows  
    and reducing processing time by **94%**. I also cleaned and structured **150,000+ records** using **SQL and Python**,  
    improving data reliability for strategic analysis.  

    To increase visibility for executive leadership, I built an **automated Power BI dashboard** that visualized  
    KPIs such as **cost savings over time, inventory turnover rates, and inflation-adjusted price trends**.  
    This dashboard pulled from Excel reports using scheduled refreshes, ensuring real-time updates with minimal maintenance.  

    I also led process automation projects using **Python and Knime**, helping convert manual analysis that previously took  
    several hours into workflows that now run in **just minutes or seconds**. These solutions are actively used by the team today.  

    In addition to development, I presented insights and dashboard walkthroughs to **non-technical stakeholders**,  
    simplifying metric interpretation and encouraging broader adoption across departments.  

    This experience strengthened my ability to work in **fast-paced, cross-functional environments**,  
    and to deliver **data-driven tools that directly improve operational efficiency**.
    """)

with st.expander("📁 Lead Student Worker - University of Texas at Arlington"):
    st.write("📅 **Feb 2021 - June 2023 | Arlington, TX**")
    st.write("")  # Forces a line break
    st.write("""
    At UTA’s Office of International Education, I managed and maintained **student immigration records**  
    for over **4,000 students**, ensuring data accuracy and compliance with internal standards.  
    I created and maintained an **Excel-based tracking system** to monitor long-term document storage and pickup,  
    which helped the office track outstanding records and notify students more efficiently.  

    The system became the central database for recordkeeping, and I ensured it stayed updated and correctly formatted  
    for daily use. I also helped onboard and train new student workers, guiding them on data entry best practices  
    and consistency in handling sensitive information.  

    This role strengthened my ability to **design structured processes**, handle **high-volume data**, and  
    support operational efficiency in a **dynamic, team-driven environment**.
    """)

st.write("---")

# Projects Section
st.header("📊 Projects")

with st.expander("📌 Catalog Number Detection with KNN – Python, Pandas, ML"):
    st.write("""
    As part of my internship at CHRISTUS Health, I collaborated with the data team to develop  
    a **Python-based machine learning script** that detects **product catalog numbers** from unstructured text  
    in product descriptions. The project used **tokenization and rule-based scoring** to identify patterns,  
    followed by a **K-Nearest Neighbors (KNN) classifier** to determine whether a token was a valid catalog number.  

    The model achieved **92% accuracy** on large-scale testing (100,000+ records), significantly improving  
    the process of catalog number extraction from Excel-based product data. The output was used in follow-up  
    data enrichment pipelines and replaced a manual step that had previously required substantial time and effort.  

    This was my first hands-on experience applying **machine learning in Python** and collaborating directly  
    with a professional data analyst, giving me valuable exposure to **real-world ML workflows and applied problem solving**.
    """)

with st.expander("🔎 Web Scraping for Medical Product Data – Python, BeautifulSoup, Selenium"):
    st.write("""
    As part of my internship at CHRISTUS Health, I developed **two Python-based web scraping scripts**  
    to collect **medical product information** from two distinct online sources. Using **BeautifulSoup** for  
    a static website and **Selenium** for a more interactive site with dynamic elements, I extracted data  
    such as **product descriptions, manufacturers, prices, device identifiers, and supplier information**.  

    The scraping process used a **list of 50,000 catalog numbers**, dynamically generating URLs or automating  
    search queries depending on the site structure. The extracted data was **cleaned and consolidated into Excel**,  
    where it was later prepared for upload into **Informatica** for broader data integration.  

    This project deepened my experience with **web automation, dynamic content handling, and exception-based debugging**,  
    especially in cases where websites introduced unique formatting or unexpected behavior. It significantly  
    reduced the manual effort previously required to compile this data, improving speed, accuracy, and consistency  
    in the data enrichment pipeline.
    """)

with st.expander("📊 Latin America Supply Chain Dashboard – Power BI, DAX, SharePoint"):
    st.write("""
    As part of my internship at CHRISTUS Health, I was tasked with redesigning an underperforming  
    **Power BI dashboard** used to track supply chain project performance across **Chile, Colombia, and Mexico**.  
    The original dashboard was slow and cluttered with unused datasets, so I conducted a full **data model overhaul**,  
    rebuilding it from scratch and improving its reliability and responsiveness.  

    I restructured the **entity relationship diagram**, removed unnecessary tables, and rewrote complex metrics  
    using **DAX** to improve formula efficiency and accuracy. The dashboard integrated data from both  
    **Excel spreadsheets and SharePoint sources**, requiring consistent dataset updates and validation.  
    I ensured accuracy by cross-validating all key financial metrics—such as **savings, inflation adjustments,  
    increase over inflation, and total project costs**—against the original dashboard.  

    The final version is now used by the **Supply Chain team** to evaluate **project-level financial impacts**,  
    and is actively reviewed by **international leadership** for strategic decision-making across regions.
    """)

with st.expander("📄 Document Translator Script – Python, deep-translator"):
    st.write("""
    As part of my internship at CHRISTUS Health, I developed a small **Python script** using the  
    `deep-translator` library to automate the translation of **project-related documentation**  
    from English to Spanish. The translated content was later used in a **presentation for the Supply Chain team**  
    and international stakeholders.  

    While this was a one-time task, it demonstrated how scripting could eliminate repetitive translation work,  
    saving time and ensuring consistency for internal communications.
    """)

with st.expander("🔁 Price Discrepancy Detection Workflow – KNIME, Python, Excel"):
    st.write("""
    As part of a collaborative intern project at CHRISTUS Health, I co-developed a **KNIME workflow**  
    that automated **price discrepancy analysis** across thousands of medical supply records.  
    The workflow integrated **7 Excel datasets** (totaling over **500,000 rows**) and performed  
    **data cleaning, merging, and preprocessing** using both **KNIME visual workflows** and embedded **Python scripts**.  

    My main contribution involved building the **Python script** used for the analysis portion of the pipeline.  
    It compared current product prices against negotiated vendor pricing to identify discrepancies,  
    calculate price differences, and flag inconsistent entries. The final output was a structured Excel report  
    of **50,000+ rows**, highlighting mismatches with calculated percentage differences for internal auditing.  

    This solution is now used regularly by the **Supply Chain team in Chile** and is being expanded to support  
    **Mexico and Colombia**. The workflow has helped **streamline price validation**, allowing the team to  
    reallocate time to higher-priority tasks and strengthen vendor compliance monitoring.
    """)

with st.expander("📥 Informatica Upload for Item Master – Python, Excel, Informatica"):
    st.write("""
    At CHRISTUS Health, I used **Informatica** to upload structured medical product data into our  
    centralized **item master**, based on outputs generated from earlier projects including the  
    **KNN catalog detection script** and **web scraping workflows**.  

    I prepared data in a standardized **CSV format** that followed strict metadata templates,  
    ensuring compatibility with Informatica’s upload process. This task was repeated multiple times  
    across large datasets to progressively update catalog entries.  

    Through this process, we helped improve the **catalog identification rate** in the item master  
    from **46% to 67%**, significantly increasing visibility, traceability, and data quality  
    for product records across the organization.
    """)

with st.expander("📦 Inventory Tracking & Overstock Analysis – Python, Data Normalization"):
    st.write("""
    At CHRISTUS Health, I developed a **Python-based workflow** to automate monthly **inventory analysis**  
    for warehouse data across Chile. Each month, I received inventory records in **.txt format**,  
    totaling up to **100,000 records per file**, and converted them into normalized **CSV files**  
    by adjusting thousands and decimal separators from Latin American to U.S. formatting standards.  

    After preprocessing, I merged at least **13 months of historical inventory data** to run movement-based  
    analysis. The logic classified each item as **slow-moving, regularly moving, or overstocked**  
    based on its historical movement across the past year. The final output included structured tables  
    detailing product quantities and values for each category.  

    This analysis is used by the **Supply Chain team** in Chile whenever a report is needed for a specific warehouse,  
    helping them identify excess stock and optimize supply chain efficiency.
    """)

with st.expander("🤖 Facial Recognition Classification – Orange Analytics, ML"):
    st.write("""
    In a team-based project for my Intro to Business Analytics course, I helped develop  
    a **facial recognition model** using **Orange Analytics** to classify images of  
    **Cillian Murphy, Emma Stone, and Matt Damon**. The objective was to compare various  
    **machine learning algorithms** and optimize performance through iterative tuning.  

    We tested and evaluated models including **KNN, Decision Tree, Logistic Regression,  
    Random Forest, and Neural Networks**, measuring performance using **AUC scores** and  
    **confusion matrices**. After adjusting parameters and refining the model,  
    our best-performing algorithm achieved an accuracy of **92%**.  

    This project provided a strong foundation in **classification modeling, performance evaluation,**  
    and practical machine learning experimentation in a visual workflow environment.
    """)

with st.expander("📊 Gender Pay Gap Analysis – SQL, Tableau"):
    st.write("""
    As part of my Data Visualization course, I conducted a solo project analyzing the **gender pay gap**  
    across multiple professional fields using a dataset of over **15,000 salary records**. Using **SQL**,  
    I performed exploratory data analysis to identify discrepancies in compensation based on gender,  
    and segmented the data by industry, occupation, and academic background.  

    After uncovering meaningful trends, I used **bar charts in Tableau** to visualize patterns such as  
    **pay gap differences**, **popular majors by gender**, and potential correlations between workforce  
    composition and compensation disparity. One key insight showed that **industries dominated by one gender  
    tend to have a slight pay advantage for that gender**, while more gender-balanced fields had a smaller gap overall.  

    The final deliverable was a **written report** summarizing my findings and visualizations, demonstrating  
    my ability to connect **data storytelling** with **business and social insights**.
    """)

with st.expander("🏦 Home Credit Risk Prediction – Python, Scikit-Learn, XGBoost"):
    st.write("""
    In a team project for my Data Science class, I helped build a **machine learning model**  
    to predict whether loan applicants would repay or default, using a dataset of over **12,000 records**.  
    The goal was to help financial institutions assess **credit risk** by developing a reliable  
    classification pipeline from end to end.  

    We used **Python with Scikit-learn, XGBoost, and imbalanced-learn** to handle data cleaning,  
    preprocessing, feature engineering, and model training. I also performed **EDA** using **Seaborn**  
    and **Matplotlib** to uncover correlations and guide our feature selection.  

    Our final model achieved **74% accuracy**, and the process helped reinforce key concepts  
    around **model evaluation, class imbalance, and predictive analytics**.  
    This hands-on experience clarified several complex data science techniques  
    and strengthened my confidence working with real-world machine learning problems.
    """)

with st.expander("⚽ AI-Powered Soccer Chatbot – Botpress, Web Integration"):
    st.write("""
    I developed an **AI-powered chatbot** using **Botpress** to provide real-time insights  
    on **European soccer leagues, teams, and players**. Users could ask about  
    **league standings, top scorers, or upcoming fixtures**, and the chatbot would retrieve  
    current information from **external websites**, depending on the league requested.  

    I designed automated workflows within Botpress to create **structured, user-friendly conversations**,  
    allowing users to naturally navigate and access data based on their queries. The system dynamically  
    pulled the latest information from public web sources, keeping responses accurate and relevant.  

    This project strengthened my skills in **workflow automation**, **real-time data integration**,  
    and designing chat interfaces that bridge **user questions with live web data** — showcasing how AI  
    can be applied to build engaging and useful tools for sports fans.
    """)

with st.expander("🧠 Trust in AI: Student Sentiment Study – Python, Power BI"):
    st.write("""
    For my senior seminar in Business Analytics, I conducted a **student survey on trust in AI**,  
    gathering over **100 responses** from individuals across campus. The survey measured attitudes  
    toward AI, experience using it, and reactions to common use cases and hallucinations.  

    I cleaned and transformed the data using **Python**, converting qualitative responses into  
    numeric formats for analysis. I then developed an **interactive dashboard in Power BI** to visualize  
    trends across different demographics, such as **major, academic year, and level of AI familiarity**.  

    One key insight showed that **less experienced users tend to overtrust AI**, while those with more  
    hands-on exposure showed greater skepticism — especially after encountering hallucinated outputs.  
    The project culminated in both a **formal report and live presentation**, strengthening my ability to  
    translate survey data into **clear, actionable insights**.
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
    "Data Integration (APIs, CSV, TXT)": 70,
    "Web Scraping (Selenium, BeautifulSoup)": 68,
    "Tableau": 63,
    "SQL": 60,
    "Version Control (Git/GitHub)": 60,
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
    "Data Modeling & Structuring": 73,
    "Survey Data Analysis": 72,
    "Feature Engineering": 70,
    "Classification Algorithms (LogReg, RF, KNN)": 68,
    "Machine Learning": 65,
    "Model Evaluation (AUC, Confusion Matrix)": 65,
    "Time-Series Analysis": 62,
    "A/B Testing & Experimentation": 60
}

for skill, level in statistical_skills.items():
    st.write(f"**{skill}**")
    st.progress(level / 100)

st.write("---")  # Separator

# Business & Soft Skills
st.subheader("📈 Business & Soft Skills")
business_skills = {
    "Adaptability & Learning Agility": 90,
    "Cross-Functional Collaboration": 89,
    "Communication & Data Storytelling": 89,
    "Time Management & Prioritization": 89,
    "Data-Driven Decision Making": 89,
    "Business Process Optimization": 87,
    "Attention to Detail": 86,
    "Presentation & Reporting": 85,
    "Problem-Solving": 85,
    "Critical Thinking": 85
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

# Contact Form - Stores Messages Privately
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
        st.markdown(
            """
            <div style="
                background-color: #DFF6DD;
                padding: 12px;
                border-radius: 8px;
                color: black;
                font-size: 16px;
                font-weight: bold;
            ">
                ✅ Message sent! Thank you for reaching out, I'll get back to you ASAP
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ Please fill out all fields before sending.")


st.write("© 2025 Juan Pablo Perez Flores | All Rights Reserved")