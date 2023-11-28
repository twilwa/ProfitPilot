

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains a collection of files and folders related to profit maximization, email drafting, language generation, conversation agents for sales calls, and web scraping. The files include modules for profit maximization, an agent class, email drafting scripts, a language model implementation, a conversation agent class, tools for data processing and web scraping, and scripts for web scraping and data extraction. Each file and folder serves a specific purpose, such as providing functionality for profit maximization, generating draft emails, implementing a language model, building a conversation agent for sales calls, and performing data processing and web scraping tasks.


### `__init__.py`

📝 This file is an executive summary of the profit.main and profit.agent modules.
🚀 It serves as an entry point to the ProfitPilot and Agent classes.
✨ The ProfitPilot class provides functionality for profit maximization.
💼 The Agent class represents an agent in the profit maximization process.
💡 This file provides an overview of the main components of the profit maximization system.



### `agent.py`

📝 This file defines a class called "Agent" which represents an autonomous agent.
🤖 The Agent class is responsible for setting up tools, memory, and the agent itself.
🔧 The tools include file reading and writing, CSV processing, website querying, and more.
🧠 The memory is set up using FAISS, an efficient similarity search library.
🔍 The agent uses AutoGPT, a language model, along with the LLama2 framework.
🔀 The agent can be run with a task as input, which triggers the execution of the agent's tools.
⚠️ Errors during setup or execution are handled and raised as runtime errors.
📞 The agent can also be called directly as a function, with a task as input.



### `email_drafter`

This folder contains three files: `email_generator.py`, `gmail.py`, and `run.sh`. 

`email_generator.py` is a Python script that generates a draft email using the OpenAI ChatCompletion API. It imports necessary modules, reads input data from files, and generates an email based on a predefined schema. The generated email is written to an output file and sent as a draft email using a subprocess.

`gmail.py` is another Python script that uses the Gmail API to create and insert a draft email. It imports necessary modules, retrieves user-specific information, and constructs an email message with the provided content. The script can be executed directly to create and insert a draft email.

`run.sh` is an empty file.


### `llama2.py`

📝 This file defines a class called "LLama2" that implements a language model for text generation.
🔧 The class takes in various parameters such as model ID, device, maximum length, and quantization options.
🔍 It uses the Hugging Face library to load a pre-trained language model and tokenizer based on the provided model ID.
🔑 The class has a "__call__" method that generates text based on a given prompt using the loaded model and tokenizer.
⚙️ There is also a "generate" method that performs the same text generation functionality as "__call__".
❌ If any errors occur during model or tokenizer loading, an exception is raised.
✨ The class can be instantiated with different parameters and the "generate" method can be called to generate text.
💡 There are some commented-out code lines that show an example of instantiating the class and generating text.
🧪 Overall, this file provides a convenient interface to generate text using a pre-trained language model.


### `main.py`

📝 This file defines a class called "ProfitPilot" that serves as a conversation agent for sales calls.
📝 The agent has various attributes such as AI name, AI role, company name, company values, conversation type, etc.
📝 The class includes a system prompt that provides guidelines for conducting sales conversations at different stages.
📝 The "run" method of the class uses the "Agent" class from the "profit.agent" module to generate responses based on given tasks.
📝 The generated response is printed to the console.
📝 The purpose of this file is to provide a framework for building a conversational AI agent for sales calls.
📝 The agent follows specific guidelines and principles for effective sales conversations.
📝 It can handle different stages of the conversation, from introduction to objection handling and closing.
📝 The file includes an example conversation history and instructs the agent to respond based on the previous conversation and the current stage.
📝 The executive summary should be concise, providing an overview of the file's purpose and functionality.


### `tools.py`

✨ This file is a Python script that contains various tools and functions for data processing, web scraping, and email drafting.
✨ It imports libraries such as asyncio, os, pandas, and BeautifulSoup.
✨ The file defines functions for processing CSV files using pandas, scraping data from websites, and drafting emails.
✨ It also includes a function for browsing web pages and extracting relevant information.
✨ The script uses tools from the langchain and profit libraries for language processing and data analysis.
✨ There are also tools for interacting with external services such as Zapier and LLama2.
✨ The file includes some helper functions and context managers for managing the working directory and handling exceptions.
✨ Overall, this script provides a collection of tools for various data-related tasks, making it useful for data analysts and web developers.
✨ The script is organized into sections, with each section focusing on a specific tool or functionality.
✨ The code includes comments and docstrings to provide explanations and instructions for using the tools.


### `webscraper`

This folder contains Python scripts for web scraping and data extraction. The `main.py` script uses Selenium and SeleniumWire to scout or collect data from a target URL. The `parse_data.py` script automates the extraction of specific data from HTML content. The `scraper.py` script also performs data collection using SeleniumWire. The `setup.bat` file is currently empty and serves as a placeholder for future content.

<!-- Living README Summary -->