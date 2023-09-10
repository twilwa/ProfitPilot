# ProfitPilot
Introducing ProfitPilot, your ultimate autonomous AI sales professional agent. With our cutting-edge technology, we revolutionize the way businesses drive profits and skyrocket their sales.

Imagine having a highly skilled sales professional who works tirelessly for you, always ready to engage clients, close deals, and generate revenue. 

That's exactly what ProfitPilot offers – a seductive value proposition that guarantees increased profitability and accelerated growth for your business.

ProfitPilot combines powerful artificial intelligence with deep learning algorithms, enabling it to understand customer behaviors, preferences, and purchase patterns better than any human salesperson. 

It captivates potential clients with its persuasive communication skills, building lasting relationships and creating repeat customers.

Say goodbye to wasted resources on hiring and training sales staff, as ProfitPilot works 24/7, tirelessly prospecting, qualifying leads, and delivering personalized pitches. 

Its effortless adaptability allows it to navigate through different industries, ensuring your value proposition resonates flawlessly with every client.

But that's not all. 

ProfitPilot's unparalleled ability to analyze big data means it can identify market trends, predict customer demands, and provide you with valuable insights to stay ahead of the competition. 

It becomes your reliable co-pilot, guiding your business towards profitable decisions and unlocking hidden revenue streams.

With ProfitPilot, you'll experience unrivaled efficiency, precision, and revenue generation in your sales process. 

By leveraging the power of autonomous AI, you unlock endless possibilities for sustainable growth, increased ROI, and a competitive edge in any market.

Don't settle for outdated sales strategies. Embrace the future of selling with ProfitPilot – your ultimate seductive value proposition that guarantees an unstoppable surge in profits and takes your business to soaring heights.

---

# Installation
```pip install profit-pilot```

# Usage
```python
from profit.main import ProfitPilot



# Create an instance of the ProfitPilot class
pilot = ProfitPilot(
    openai_api_key="YOUR_OPENAI_API_KEY",
    ai_name="Athena",
    ai_role="Sales Representative",
    external_tools=None,
    company_name="ABC Company",
    company_values="Quality, Innovation, Customer Satisfaction",
    conversation_type="Cold Call",
    conversation_purpose="discuss our new product",
    company_business="Software Development",
    salesperson_name="John Doe",
    human_in_the_loop=False
)

# Define the task you want the agent to perform
task = "Hello, I'm calling to discuss our new product. Can I speak with the decision-maker?"

# Run the task using the ProfitPilot instance
pilot.run(task)

```
# Todo
- Worker
- Prompt,
- Tools, Zapier tool, email answering, summarizng, email understanding, email response
- Lead scraping, create tool that scrapes that scrapes on a website domain


## Requirements
- Email function tools
- Zapier tools
- Prompts
- pdf tool


# TO win Hackathon
- Focus on the story, why we're building this
- Build a seamless user experience


-----

![Clarifai logo](https://www.clarifai.com/hs-fs/hubfs/logo/Clarifai/clarifai-740x150.png?width=240)

# Clarifai App Module Template

This is a template repository to make it easy to get started creating a UI module with Clarifai.


## To use this repo

1. Click the "Use this template" green button on github to make a repo from this repo template and give it a name of the format module-{XYZ} filling in the XYZ portion. 
2. Clone the new repo as normal to your development environment.
3. `pip install -r requirements.txt` to make sure you have all the Python packages installed. Add any new packages to this requirements.txt file that you add during development.
4. Update the README.md to capture what your new module will do.
5. Rename the pages/*.py files as you desire and start filling them in to implement your module.
6. After you're tried things out locally, push your changes to github and get the git commit URL from there in order to create a module in Clarifai. 
7. Go to any app you can create in within Clarifai, select Modules on the left and "Create Module" button, then follow the steps.



<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains files and folders related to various tasks and projects. It includes a configuration file for a Streamlit application, a license file for software distribution, a Python file for generating and sending sales emails, a Python file for running a ProfitPilot instance for sales-related tasks, a Python file for making predictions using the Clarifai API, and folders for a project involving AI agents and chat applications, a Python project using Poetry as the build system, and files for language processing tasks. There are also files related to web scraping, including project summaries, data collection, parsing HTML content, and extracting information.


### `.streamlit`

This folder contains a configuration file named "config.toml" that defines the theme and UI settings for an application. The file specifies that the base theme is set to "light", the primary color is set to "#356dff", and the sidebar navigation is hidden.


### `LICENSE`

📝 This file contains the Apache License, Version 2.0.
🔒 It grants permissions to use the file in compliance with the license.
📜 The license can be obtained from http://www.apache.org/licenses/LICENSE-2.0.
📚 The file relates to software distribution under the license.
📄 It specifies that the software is distributed on an "AS IS" basis.
🔐 There are no warranties or conditions attached to the software.
🚫 The license sets limitations on the use of the software.
💡 The purpose of the file is to define the terms and conditions for using the software.
👥 It is important to comply with the license when using the software.
📝 The file is a legal document that protects the rights of the software owner.


### `app.py`

🏠 This file contains code for a Streamlit application.  
💬 The application has two pages: "Home" and "Chat".  
📝 The user can select a page from the sidebar on the left.  
📲 If the user selects "Home", a message is displayed to select a specific page.  
💬 If the user selects "Chat", an instance of the LlamaClarifaiChat class is created.  
🤖 The LlamaClarifaiChat class runs the logic for the chat functionality.  
🔧 The file uses the Streamlit library for building the user interface.  
⚙️ It also includes commented out code related to CSS styling.  
📚 The file imports modules from the Clarifai and profit.llama libraries.  
📄 The file is configured to have a wide layout for the Streamlit app.


### `email_drafter`

This folder contains scripts and files related to generating and sending sales emails for a start-up called Move Right. The `email_generator.py` script uses the OpenAI API to generate email content based on input examples and system instructions, and then calls the `gmail.py` script to send the draft email using Gmail. The `marketing_report.py` script is for running a marketing report by retrieving data from a company's website and summarizing it using OpenAI's Chat API. The `url_parse.py` script extracts the domain name from a given URL. The `run.sh` file is currently empty and serves no purpose.


### `example.py`

📝 This file sets up and runs a ProfitPilot instance to perform a sales-related task using OpenAI's API.
🔑 It defines variables and configurations for the ProfitPilot instance.
📧 It creates an email task template with personalized information.
🚀 The task is then executed by running the ProfitPilot instance.
💼 The purpose is to automate the process of sending personalized sales emails to prospects.
🤖 The ProfitPilot instance acts as a sales representative AI named Athena.
🌐 The AI interacts with prospects via email to discuss a new product.
📨 The email is customized with prospect and company details.
🔑 OpenAI API key and other sensitive information should be added before running the file.
🔍 The file can be modified to suit different sales scenarios and use cases.


### `llama.py`

📝 This file sets up user authentication and specifies the user and app ID, model details, and the URL of the text input. It then uses the Clarifai API to make predictions on the given text and prints the predicted concepts for each model in the workflow.


### `profit`

This folder contains files for a project that involves AI agents and chat applications. The files include an agent.py file that defines an AI agent class with various functionalities such as reading/writing files, processing CSV data, and querying websites. There is also a llama.py file that implements a chat application using the Llama library. Additionally, there is a main.py file that defines an agent class for conducting sales conversations with predefined stages. Lastly, there is a tools.py file that contains various tools and functions for data processing, web scraping, and question answering.


### `pyproject.toml`

📋 The file is a configuration file for a Python project using Poetry as the build system. 
🔧 It specifies the project name, version, description, license, authors, and homepage. 
🔗 It also includes information about the project's repository and documentation. 
🔎 The file lists keywords and classifiers to categorize the project. 
📦 It defines the packages and their inclusion patterns for packaging. 
🐍 The file specifies the Python version and dependencies required by the project. 
🔧 There are no specific development dependencies mentioned in the file.


### `requirements.txt`

📝 This file contains a list of Python packages and libraries that are used in a project.
💡 The purpose of this file is to specify the dependencies required for the project to run.
📦 The packages listed here include clarifai-grpc, streamlit, streamlit-chat, langchain-experimental, langchain, faiss-gpu==1.7.2, loguru, and openai.
🔍 These packages may be used for tasks such as machine learning, natural language processing, and logging.
🌟 It is important to have these packages installed in order for the project to function properly.
🔧 The versions of the packages are specified for compatibility reasons.
🗂️ This file is commonly named "requirements.txt" or "dependencies.txt".
💻 Developers can use this file to easily install all the required packages for the project.
📌 It is recommended to regularly update the packages listed in this file to ensure security and compatibility.
👍 Having a clear and up-to-date list of dependencies helps streamline the development process.    


### `vectordb`

This folder contains a collection of Python files that provide modules and classes for various language processing tasks. The files include a module for vector database operations, a class for selecting and retrieving text embeddings, a class for selecting different types of document loaders, a class for selecting and initializing retrievers for language processing tasks, a base selector class for managing options, a module for defining and selecting text splitters, and a class for managing a vector store. These files provide a flexible and modular way to perform language processing tasks such as embedding selection, document loading, text retrieval, option selection, text splitting, and vector storage.


### `webscraper`

This folder contains a variety of files with different purposes. There are files related to project summaries, data collection from websites, parsing HTML content, and extracting information. It also includes files for setting up and running programs, as well as files containing specific information about characters in a game. Additionally, there are files that appear to be placeholders for storing user data or for seeking assistance.

<!-- Living README Summary -->