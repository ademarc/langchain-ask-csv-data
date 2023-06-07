from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
import tempfile

# Set Streamlit page configuration
st.set_page_config(page_title="Ask your CSV")

def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        st.error("OPENAI_API_KEY is not set")
        return

    st.header("Ask your CSV 📈")

    csv_files = st.file_uploader("Upload a CSV file", type="csv", accept_multiple_files=True)
    if csv_files:
        tmp_file_names = []
        for csv_file in csv_files:
            # Create a temporary file and write the contents of the uploaded file to it
            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
                tmp.write(csv_file.getvalue())
                tmp_file_names.append(tmp.name)

        # Pass the path to the temporary file to create_csv_agent
        agent = create_csv_agent(OpenAI(temperature=0), tmp_file_names if len(tmp_file_names) > 1 else tmp_file_names[0], verbose=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question.strip() != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))

if __name__ == "__main__":
    main()
