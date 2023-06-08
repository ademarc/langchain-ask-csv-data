from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
import tempfile
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(page_title="Ask your CSV")

hide_streamlit_style = """
            <style>
            
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def process_files(csv_files):
    tmp_file_names = []
    for csv_file in csv_files:
        # Create a temporary file and write the contents of the uploaded file to it
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            tmp.write(csv_file.getvalue())
            tmp_file_names.append(tmp.name)
            data = pd.read_csv(csv_file)
            limited_data = pd.concat([data.head(3), data.tail(2)])
            st.dataframe(limited_data, use_container_width=True)
    return tmp_file_names

def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        st.error("OPENAI_API_KEY is not set")
        return

    st.header("Chat with your CSV Data 📈")
    st.markdown("Please upload one or more CSV files and ask a question about the data.")

    csv_files = st.file_uploader("Upload CSV file(s)", type="csv", accept_multiple_files=True)
    if csv_files:
        tmp_file_names = process_files(csv_files)
        st.success("CSV file(s) uploaded successfully!")

        agent = create_csv_agent(OpenAI(temperature=0), tmp_file_names if len(tmp_file_names) > 1 else tmp_file_names[0], verbose=True)

        user_question = st.text_input("Ask a question about your Data: ")
        submit_button = st.button("Submit")

        if submit_button:
            if user_question.strip() != "":
                with st.spinner(text="In progress..."):
                    result = agent.run(user_question)
                    if result:
                        st.write(result)
                    else:
                        st.error("No result returned. Please check your question.")
            else:
                st.error("Please enter a valid question.")

        # Delete temporary files
        for file_name in tmp_file_names:
            os.remove(file_name)

if __name__ == "__main__":
    main()
