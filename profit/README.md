

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains files that serve different purposes. The "__init__.py" file provides the main functionality and logic for the ProfitPilot application. The "agent.py" file defines a class called "Agent" which serves as an interface for running tasks using an AutoGPT model. The "llama2.py" file contains a class called "LLama2" that serves as an interface to a language model for text generation. The "main.py" file defines a class called "ProfitPilot" that serves as a conversational agent for sales purposes. The "tools.py" file provides a collection of tools for various language processing tasks.


### `__init__.py`

📝 This file contains the main ProfitPilot class from the profit module.     
🤖 It also imports the Agent class from the same module.     
💼 The purpose of this file is to provide the main functionality and logic for the ProfitPilot application.


### `agent.py`

📝 This file defines a class called "Agent" which serves as an interface for running tasks using an AutoGPT model.
📦 The class has methods for setting up tools, memory, and the agent itself.
🔧 The tools include file read/write, CSV processing, website querying, human input, Zapier integration, email drafting, and data scraping.
🧠 The memory setup involves creating an embedding model, an index, and a vector store using FAISS and InMemoryDocstore.
⚙️ The agent setup initializes an AutoGPT model with the specified name, role, tools, and memory.
🏃‍♀️ The "run" method runs a given task using the agent and returns the result.
🔁 The "__call__" method is a shorthand for calling the "run" method.
🔴 If any errors occur during setup or execution, appropriate error messages are raised.
📚 The file imports various libraries and modules, including faiss and langchain, to support its functionality.
🗂️ The file also defines a ROOT_DIR constant and uses it for file operations.


### `llama2.py`

📝 The file contains a class called "LLama2" that serves as an interface to a language model for text generation.
🔧 The class constructor allows for customizing the model's settings such as the model ID, device, maximum length, and quantization.
📚 The class uses the Hugging Face transformers library to load the model and tokenizer based on the provided model ID.
🔍 The "__call__" method generates text based on a given prompt using the loaded model and tokenizer.
🔍 The "generate" method is an alternative name for the "__call__" method.
⚠️ If any errors occur during model or tokenizer loading, an error message is logged and an exception is raised.
🔧 The code includes commented out example usage of the "LLama2" class.
⚠️ If any errors occur during text generation, an error message is logged and an exception is raised.



### `main.py`

📄 This file defines a class called "ProfitPilot" that serves as a conversational agent for sales purposes. 
🤖 The agent is designed to simulate a salesperson and generate responses based on the stage of the conversation and previous interaction history. 
🔧 It has various attributes and methods for managing conversation parameters and generating appropriate responses. 
📝 The file also includes a system prompt that provides guidelines for the agent's behavior and conversation flow. 
⚙️ The "run" method initializes an instance of the Agent class and executes the conversation task. 
📩 The generated response is printed to the console.


### `tools.py`

📝 This file contains a Python script that serves as a toolkit for various language processing tasks. It includes tools for processing CSV files, scraping web data, drafting emails, browsing web pages, and querying webpages for relevant information. The file also imports several libraries and defines helper functions and classes. The purpose of this file is to provide a collection of tools for language-related tasks.

<!-- Living README Summary -->