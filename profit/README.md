

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains files for a project that involves AI agents and chat applications. The files include an agent.py file that defines an AI agent class with various functionalities such as reading/writing files, processing CSV data, and querying websites. There is also a llama.py file that implements a chat application using the Llama library. Additionally, there is a main.py file that defines an agent class for conducting sales conversations with predefined stages. Lastly, there is a tools.py file that contains various tools and functions for data processing, web scraping, and question answering.


### `__init__.py`

📄 This file is used to run the ProfitPilot program.


### `agent.py`

📝 This file defines a class called "Agent" that represents an AI agent.
🔧 The agent is initialized with various parameters like the model name, API key, and temperature.
🔌 It also has a setup function to configure external tools and memory.
🚀 The agent can be run with a task, which will be processed by the underlying AutoGPT model.
📚 The agent uses tools like reading/writing files, processing CSV data, and querying websites.
🧠 It utilizes a vector store and memory to store and retrieve embeddings.
🔀 The agent can also be called as a function, with the same functionality as the run method.
⚠️ Exceptions are handled and raised with informative error messages.
📃 The file is part of a larger project and imports various modules and packages.
🗂️ The file also contains a root directory constant and a class definition for the Agent.


### `llama.py`

📝 This file implements a chat application using Streamlit and a library called Llama. 
📝 The chat application allows users to interact with an assistant by sending messages and receiving responses. 
📝 The user can enter their message in a text input field and click a button to send it. 
📝 The assistant's responses are generated using the Llama library. 
📝 The chat history is stored in the session state and displayed on the screen. 
📝 There is a button to clear the chat history. 
📝 The file defines a class called LlamaClarifaiChat that initializes the chat application and handles user input and rendering. 
📝 The main function creates an instance of the LlamaClarifaiChat class to start the chat application.


### `main.py`

📝 This file defines a class called "ProfitPilot" that serves as an agent for conducting sales conversations.
🤖 The agent is designed to generate responses in a conversation based on predefined stages of the sales process.
📞 The agent can handle various stages of the conversation, including introduction, qualification, value proposition, needs analysis, solution presentation, objection handling, closing, and ending the conversation.
📝 The agent takes into account the previous conversation history and generates a response based on the stage of the conversation.
🔑 The agent requires certain input parameters, such as AI name, AI role, company name, company values, conversation type, conversation purpose, company business, and salesperson name.
🔑 The agent can also be configured with an OpenAI API key and external tools.
📝 The agent includes a system prompt that provides guidelines for conducting the conversation.
🖥️ The agent can be run with a specific task, and it will generate a response based on the task and the current conversation stage.
🖨️ The agent's response is printed to the console.


### `tools.py`

📝 This file contains a collection of tools and functions for data processing, web scraping, and question answering.

<!-- Living README Summary -->