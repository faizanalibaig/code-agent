import streamlit as st
from openai_code import generate_code

st.title("Code-Agent")

code_prompt = st.text_area("Enter Your Prompt: (ctrl + enter to submit)")
st.write(f"You wrote {len(code_prompt)} characters.")

language_prompt = st.text_input("Enter Your Language: ")


if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        response = generate_code(code_prompt)

        st.subheader("Code Response:")
        st.code(response, language=language_prompt)
