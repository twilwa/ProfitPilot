

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains files related to an AI agent called "ProfitPilot" and its supporting classes and tools. The "agent.py" file defines the main Agent class, which can perform various tasks using tools like reading and writing files, processing CSV data, querying websites, drafting emails, and scraping data. The "llama.py" file provides a wrapper for a language model called "LLama2" and allows for text generation based on a given prompt. The "main.py" file contains the ProfitPilot class, which interacts with users through conversations. The "tools.py" file provides a collection of tools for data processing, web scraping, and web querying.


### `__init__.py`

📚 This file initializes the ProfitPilot and Agent classes.


### `agent.py`

📝 This file defines a class called "Agent" that represents an autonomous agent.
🤖 The agent can perform various tasks using a set of tools, including reading and writing files, processing CSV data, querying websites, drafting emails, and scraping data.
🔧 The agent uses the LLama2 language model and the OpenAIEmbeddings model for natural language processing tasks.
🗂️ The agent also uses a vector store for storing and retrieving documents.
🔎 The vector store is implemented using the FAISS library for efficient similarity search.
🤝 The agent can optionally operate in a human-in-the-loop mode, where human input can be incorporated into its decision-making process.
🔀 The agent is set up with a specific AI name and role, and it is initialized with the necessary tools, memory, and the LLama2 model.
🏃 The agent can be run with a task as input, which triggers its execution and returns the result.
❌ If any errors occur during the setup or execution of the agent, a RuntimeError is raised with an appropriate error message.


### `llama.py`

📝 This file contains the implementation of the LLama2 class, which is a wrapper for a language model called "georgesung/llama2_7b_chat_uncensored".
🔧 The class provides methods for generating text based on a given prompt.
⚙️ It initializes the model and tokenizer, and allows for optional quantization of the model.
💡 The model can be run on either CPU or GPU, depending on availability.
📜 The "__call__" method generates text based on a given prompt, while the "generate" method is a shorthand for the same functionality.
🔒 If there are any errors during model loading or text generation, an exception is raised.
⚠️ The code includes commented out example usage, which can be uncommented and executed.



### `main.py`

📝 The file contains a class called ProfitPilot.
🤖 ProfitPilot is an AI agent that interacts with users through conversations.
💼 It has various attributes related to the AI agent, the company, and the conversation.
📚 The system prompt provides guidelines for the AI agent's behavior during the conversation.
📝 The class has a run method that runs the AI agent and prints the response.



### `tools.py`

📋 This file contains a Python script with various tools and functions.
🔧 The tools include functions for processing CSV files, browsing web pages, and querying web pages for information.
📚 The script also imports several libraries and modules, such as pandas, BeautifulSoup, and Playwright.
📂 The script defines a context manager for changing the current working directory.
🔒 The script sets environment variables for authentication with Zapier.
🧪 The script includes some code for testing and running the tools and functions.
💡 The purpose of this file is to provide a collection of tools for data processing, web scraping, and web querying.
📝 The file can be used as a starting point for building more complex applications or workflows.
📝 It is intended for someone who wants to utilize these tools in their Python projects.
📝 The functions and tools defined in this file can be imported and used in other Python scripts.

<!-- Living README Summary -->