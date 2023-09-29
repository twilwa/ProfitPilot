

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains files for building an autonomous agent and conducting sales conversations. The "agent.py" file defines the Agent class, which represents the autonomous agent. It can perform various tasks like reading and writing files, processing CSV data, querying websites, and interacting with humans. The "llama2.py" file contains the LLama2 class for text generation using a pre-trained language model. The "main.py" file provides a framework for sales conversations, utilizing the AI agent to generate responses. The "tools.py" file includes code for processing CSV files, browsing web pages, and extracting information.


### `__init__.py`

📝 This file is used to import the ProfitPilot and Agent classes from the profit package.


### `agent.py`

📝 This file defines a class called "Agent" that represents an autonomous agent.  
🔧 The agent is initialized with a set of tools and a memory system.  
🔍 The memory system uses the FAISS library for efficient similarity search.  
🤖 The agent can be run on a task, which triggers its execution using the provided tools and memory.  
📁 The agent can read and write files, process CSV data, query websites, and perform other tasks.  
📝 The agent can also interact with humans using the HumanInputRun tool.  
📨 The agent can draft emails, scrape data, and use Zapier tools for automation.  
🔧 External tools can be added to the agent's toolset.  
🔎 The agent uses an AutoGPT model for natural language processing tasks.  
🚀 The purpose of this file is to define and configure an autonomous agent for various tasks.


### `llama2.py`

📝 The file contains a class called "LLama2" which is used for text generation using a pre-trained language model.
🔌 The class constructor takes several parameters including the model ID, device, and maximum length of generated text.
🔧 The class uses the "transformers" library for working with pre-trained models and tokenizers.
🔍 The "__call__" method can be used to generate text given a prompt text.
🧪 The "generate" method is an alternative to "__call__" for generating text.
📥 The class loads the specified model and tokenizer from the Hugging Face model hub.
💻 The generated text is returned as a string.
🔎 If an error occurs during text generation, an exception is raised.
🔒 The class supports quantization of the model for efficient inference.
📝 The file also contains commented out code that demonstrates how to use the "LLama2" class.


### `main.py`

📝 This file contains a class called "ProfitPilot" which serves as a framework for conducting sales conversations with potential prospects. 
🤖 It utilizes an AI agent from the "profit.agent" module to generate responses based on the conversation history and stage of the conversation. 
📞 The purpose of this file is to provide a structure and guidelines for salespeople to effectively engage with prospects and move them through the sales process. 
💼 It includes attributes for the salesperson's name, company information, conversation type, purpose, and business, as well as external tools and a flag for human involvement. 
🗂️ The file also includes a system prompt that provides instructions and examples for each stage of the conversation. 
📝 The "run" method initializes an instance of the AI agent and runs the specified task, printing the response.


### `tools.py`

📝 This file contains code for processing CSV files using pandas, browsing web pages, and extracting relevant information from them.
📦 It imports various modules and tools for data manipulation, web scraping, and text processing.
🔧 The code includes functions for processing CSV files, browsing web pages using Playwright, and querying web pages for specific information.
🧩 It also defines a tool for splitting text into smaller chunks and a tool for querying web pages using a question-answer chain.
🔌 The file sets up a Zapier integration and provides tools for interacting with Zapier's NLA API.
📚 Some parts of the code are commented out and may not be currently used.
🚀 The code is organized into functions, context managers, and async functions for efficient data processing and web scraping.
🔑 The file may require additional setup and configuration, such as providing a Zapier NLA API key.
💡 Overall, this file serves as a central module for data processing, web scraping, and information extraction tasks.

<!-- Living README Summary -->