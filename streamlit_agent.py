import streamlit as st
from streamlit_extras.let_it_rain import rain
from openai_code import generate_code
from code_editor import run_code

st.title("Code-Agent")

code_prompt = st.text_area("Enter Your Prompt: (ctrl + enter to submit)")
st.write(f"You wrote {len(code_prompt)} characters.")

language_prompt = st.text_input("Enter Your Language: ")

with st.container():
    if st.button("Generate Response"):
        with st.spinner("Generating response..."):
            if not code_prompt.strip() or not language_prompt.strip():
                st.error("Please provide both a code prompt and a programming language.")
                st.stop()

            response = generate_code(code_prompt)

            st.subheader("Code Response:")
            st.code(response, language=language_prompt.lower())

            st.balloons()


st.divider()

st.subheader("Run Python Code")
code_input = st.text_area(
    "Enter Your Code: (ctrl + enter to submit)",
    key="code_editor",
    height=200
)

if st.button("Run Code"):
    with st.spinner("Running code..."):
        if not code_input.strip():
            st.error("Please provide code to run.")
            st.stop()

        output, error = run_code(code_input)

        if output:
            st.subheader("Output:")
            st.code(output, language='python')

            st.balloons()

        if error:
            st.subheader("Error:")
            st.code(error, language='plaintext')

            rain(emoji="💥", font_size=54, falling_speed=8, animation_length=5)
