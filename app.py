import streamlit as st

# Page Setup
st.set_page_config(
    page_title="Student Profile Website",
    page_icon="🎓",
    layout="centered"
)

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

        Hello **{name}**!  
        Wishing you great success in your studies at **{college}**.

        Keep learning, keep growing, and keep building your future! 🚀✨
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