
import streamlit as st

st.set_page_config(page_title="Yashawini Chandrasekar — Portfolio", page_icon="💻", layout="wide")

# --- Header ---
st.title("Yashawini Chandrasekar")
st.subheader("Aspiring AI Enthusiast | 4× AWS Certified | AWS Solution Architect | AWS ML Associate")
st.write("📍 Chennai, Tamil Nadu, India")
st.write("✉️ yashawini.chandrasekar@gmail.com")

st.markdown("---")

# --- About ---
st.header("About Me")
st.write("""
Aspiring to become an AI Enthusiast with strong foundation in cloud technologies (AWS), 
machine learning, and software development. Passionate about solving real-world problems 
through AI and cloud-based solutions.
""")

# --- Education ---
st.header("Education")
st.write("🎓 **Bachelor of Engineering, Computer Science** — St. Joseph's College Of Engineering (2023 – 2027)")
st.write("🎓 **HSE, Computer Science** — Chettinad Vidyashram (2021 – 2023)")

# --- Experience ---
st.header("Experience")
st.subheader("💻 AI Intern — RETECH Solutions Pvt Ltd (Jul 2024, Chennai)")
st.write("15-day AI Architect internship with hands-on experience in AI model development, "
         "machine learning algorithms, and optimizing AI solutions.")

# --- Skills ---
st.header("Skills")
cols = st.columns(2)
with cols[0]:
    st.write("• Java")
    st.write("• Python")
    st.write("• C")
    st.write("• SQL")
with cols[1]:
    st.write("• AWS (Cloud Practitioner, Solutions Architect, AI Practitioner, ML Associate)")

# --- Certifications ---
st.header("Certifications")
st.write("• AWS Certified Machine Learning Engineer – Associate (Jun 2025 – Jun 2028)")
st.write("• AWS Certified AI Practitioner (Apr 2025 – Apr 2028)")
st.write("• AWS Certified Solutions Architect – Associate (Feb 2025 – Feb 2028)")
st.write("• AWS Certified Cloud Practitioner (Mar 2024 – Mar 2027)")
st.write("• Data Visualization with Python (Skillsoft, Jun 2025)")
st.write("• MongoDB Basics for Students (MongoDB, Jun 2025)")

# --- Contact ---
st.markdown("---")
st.header("Contact")
st.write("✉️ Email: yashawini.chandrasekar@gmail.com")
st.write("🔗 LinkedIn: [Profile](https://www.linkedin.com/in/yashawini-chandrasekar-abb847218)")

st.markdown('<div style="text-align:center; color:gray; margin-top:30px;">'
            'Portfolio generated with Streamlit | Edit on GitHub to customize'
            '</div>', unsafe_allow_html=True)
