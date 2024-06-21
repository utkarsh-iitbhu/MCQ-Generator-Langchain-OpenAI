# MCQ Creator Application with Langchain

Welcome to the MCQ Creator Application with Langchain. This application uses Langchain and OpenAI to generate Multiple Choice Questions (MCQs) from a given text or PDF document. 

![image](https://github.com/utkarsh-iitbhu/MCQ-Generator-Langchain-OpenAI/assets/84759422/7f6c05c4-f453-4a4c-9087-49011a6cf883)

Voila! You will get your desired set of MCQs generated with a review on the level of difficulty of the MCQs generated as well.

![image](https://github.com/utkarsh-iitbhu/MCQ-Generator-Langchain-OpenAI/assets/84759422/ad0a0743-c533-45b5-9ceb-2c433baad971)


## Features

- Upload a PDF or text file and generate MCQs based on its content.
- Customize the number of MCQs, subject, and complexity level.
- View the generated MCQs in a tabular format.
- Review the generated MCQs directly within the application.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- The following Python packages:
  - `openai`
  - `langchain`
  - `streamlit`
  - `python-dotenv`
  - `PyPDF2`

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/utkarsh-iitbhu/MCQ-Generator-Langchain-OpenAI.git
    cd MCQ-Generator-Langchain-OpenAI
    ```

2. **Set up a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key:**

    Create a `.env` file in the root directory of the project and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```


### Running the Application

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run app.py
```

# MCQ Creator Application with Langchain

Welcome to the MCQ Creator Application with Langchain. This application uses Langchain and OpenAI to generate Multiple Choice Questions (MCQs) from a given text or PDF document. 

## Features

- Upload a PDF or text file and generate MCQs based on its content.
- Customize the number of MCQs, subject, and complexity level.
- View the generated MCQs in a tabular format.
- Review the generated MCQs directly within the application.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- The following Python packages:
  - `openai`
  - `langchain`
  - `streamlit`
  - `python-dotenv`
  - `PyPDF2`

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/utkarsh-iitbhu/MCQ-Generator-Langchain-OpenAI.git
    cd MCQ-Generator-Langchain-OpenAI
    ```

2. **Set up a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -e .
    ```

4. **Set up your OpenAI API key:**

    Create a `.env` file in the root directory of the project and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

### Running the Application

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run app.py
```
This will start the Streamlit server, and you can access the application in your web browser at http://localhost:8501

## Usage

1. **Upload a PDF or txt file:**
   - Click on the "Browse files" button and select the file you want to upload.

2. **Enter the number of MCQs:**
   - Input the desired number of MCQs (between 3 and 50).

3. **Insert the subject:**
   - Enter the subject for the MCQs (maximum 25 characters).

4. **Specify the complexity level:**
   - Enter the desired complexity level of the questions (e.g., Simple, Medium, Complex).

5. **Generate MCQs:**
   - Click on the "Create MCQ" button to generate the MCQs.
   - The generated MCQs will be displayed in a table format along with a review section.

# Thank You !!! 
