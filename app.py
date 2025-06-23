
import streamlit as st
from career_bot import recommend_career

st.title("🎓 AI Virtual Career Counsellor")
st.write("Tell me about your interests, and I'll help suggest a career path!")

user_input = st.text_input("Your Interests:")

if st.button("Recommend Career"):
    if user_input:
        results = recommend_career(user_input)
        st.success(f"Recommended Careers: {', '.join(results)}")
    else:
        st.warning("Please type something about your interests.")
