
import streamlit as st
from streamlit_extras.let_it_rain import rain

# Page Setup
st.set_page_config(
    page_title="Student Profile Website",
    page_icon="🎓",
    layout="centered"
)

theme = st.sidebar.selectbox(
    "Choose Theme",
    ["Dark Mode 🌙","Light Mode ☀️"]
)

if theme == "Dark Mode 🌙":

    st.markdown("""
    <style>
    .stApp{
        background: linear-gradient(135deg,#141E30,#243B55);
        color:white;
    }
    </style>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
    <style>
    .stApp{
        background: linear-gradient(135deg,#f6f9fc,#dbeafe);
        color:black;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🎓 Student Information Website")

st.write("Fill your details below!")

# Inputs
name = st.text_input("👤 Enter your Name")

age = st.number_input(
    "🎂 Enter your Age",
    min_value=1,
    max_value=120
)

college = st.text_input("🏫 Enter your College Name")

course = st.text_input("📚 Enter your Course / Branch")

city = st.text_input("🌍 Enter your City")

# Submit Button
if st.button("Generate Profile 🚀"):

    if name and college and course and city:

        st.success("Profile Generated Successfully!")

        st.markdown(f"""
        ## 🌟 Student Profile

        **Name:** {name}  
        **Age:** {age}  
        **College:** {college}  
        **Course:** {course}  
        **City:** {city}
        

        ### 💬 Personalized Message

        Hello {name}! 🤗 
        
        Listen bestie 😉
        Your GPA is important but your growth matters too.
        You don't need to have your whole life figured out at {age}.
        Just keep learning, keep trying, and keep romanticizing your comeback era ✨
        
        Wishing you great success in your studies at {college}.
        """)

        st.balloons()
        
    else:
        st.warning("Please fill all details.")
    


    

# Footer
st.markdown("---")

st.markdown(
    "<center><h4>Created by ❤️ Kaysha Motiani</h4></center>",
    unsafe_allow_html=True
)
