import streamlit as st
import time
import pandas as pd

# Add an image above the title
# Ensure 'profile.jpg' is in the same directory as this script
st.image("bud.jpg", use_column_width=True)

# Title and Subtitle
st.title("My Autobiography & Portfolio")
st.subheader("Welcome to my personal page!")

# Autobiography Section
st.header("Autobiography")
st.write("""
Hello, I'm Rickshel Brent B. Ilustrisimo, a dedicated web developer with a strong enthusiasm for building user-friendly and meaningful web applications. Residing on Santa Fe, Bantayan Island, Cebu, I developed a love for technology early on. I am now a fourth-year BSIT student at Cebu Institute of Technology University, where I have refined my skills.
""")

# Adding a Divider
st.markdown("---")

# Portfolio Section
st.header("Portfolio")

# Project 
st.subheader(" Project: Library Management System")
st.write("""
Developed a full-stack Library Management System using Spring Boot and React. The system includes features like 
user authentication, book reservations, and administrative controls. Integrated MySQL for database management and 
used Docker for containerization.
""")

# Adding a Contact Form with your information
st.header("Contact Me")
st.write("Feel free to reach out to me through the information below:")

# Displaying contact information
st.write("**Name:** Rickshel Brent B. Ilustrisimo")
st.write("**Email:** brentilustrisimo13@gmail.com")
st.write("**Contact no:** 09212330825")

# Adding Social Media Links
st.header("Find me on Social Media")
st.write("""
- [Facebook](https://web.facebook.com/buddy.ilustrisimo.7)
- [GitHub](https://github.com/Rickshel)
""")

# Adding an Expander Section for Skills
st.header("Skills")
with st.expander("Frameworks & Libraries"):
    st.write("""
    - Spring Boot
    - React
    - Streamlit
    """)
with st.expander("Programming Languages"):
    st.write("""
    - Python
    - JavaScript
    - Java
    """)
