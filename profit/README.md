

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains a variety of files and folders with different purposes. It includes files for setting up an agent that can perform various tasks, such as reading and writing files, processing CSV data, querying websites, and interacting with humans. There are also files for running an email drafting process, creating a chat interface using the Clarifai API, generating text using a pre-trained language model, and implementing a chat interface using Streamlit. Additionally, there are files for a conversational agent template for sales purposes, a collection of tools and functions for data processing and web scraping, and several Python scripts for web scraping and data parsing.


### `__init__.py`

📝 This file is likely to be part of a larger project or system.


### `agent.py`

📝 This file contains the definition of a class called "Agent".
💡 The purpose of the file is to set up an agent that can perform various tasks.
🔧 The agent can use a set of tools, including reading and writing files, processing CSV data, querying websites, and interacting with humans.
🧠 The agent has a memory component that uses embeddings and a vector store for retrieval.
🤖 The agent is based on the AutoGPT model and can be run with a task.
💼 The agent can be customized with a name, role, and external tools.
🚀 The agent is designed to be used as part of a larger system or framework.
⚠️ Errors may occur during the setup or execution of the agent, which will be raised as exceptions.
📞 The agent can be called as a function and passed a task to run.
📚 The file also includes some imports and a root directory constant.


### `email_drafter`

This folder contains three files: `email_generator.py`, `gmail.py`, and `run.sh`. 

- `email_generator.py` is responsible for running an email drafting process using the OpenAI GPT-3.5 Turbo model. It extracts domain names from URLs, generates draft emails using the OpenAI model, and sends the draft emails using subprocesses.
- `gmail.py` creates and inserts draft emails using the Gmail API. It requires authentication, uses command line arguments to provide email content and recipient information, and interacts with the Gmail API to create drafts.
- `run.sh` is an empty file.


### `llama.py`

📝 This file is a Python script that sets up a chat interface using the Streamlit library and the Clarifai API for natural language processing. The purpose of the script is to allow users to interact with the Clarifai model and get responses based on their input messages.


### `llama2.py`

📝 This file contains a Python class called "LLama2".
🔧 The purpose of this class is to generate text using a pre-trained language model.
🔌 It uses the Hugging Face "transformers" library for language model loading and tokenization.
💡 The class constructor allows for customization of the model, device, maximum text length, and quantization.
⚙️ The "__call__" and "generate" methods can be used to generate text given a prompt.
🔑 The generated text is returned as a string.
📚 If there is an error in loading the model or generating the text, an exception is raised.
🔒 The class is currently commented out, so it is not being used.
👉 To use the class, uncomment the code at the bottom and create an instance of "LLama2".
🔡 Call the "generate" method on the instance, passing a prompt text to generate text.


### `llamachat.py`

📝 The file is a Python script implementing a chat interface using Streamlit.  
🤖 It uses the "streamlit_chat" library for displaying messages.  
📧 It also imports functions for generating marketing reports and emails.  
🐪 The main class is "LlamaClarifaiChat" which initializes the chat session and handles user prompts.  
💬 User prompts are processed using the "llama" module to generate a response.  
📝 The chat history is stored in the "messages" list in the session state.  
✨ The chat interface is rendered using Streamlit components.  
🔘 Users can input messages and send them by clicking the "Send" button.  
🗑️ There is a "Clear Chat" button to reset the chat history.  
📊 There is also a method for generating prospect reports, but it is not currently used.


### `main.py`

📝 This file contains a class called "ProfitPilot" that serves as a template for a conversational agent. 
📝 The agent is designed to engage in sales conversations with potential customers, following a predefined script.
📝 The class has various attributes that store information about the agent, the company, and the ongoing conversation.
📝 The "run" method is responsible for running the agent and generating responses based on the given task.
📝 The agent utilizes an external tool called "Agent" to handle the conversation logic and generate appropriate responses.
📝 The generated responses are printed to the console.
📝 The file includes a system prompt that provides instructions and examples for the agent's behavior during different stages of the conversation.
📝 The system prompt also includes a conversation history and a placeholder for the salesperson's name.
📝 The purpose of this file is to define the structure and behavior of the conversational agent for sales purposes.
📝 The file can be further extended and customized to create specific instances of the conversational agent.


### `tools.py`

💡 This file contains a collection of tools and functions for data processing, scraping web data, and generating email drafts.
💡 It uses various libraries and modules such as pandas, BeautifulSoup, Playwright, and Pydantic.
💡 The file includes tools for processing CSV files, scraping data from websites, and drafting emails.
💡 It also includes a tool for browsing web pages and retrieving relevant information based on a question.
💡 The file uses context managers for changing the current working directory and has some utility functions.
💡 It imports modules from the langchain package and defines a few classes and functions specific to that package.
💡 The file includes an asynchronous function for loading web pages using Playwright and BeautifulSoup.
💡 It defines a tool for querying web pages and retrieving information using a question-answer chain.
💡 The file also includes a tool for searching the web using DuckDuckGo and a toolkit for interacting with Zapier's NLA API.


### `webscraper`

This folder contains several Python scripts for web scraping and data parsing. The "main.py" script uses the SeleniumWire library to collect data from a target URL, while the "parse_data.py" script is used for parsing information from an HTML file. The "scraper.py" script is another web scraping script that uses Selenium Wire, and the "setup.bat" file is empty.

<!-- Living README Summary -->