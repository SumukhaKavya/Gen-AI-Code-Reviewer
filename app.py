import streamlit as st
from openai import OpenAI

# Read API key from file
with open(r"key.txt", "r") as f:
    OPENAI_API_KEY = f.read()

client = OpenAI(api_key=OPENAI_API_KEY)

# Set colored page title
st.title("An AI Code Reviwer")

# User input section
prompt = st.text_area("Enter your Python code here:", height=200)

# Button to trigger code review
if st.button("Generate"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "user", "content": "Review the given python code and Generate what are the list of mistakes in the code and give fixed code by correcting the code"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    # Display the generated text
    generated_text = response.choices[0].message.content
    st.write(generated_text)
