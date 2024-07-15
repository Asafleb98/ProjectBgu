import streamlit as st
from multipage import MultiPage
from pages import student, teacher

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Evanti Project")

# Add all your applications (pages here)
app.add_page("Student", student.app)
app.add_page("Teacher", teacher.app_with_password)

# Run the main app
app.run()
