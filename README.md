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

This folder contains a variety of files and folders related to different aspects of a software application. It includes configuration files for customizing the application's theme and user interface, a Dockerfile for building a containerized version of the application, a license file for compliance and legal terms, Python scripts for running AI tools and generating sales emails, a Docker Compose configuration file for managing the application's deployment, documentation files for interacting with Google APIs and services, and various other files related to the application's functionality and dependencies. Overall, these files provide the necessary resources and components for running and managing the software application.


### `.streamlit`

This folder contains a configuration file named "config.toml" that is used to customize the theme and user interface of a software application. The file specifies a "light" theme with a primary color of "#356dff" and hides the sidebar navigation in the user interface.


### `Dockerfile`

🐍 The file is a Dockerfile for building a Docker image.  
🔧 It uses the official Python 3.8-slim runtime as the base image.  
📁 The working directory in the image is set to `/app`.  
📥 The contents of the current directory are copied into the image at `/app`.  
🛠️ Required tools and dependencies are installed using `apt-get`.  
🐍 Several Python packages are installed using `pip`.  
🔒 Port 80 is exposed to allow incoming network connections.  
📜 The command `python3 example.py` is run when the container starts.  
✨ The purpose of this Dockerfile is to create a containerized Python application.


### `LICENSE`

📄 This file contains the copyright notice and license information for Clarifai, Inc.
🔒 It is licensed under the Apache License, Version 2.0.
🔗 The license can be obtained from http://www.apache.org/licenses/LICENSE-2.0.
💻 The file is intended for compliance with the license when using Clarifai's software.
📝 It specifies that the software is distributed on an "AS IS" BASIS.
🔐 The license outlines the warranties and limitations associated with the software.
📚 The file is important for understanding the legal terms and conditions of using Clarifai's software.
❌ It should not be used for trivial or simple purposes like imports.
👀 It is recommended to read and understand the license before using the software.
📢 Clarifai's copyright and licensing information is provided in this file.


### `app.py`

📝 This file is a script written in Python using the Streamlit library.  
📊 It imports the `ProfitPilot` class from the `profit.main` module.  
🤖 The purpose of the script is to run the ProfitPilot AI tool for generating personalized sales emails.  
📧 It defines various variables and creates an instance of the ProfitPilot class with the provided arguments.  
✉️ The script also defines a task, which is a personalized email template.  
🖥️ It uses the Streamlit library to create a simple web interface for running the ProfitPilot tool.  
🔘 When the "Run" button is clicked, it executes the ProfitPilot tool with the task and displays the response.  
💬 The user can also input their own response and click the "Send" button to run the ProfitPilot with the user input.  
👥 The ProfitPilot tool generates personalized sales emails based on the provided variables and the user input.


### `docker-compose.yml`

📋 This file is a Docker Compose configuration file.
🐳 It defines a service called "app" for building and running a Docker image.
🔨 The image is built using the specified Dockerfile in the current context.
🔌 The service will be accessible on port 8501 of the host and container.
💾 The current directory is mounted as a volume inside the container.
🌐 The environment variable STREAMLIT_SERVER_PORT is set to 8501.


### `docs`

This folder contains important files for interacting with Google APIs and services, including credentials and configuration information. It also contains various files related to a project, such as contact information, project summary, collected integrations, and project results. Additionally, there is an empty file named "input.json". Overall, this folder provides the necessary resources for working with Google APIs and services, as well as a comprehensive overview of the project's progress and findings.


### `example.ipynb`

📂 The file contains code for cloning a GitHub repository.     
🔍 The code cell is used to navigate to the cloned repository.     
🔧 The requirements.txt file is installed using pip3.     
🔬 An example.py file is executed using python3.


### `example.py`

📝 This file is a script that utilizes the ProfitPilot class to automate cold email conversations for sales representatives. 
📧 It defines variables such as AI name, company information, conversation type, and purpose.
🚀 An instance of ProfitPilot is created with the defined variables and an OpenAI API key.
📩 The script generates an email task by filling in the variables and runs it using the ProfitPilot instance.
📌 The purpose of the script is to introduce the company's newest product to a prospect and gauge their interest.
👥 The email is personalized with the prospect's name and the salesperson's name.
💼 The script is designed to streamline the process of reaching out to potential customers and promoting the company's product.
🔒 The human_in_the_loop variable is set to False, indicating that the AI will handle the entire conversation.
🔑 The OpenAI API key is required for the script to access the language model and generate the email content.
💡 The temperature variable controls the level of randomness in the AI's responses.


### `profit`

This folder contains files for a conversational AI application called ProfitPilot. The main file, `__init__.py`, is used to run the application and imports the `ProfitPilot` class from the `profit.main` module. The `agent.py` file defines the `Agent` class, which is responsible for setting up the chatbot's tools and memory components. The `llama.py` file contains code for the `LLama` class, which generates text using a pre-trained language model. The `main.py` file runs the conversational agent for sales purposes by initializing an `Agent` object. The `tools.py` file provides various tools and libraries for natural language processing and data analysis tasks.


### `pyproject.toml`

📝 This file is a configuration file for the Python package "ProfitPilot".
🔧 It uses the Poetry build system for managing dependencies and packaging.
📦 The package is version 0.0.4 and is described as an AI Agents framework.
📚 The package is licensed under MIT and has authors and a homepage specified.
🔗 The repository for the package is hosted on GitHub.
🔑 The package has keywords and classifiers specified for easy search and categorization.
📦 There are multiple packages listed as dependencies, including langchain, transformers, torch, and pandas.
🔬 Development dependencies are not specified in this file.



### `requirements.txt`

📋 This file contains a list of dependencies for a project.     
🔎 It specifies the packages needed for language processing and machine learning tasks.     
🔧 The packages include language models, transformers, and tools for tokenization.     
🔬 Some experimental packages are also included for testing and research purposes.     
🔌 The dependencies cover both deep learning frameworks (e.g., PyTorch) and data processing libraries (e.g., Pandas).     
🔧 A specific library for indexing and searching large-scale embeddings (Faiss-GPU) is required.     
💡 The project may involve natural language processing, text analysis, or machine translation.     
🌐 OpenAI's library is included, suggesting integration with their APIs or models.     
🔤 Sentencepiece is included, indicating the use of subword tokenization.     
🏃 The project is likely to involve language modeling or text generation tasks.


### `trigger_schema.json`

📄 This file is a JSON schema definition.
🔗 It defines a data model for a trigger configuration.
🔀 The trigger configuration can include different types of triggers, such as label triggers, comment triggers, and push triggers.
📝 Each trigger can have different properties and actions associated with it.
🔍 The schema also defines various sub-definitions for properties and actions used in the trigger configuration.
💡 The purpose of this file is to provide a standardized structure for defining trigger configurations in a specific application or system.
📚 The file includes detailed descriptions of each definition and property, making it easier for developers to understand and use the schema.
💻 Developers can use this schema to validate and enforce the structure of trigger configurations in their application or system.
🔄 The schema can be used to ensure consistency and correctness in trigger configurations, reducing errors and improving the overall reliability of the system.
📖 By following this schema, developers can easily create and maintain trigger configurations that align with the desired behavior and functionality of the application or system.


### `ven`

This folder contains files related to different functionalities in a programming environment. It includes a JSON configuration file for enabling a Python data visualization library called pydeck, a header file defining the interface for lightweight cooperative threads called greenlets in Python, and JavaScript files for a Physically Based Rendering (PBR) shader, including configuration and dependencies for features like normal mapping and environment mapping.


### `workflow_schema.json`

📋 This file is a JSON schema definition for a workflow definition.
🖋️ It defines various types of actions that can be performed within a workflow.
🔍 The schema includes definitions for different types of declarations, such as template, variable, constant, and lambda declarations.
📄 It also defines different types of action models, such as commenting, crawling folders, running bash commands, committing and pushing changes, writing into files, inserting content into text, prompting, and reading files.
🔄 The schema allows for both singular and iterable versions of these actions.
🔀 It includes conditional logic with if-else statements and lambda expressions.
🔢 The schema also defines the structure of a workflow definition, including its name, description, inputs, outputs, and steps.
💡 The purpose of this file is to provide a standardized structure for defining and validating workflows.

<!-- Living README Summary -->