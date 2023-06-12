
https://github.com/ademarc/langchain-ask-csv-data/assets/125093622/038f9c9b-308b-4b1d-8f75-35eb9ff43a29

# Ask Your CSV Data

This is a web application that allows you to upload CSV files and ask questions about the data in those files. The application uses the OpenAI language model to generate responses to your questions.

## Installation

1. Clone this repository by running `git clone https://github.com/ademarc/langchain-ask-csv-data.git`.
2. Install the necessary packages by running `pip install -r requirements.txt`.
3. Set your OpenAI API key as an environment variable. You can do this by creating a `.env` file in the same directory as the script, with the following content:
    ```
    OPENAI_API_KEY=your_api_key_here
    ```

## Usage

1. Start the app by executing `streamlit run main.py`.
2. Open your web browser and go to `http://localhost:8501`.
3. Upload your CSV files and ask a question about the data in those files.

## .env.sample

This file is a template for the `.env` file you need to create. It should look like this:
    ```
    OPENAI_API_KEY=your_api_key_here
    ```
Replace `your_api_key_here` with your actual OpenAI API key.

## License

This project is licensed under the terms of the MIT License.

## Author

This project was created by Marcus Adebayo.
