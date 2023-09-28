

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains files and folders related to various functionalities. It includes files for running the ProfitPilot program, an autonomous agent, email drafting, a chat interface, text generation, and web scraping. The files serve different purposes such as initializing and configuring the program, managing conversations with prospects, generating email drafts, providing a chat interface with an AI assistant, and performing data processing and web scraping tasks.


### `__init__.py`

📝 This file is the entry point for running the ProfitPilot program.
🔍 It imports the ProfitPilot class from the profit.main module.
🤖 It also imports the Agent class from the profit.agent module.
💼 The purpose of this file is to initialize and configure the ProfitPilot program.
🚀 It serves as a starting point for executing the ProfitPilot program.
💡 The ProfitPilot program is designed for automated trading.
📈 It utilizes the ProfitPilot class to analyze market data and make trading decisions.
👥 The Agent class is used to interact with the trading platform and execute trades.
🔧 This file may contain additional code for setting up the program's environment.
💡 It is important to have a clear understanding of the ProfitPilot program before modifying this file.


### `agent.py`

📝 This file defines a class called "Agent" that represents an autonomous agent. 
🔧 The Agent class is responsible for setting up tools, memory, and the agent itself. 
🚀 The agent can be run by calling the `run` method or by invoking the object as a function. 
📂 The Agent class uses various tools such as reading/writing files, processing CSVs, querying websites, etc. 
🔍 It also utilizes an embedding model and a vector store for memory retrieval. 
💡 The agent can be configured to work with or without human input in the loop. 
👥 The agent's purpose is to perform tasks using the provided tools and external tools if any. 
⚠️ Any errors encountered during setup or execution are raised as runtime errors.


### `email_drafter`

This folder contains three files: `email_generator.py`, `gmail.py`, and `run.sh`. 

`email_generator.py` is a script that generates email drafts using the OpenAI ChatCompletion API. It reads input data, splits it into chunks, and processes the result. The extracted information is written to an output file and used to send a draft email using `gmail.py`.

`gmail.py` is a script that creates and inserts a draft email using the Gmail API. It handles authentication and authorization, and takes command-line arguments for the draft email subject, user email, and content. It interacts with the Gmail API to create a draft email.

`run.sh` is an empty file.


### `llama.py`

📄 This file is a Python script that implements a chat interface using the Streamlit library. It allows users to have a conversation with an AI assistant powered by the Clarifai API. The assistant can process user prompts and provide responses based on the input. The script handles user authentication, sets the necessary IDs and URLs, and makes API calls to Clarifai to retrieve predictions based on user input. The chat interface is rendered using Streamlit, and messages are stored in the session state to maintain the conversation history.


### `llama2.py`

📝 This file defines a class called "LLama2" which is used for text generation using a pre-trained language model.
🔎 The purpose of this file is to provide a convenient interface for generating text using the "LLama2" model.
🤖 The "LLama2" class takes care of loading the model and tokenizer, setting up the device (GPU if available), and handling any errors that may occur.
⌨️ The class has two main methods: "__call__" and "generate", both of which can be used to generate text given a prompt.
🔠 The generated text can be controlled by specifying the maximum length of the output.
🚀 The class uses the Hugging Face library "transformers" to work with the pre-trained model and tokenizer.
💡 The class also supports quantization, which can be enabled by setting the "quantize" parameter to True.
🔧 The class provides a default model ID, but a custom model ID can be specified as well.
❗️ If any errors occur during model loading or text generation, an error message is logged and an exception is raised.
⚠️ Currently, the code is commented out, so it is not being executed.


### `llamachat.py`

📝 This file contains a Python script for a chat application called "LlamaClarifaiChat".
📱 The purpose of the script is to create a chat interface where users can interact with an assistant.
💬 Users can enter messages and receive responses from the assistant.
📨 The assistant's responses are generated using the "llama" module.
🔒 The chat history is stored in the session state to maintain conversation continuity.
🔄 The chat interface automatically updates with new messages.
🗑️ Users have the option to clear the chat history.
📊 There is a method for generating a prospect report, but it is not currently being used.
📚 The script imports various modules for Streamlit, chat functionality, email drafting, and more.
👀 The script is executed when the module is run as the main file.


### `main.py`

📝 This file defines a class called "ProfitPilot" which is used for managing conversations with potential prospects in a sales context. 
🗂️ It contains various attributes related to the AI agent, company information, conversation details, and salesperson details. 
🔍 The class has a method called "run" which executes a task using an Agent object from the "profit.agent" module. 
📝 The purpose of this file is to provide a framework for handling sales conversations and generating appropriate responses based on the stage of the conversation and previous history. 
📝 It also includes a system prompt with guidelines for the salesperson, example conversations, and instructions for generating responses. 
📝 The file is designed to be used as part of a larger system or application for sales automation and lead generation.


### `tools.py`

📝 This file contains a Python script that serves as a toolset for data processing, web scraping, and email drafting. 
🔍 It imports various libraries and modules for different functionalities. 
🔧 The script defines several functions that can be used as tools, such as processing CSV files, scraping data from websites, and drafting emails. 
🌐 It also includes tools for browsing web pages, querying web pages for specific information, and performing web searches. 
📚 The script utilizes external tools and libraries like LLama2, Selenium-wire, BeautifulSoup, and Playwright. 
🔑 It requires authentication for using the Zapier NLA API. 
💼 The script is designed to be a comprehensive toolset for various data-related tasks. 
📂 The root directory for data operations is "./data/". 
🔧 The functions are wrapped as tools using decorators for easy usage. 
⚠️ Some parts of the script may require additional configuration or setup before they can be used.


### `webscraper`

This folder contains Python scripts for web scraping and data parsing. The main script, "main.py", uses the SeleniumWire library to scrape data from web pages in either "scout" or "collect" mode. The "parse_data.py" script uses the BeautifulSoup library to extract information from HTML files and writes the extracted data to separate text files. The "scraper.py" script provides functions for scouting request URLs, grabbing responses, and collecting data. The "setup.bat" file is empty.

<!-- Living README Summary -->