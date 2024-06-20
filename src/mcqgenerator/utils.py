# pylint: disable=import-error
"""
This module provides functionality to interact with AI21 API and initialize an agent for task execution.
"""

import os
import PyPDF2
import json
import traceback


def read_file(file):
    """
    Reads the contents of a file and returns it as a string.
    
    Args:
        file: The file to be read.
        
    Returns:
        The contents of the file as a string.
        
    Raises:
        Exception: If the file format is not supported (only PDF and text files are supported).
    """
    if file.name.endswith(".pdf"):
        try:
            # Create a PyPDF2 reader object
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            # Iterate over each page in the PDF file
            for page in pdf_reader.pages:
                # Extract the text from the page and append it to the main text
                text += page.extract_text()
            return text
            
        except Exception as e:
            # Raise an exception if there's an error reading the PDF file
            raise Exception("error reading the PDF file: " + str(e))
        
    elif file.name.endswith(".txt"):
        # Read the contents of the text file and return it as a string
        return file.read().decode("utf-8")
    
    else:
        # Raise an exception if the file format is not supported
        raise Exception(
            "unsupported file format only pdf and text file suppoted"
            )

def get_table_data(quiz_str):
    
    try:
        if isinstance(quiz_str, str):
            quiz_dict = json.loads(quiz_str)
        else:
            quiz_dict = quiz_str
            
        quiz_table_data = []
        
        # Iterate over each item in the quiz dictionary
        for key, value in quiz_dict.items():
            # Extract the MCQ and options from the dictionary
            mcq = value["mcq"]
            options = " || ".join(
                [
                    f"{option}-> {option_value}" for option, option_value in value["options"].items()
                ]
            )
            
            # Extract the correct answer from the dictionary
            correct = value["correct"]
            # Create a dictionary to store the quiz data in a table format
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
        
        return quiz_table_data
        
    except Exception as e:
        # Print the exception traceback if there's an error parsing the quiz dictionary
        traceback.print_exception(type(e), e, e.__traceback__)
        return False