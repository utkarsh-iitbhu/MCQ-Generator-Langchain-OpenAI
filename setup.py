# pylint: disable=missing-module-docstring
from setuptools import find_packages, setup

setup(
    name='sahu-mcqgenerator',
    version='0.0.1',
    author='Utkarsh Kumar Sahu',
    author_email='utkarsh.bhuiit@gmail.com',
    install_requires=['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
    
)