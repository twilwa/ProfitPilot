

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains files for a conversational AI application called ProfitPilot. The main file, `__init__.py`, is used to run the application and imports the `ProfitPilot` class from the `profit.main` module. The `agent.py` file defines the `Agent` class, which is responsible for setting up the chatbot's tools and memory components. The `llama.py` file contains code for the `LLama` class, which generates text using a pre-trained language model. The `main.py` file runs the conversational agent for sales purposes by initializing an `Agent` object. The `tools.py` file provides various tools and libraries for natural language processing and data analysis tasks.


### `__init__.py`

📋 This file is used for running the ProfitPilot application.
🌐 It imports the ProfitPilot class from the profit.main module.
🤖 It also imports the Agent class from the profit.agent module.
💼 The purpose of this file is to initialize and configure the ProfitPilot application.
✅ It is essential for running the application successfully.


### `agent.py`

📝 This file defines a class called "Agent" which serves as the main component for an AI chatbot.
🔧 The "Agent" class is responsible for setting up various tools and memory components required for the chatbot's operation.
🤖 The chatbot can be configured to work with or without human input in the loop.
📚 The chatbot uses the "Langchain" library for natural language processing tasks.
🔑 The chatbot can use either the LLama model or the OpenAI GPT-4 model for generating responses.
🛠️ The chatbot supports various tools such as reading/writing files, processing CSV data, and querying websites.
🔍 The chatbot uses FAISS for efficient similarity search in its memory component.
🚀 The chatbot can be run by calling the "run" method and passing a task as input.
⚠️ Any errors encountered during setup or execution of the chatbot will raise a runtime error.
📞 The chatbot can also be called as a function, with a task as the input, to invoke the "run" method.


### `llama.py`

📝 This file contains code for a Python class called "LLama" that utilizes the Hugging Face Transformers library to generate text using a pre-trained language model.
🔌 The class has an initializer that takes parameters such as the model ID, device type, maximum length of generated text, and options for quantization.
🔧 The class loads the specified tokenizer and model from the Hugging Face model hub, and sets the device for computation.
🔍 The class provides a "__call__" method that takes a prompt text and generates text based on it using the model.
💬 The class also provides a "generate" method that performs the same text generation functionality as "__call__".
❗ If any errors occur during model or tokenizer loading or during text generation, the class logs the error and raises an exception.
📚 The file includes commented-out example code at the end that demonstrates how to create an instance of the "LLama" class and generate text.



### `main.py`

📝 This file defines a class called `ProfitPilot` which is used to run a conversational agent for sales purposes.
🧠 The class takes various parameters such as AI name, role, external tools, company information, conversation history, and more.
🔀 The `run` method of the class initializes an `Agent` object and runs the conversation task using the provided parameters.
📜 The conversation history is stored and used to generate responses based on the stage of the conversation.
📝 The generated responses are printed to the console.
🔑 The class requires an OpenAI API key to interact with the language model.
💼 The purpose of this file is to provide a framework for running a conversational AI agent for sales conversations.
📚 The class includes detailed comments explaining the different stages of a sales conversation and how to handle them.
⚠️ The file also includes an example conversation history and instructions on how to use the generated responses.
🚀 The `run` method can be called with different conversation tasks to generate responses for different stages of the conversation.


### `tools.py`

📝 This file contains code for various tools and libraries used in natural language processing and data analysis tasks.
💡 It includes imports of necessary modules and packages.
🔧 The file defines functions for processing CSV files using pandas, browsing web pages and scraping information, and querying web pages for specific information.
📚 It also includes tools for managing files, such as reading and writing files.
🌐 The file includes tools for web search and integration with Zapier for automation.
🔒 Some parts of the code require authentication or API keys.
🧠 The file defines a class for a specific NLP tool called WebpageQATool.
🔌 It imports other modules and tools from different libraries like langchain and pydantic.
📃 The file ends with the initialization of Zapier tools and the assignment of the ZapierNLAWrapper to the zapier_toolkit.

<!-- Living README Summary -->