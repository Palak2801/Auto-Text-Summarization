# Auto-Text-Summarization
-> Auto Text Summarization is the technique of producing a concise summary while preserving key information and overall meaning.
-> Text summarization will reduce the reading time and will help in finding more information in less time by extracting only relevant information, and
facilitate better retrieval of information

The project contains 4 separate Interfaces:
1.) Home Page Interface
2.) Simple Input Textbox Interface
3.) Url Interface
4.) Document File Interface

-> TextBox Summary interface: It provides Graphical User Interface to end users to summarise the text entered in input text box.
-> URL Summary interface: It provides Graphical User Interface to end users to summarise the whole text content of a webpage by using the site’s URL.
-> Document Text Summary interface: It provides Graphical User Interface to end users to summarise the text present in Document file.

There are total four files -> 
spacy_summaization.py : This script file contains the functionality to summarize text using NLP sPacy library. File follows Text Rank Algorithm to summarize the text.
main_gui_file.py : This python file contains program to create all the interfaces
About Us.txt : File contains overview of us and our project
Help.txt : File contains detail/description of project 

-> There are three different directories containing images of their respective interfaces

-> Requirements:
1.) Python version 3.9.4
    Download directly from https://www.python.org/downloads/
2.) spacy version 3.4.1
    pip install -U spacy
    pip install -U setuptools wheel
    python -m spacy download en_core_web_sm
3.) tkinter version 8.6
4.) BeautifulSoup4 version 
    pip install BeautifulSoup4
5.) Create an empty folder "Documents"
