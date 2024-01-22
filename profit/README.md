

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains files for a conversational AI agent called "ProfitPilot" and a text generation tool called "LLama". The "agent.py" file defines the "Agent" class, which serves as an interface for interacting with an AI model and includes tools for file manipulation and website querying. The "main.py" file creates an instance of the "ProfitPilot" class, which engages in conversations with potential prospects. The "llama.py" file contains the "LLama" class, used for text generation using a pre-trained language model. The "tools.py" file provides tools and functions for processing data, scraping webpages, and querying information.


### `__init__.py`

📝 This file sets up the ProfitPilot and Agent classes.


### `agent.py`

📝 The file defines a class called "Agent" that serves as an interface for interacting with an AI model.
🔧 The "Agent" class can be configured with various parameters, such as the AI name, role, and temperature.
🧠 The class sets up memory using FAISS and OpenAIEmbeddings for efficient query-based retrieval.
🔧 The class also sets up various tools for file manipulation, CSV processing, website querying, and human input handling.
🚀 The "run" method of the class executes the AI model on a given task, returning the result.
🔍 The "__call__" method is a shorthand for calling the "run" method.
⚠️ Errors during setup or execution are handled and raised as runtime errors.
🔒 The file imports external modules and classes from other packages for its functionality.
📚 The file includes comments to provide additional information about the purpose and usage of the code.
💡 The file is intended to serve as a high-level interface for using the AI model in an application, with customizable parameters and tools.


### `llama.py`

📝 This file contains a Python class called "LLama" that is used for text generation using a pre-trained language model.
🤖 The class takes in parameters such as the model ID, device type, maximum length of generated text, and quantization options.
🔤 It uses the "transformers" library to load the tokenizer and the model for text generation.
🖥️ The class has a "__call__" method and a "generate" method, both of which generate text based on a given prompt.
⚠️ If there are any errors during text generation, the class logs the error and raises an exception.
🔧 The class can be instantiated and used to generate text by calling the "__call__" or "generate" methods.
✅ The code also includes commented-out example usage of the class.
📚 The purpose of this file is to provide a convenient way to generate text using a pre-trained language model.


### `main.py`

📄 This file contains the code for the "ProfitPilot" class, which is a part of the "profit" module.
🤖 The purpose of this class is to create an instance of an AI agent that can engage in conversations with potential prospects.
🔀 The class has various attributes and parameters that define the AI agent's behavior and characteristics.
📝 The agent can be customized with a name, role, external tools, company information, conversation type, and more.
🔑 It also requires an OpenAI API key to function.
🗣️ The AI agent follows a specific conversation flow, progressing through stages such as introduction, qualification, value proposition, needs analysis, solution presentation, objection handling, closing, and ending the conversation.
💬 The agent generates responses based on the conversation history and the stage of the conversation.
🖥️ The "run" method of the class initializes an instance of the AI agent and runs a specified task.
📩 The generated response can be printed for further analysis or use.


### `tools.py`

📝 This file contains code for processing CSV files using pandas, scraping webpages, and querying webpages for information.
📊 It uses various libraries and tools such as pandas, BeautifulSoup, Playwright, and Zapier.
🔍 The `process_csv` function processes a CSV file using pandas and a limited REPL.
🌐 The `browse_web_page` function scrapes a whole webpage using Playwright and BeautifulSoup.
❓ The `WebpageQATool` class allows browsing and scraping webpages, and querying them for specific information.
🗂️ The file also includes some utility functions and imports necessary libraries.
🔧 It defines a context manager for changing the current working directory.
📚 It imports and uses various modules from the `langchain` package.
🔑 It sets environment variables and initializes tools for Zapier integration.
📌 Overall, this file provides tools and functions for processing data, scraping webpages, and querying information from webpages.

<!-- Living README Summary -->