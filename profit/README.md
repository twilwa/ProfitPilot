

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains files for the ProfitPilot program. The `__init__.py` file is the starting point for running the program and creates an instance of the Agent class. The `agent.py` file defines the Agent class, which is responsible for executing trading strategies and managing financial transactions. The `llama.py` file provides a wrapper for the LLama2 language model. The `main.py` file contains the ProfitPilot class, which serves as an agent for conducting sales conversations. The `tools.py` file provides a set of tools for working with data, interacting with web pages, and extracting information from them.


### `__init__.py`

📝 This file contains an executable script for the ProfitPilot program.
🤖 It utilizes the ProfitPilot class from the profit.main module.
💼 The purpose of this file is to create an instance of the Agent class from the profit.agent module.
🔧 The Agent class is responsible for executing trading strategies and managing financial transactions.
💡 This script is the starting point for running the ProfitPilot program.



### `agent.py`

📝 This file defines a class called "Agent" that serves as an interface for an AI agent.
🔧 The agent can be configured with various tools for performing tasks such as reading/writing files, querying websites, sending emails, etc.
🗄️ It uses an in-memory document store and a FAISS index for storing and retrieving embeddings of text data.
🤖 The agent is initialized with a language model (LLama2) and the configured tools.
🏃 The agent can be run with a task as input, which triggers the execution of the specified tools and returns the result.
📚 The file also contains a few helper classes and functions for setting up the tools, memory, and agent.
⚠️ Exceptions are raised if there are errors during the setup or execution of the agent.
🔎 The agent can optionally operate in a "human-in-the-loop" mode, where human input is incorporated in the decision-making process.
📥 The file imports external modules and defines a ROOT_DIR constant for specifying the root directory for file operations.
🧠 The file demonstrates how to set up and use an AI agent with various tools and memory mechanisms.


### `llama.py`

📝 The file defines a class called `LLama2`.
🔍 The purpose of the file is to provide a wrapper for a language model called LLama2.
🔧 The `LLama2` class has an `__init__` method for initializing the model and tokenizer.
🔌 The class has a `__call__` method and a `generate` method for generating text based on a given prompt.
🤖 The generated text is produced by the LLama2 language model.
🔧 The class supports optional quantization of the model using a specified configuration.
⚙️ The device (CPU or GPU) used for running the model can be specified.
🔧 The maximum length of the generated text can be set.
📝 The file also includes error handling for loading the model or tokenizer and generating the text.
🔒 The file currently contains commented out code that demonstrates how to use the `LLama2` class.


### `main.py`

📄 This file contains a class called "ProfitPilot" which serves as an agent for conducting sales conversations.
🤝 The agent can initiate and respond to conversations with potential prospects.
🏢 The agent collects information about the company and salesperson involved in the conversation.
💼 It follows a predefined conversation flow with different stages, such as introduction, qualification, value proposition, needs analysis, solution presentation, objection handling, closing, and end of conversation.
📝 The agent provides example conversations and prompts for generating appropriate responses.
🔀 The agent uses the "Agent" class from the "profit.agent" module.
📝 The agent can be run with a specific task, which triggers the conversation flow.
🔄 The agent generates responses based on the previous conversation history and the stage of the conversation.
📝 The generated responses are printed to the console.
⚙️ The agent can be customized with various parameters, such as AI name, role, external tools, company name, values, conversation type, business, and salesperson name.


### `tools.py`

📚 The file contains Python code that imports various modules and tools.   
🧰 It defines functions and classes for processing CSV files, browsing web pages, and querying web pages.   
🔍 It uses tools like pandas, BeautifulSoup, and Playwright for data manipulation, web scraping, and parsing HTML.   
💡 The purpose of the file is to provide a set of tools for working with data, interacting with web pages, and extracting information from them.   
📝 It also includes some utility functions and context managers for file management and directory navigation.   
🔌 The file uses external libraries such as langchain and profit.llama for additional functionality.   
⚠️ There are some commented-out code lines that indicate possible future enhancements or dependencies.   
🌐 The file also includes integration with Zapier for automating workflows using the ZapierNLAWrapper.   
📦 The file imports several modules and classes from different packages, indicating a modular and extensible design.   
🔧 The code includes error handling to handle exceptions and return appropriate error messages.

<!-- Living README Summary -->