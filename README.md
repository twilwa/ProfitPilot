# ProfitPilot
ProfitPilot is an autonomous AI sales professional agent.


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

This folder contains a variety of files and folders related to a software project. It includes configuration files for Docker and Streamlit, a Dockerfile for creating a Docker image, licensing information, code files for running tasks and sending emails, and files related to a project called "ProfitPilot" that involves trading strategies and sales conversations. There are also files related to authentication, project documentation, a Python project configuration file, and JSON schema definitions for configuring actions and triggers in a workflow. Additionally, there are files related to dependencies and requirements for the project.


### `.streamlit`

This folder contains a configuration file called "config.toml" that is used for specifying theme and UI settings. The file specifies a light theme with a primary color of "#356dff" and indicates that the sidebar navigation should be hidden.


### `Dockerfile`

🐍 This file is a Dockerfile for creating a Docker image.  
📦 It uses the official Python 3.8-slim runtime as the parent image.  
📁 The working directory inside the container is set to /app.  
📂 The contents of the current directory are copied into the container at /app.  
🔧 Required tools and dependencies are installed using apt-get.  
🐍 Several Python packages are installed using pip.  
🔌 The app runs on port 80, which is exposed in the Docker image.  
▶️ The command to run the application is "python3 example.py".


### `LICENSE`

📄 This file contains the licensing information for the software.     
🔒 It is licensed under the Apache License, Version 2.0.     
📝 The license grants permissions and outlines limitations for using the software.     
🔗 The license can be obtained from the provided URL.     
👨‍💻 The software is distributed on an "AS IS" BASIS.     
🚫 There are no warranties or conditions provided with the software.     
📜 The license is governed by applicable law.     
📝 The purpose of the file is to provide legal information and terms of use.     
📑 It is important to comply with the license when using the software.     
🆓 The software is free to use, subject to the terms of the license.    


### `app.py`

📝 This file defines variables and creates an instance of the ProfitPilot class. 
🤖 The purpose of the file is to run a task using the ProfitPilot instance. 
📧 The task is to send an introductory email to a prospect, introducing a new product. 
📩 The email is personalized with the prospect's name, the salesperson's name, and the company's name. 
📨 The email highlights how the product aligns with the prospect's values. 
👥 The email invites the prospect to explore how the product can benefit their team. 
🚀 The ProfitPilot class is responsible for running the task and sending the email. 
💼 The AI name is "Athena" and the AI role is "Sales Representative". 
🌏 The company's business is "APAC AI" and the company's values are "Quality, Innovation, Customer Satisfaction".


### `docker-compose.yml`

📄 This file is written in YAML format.    
🏭 It is used to define a Docker Compose configuration.    
🔨 The configuration specifies a service named "app".    
🐳 The service is built using a Dockerfile in the current directory.    
🌐 The service's port 8501 is mapped to the host's port 8501.    
💾 The current directory is mounted as a volume in the container.    
🔧 An environment variable STREAMLIT_SERVER_PORT is set to 8501.    



### `docs`

This folder contains files related to authentication and credentials, as well as files related to a project called "LangChain." The authentication files contain client-specific installation information and credentials for a Google service account. The project files include information about contact collection, project progress and milestones, integrations, contextual compression in document retrieval systems, platform information, results related to contextual compression, and a list of URLs and file paths related to the project.


### `example.ipynb`

📋 This file is a code cell containing a series of commands.     
🔍 The purpose of the file is to clone a GitHub repository, navigate into it, install required packages, and run an example script.     
💻 It uses Git commands, Python commands, and pip for package installation.     
🔗 The GitHub repository being cloned is "https://github.com/kyegomez/ProfitPilot.git".     
📂 The script assumes that the repository has a file named "requirements.txt".     
📝 The "requirements.txt" file contains a list of packages that need to be installed.     
🔄 After navigating into the cloned repository, it runs a Python script named "example.py".     
🚀 The purpose of the "example.py" script is not specified in the file.     
🔧 This file can be used to automate the setup and execution of a specific project or workflow.     
📖 It is recommended to review the code and understand its purpose before running it.


### `example.py`

📝 This file defines variables and creates an instance of the ProfitPilot class.     
📧 It prepares an email task to introduce a new product to a prospect.     
🚀 The ProfitPilot instance is used to run the task.     
💼 The purpose is to automate the process of sending cold emails to prospects.     
📩 The email is personalized with the prospect's name and company information.     
🔗 The email highlights how the new product aligns with the prospect's values.     
👥 The email is sent from a sales representative named John Doe.     
🏢 The company is ABC Company specializing in APAC AI.     
🧠 The ProfitPilot class handles the AI-powered email automation.     
📨 The task is executed using the ProfitPilot instance.


### `profit`

This folder contains files for the ProfitPilot program. The `__init__.py` file is the starting point for running the program and creates an instance of the Agent class. The `agent.py` file defines the Agent class, which is responsible for executing trading strategies and managing financial transactions. The `llama.py` file provides a wrapper for the LLama2 language model. The `main.py` file contains the ProfitPilot class, which serves as an agent for conducting sales conversations. The `tools.py` file provides a set of tools for working with data, interacting with web pages, and extracting information from them.


### `pyproject.toml`

📝 This file is a configuration file for a Python project.  
📦 It uses Poetry as the build system.  
🔧 The project is named "profit-pilot" and its version is "0.0.3".  
📚 The project is described as "ProfitPilot - AI Agents".  
📝 The license for the project is "MIT".  
👥 The author of the project is Kye Gomez.  
🏠 The homepage and repository for the project are hosted on GitHub.  
📚 The project has keywords related to artificial intelligence and engineering.  
🔧 The project has various dependencies, including clarifai, streamlit, transformers, and more.  
💻 There are no specific development dependencies listed in this file.


### `requirements.txt`

📄 This file contains a list of Python libraries and packages.  
📦 It includes popular libraries like PyTorch, Pandas, and Transformers.  
🔍 Some specialized packages like Clarifai and Faiss-GPU are also included.  
🚀 The purpose of this file is likely to manage dependencies for a project.  
💻 It can help ensure that the required packages are installed.  
🔧 It may also be used to track the versions of the packages being used.  
📝 The file can be used as a reference for developers working on the project.  
📌 It provides a clear overview of the project's dependencies.  
❗️ Empty lines in the file do not contribute to the dependencies.  
⚙️ The order of the packages in the file may indicate their importance or priority.


### `trigger_schema.json`

📋 This file is a JSON schema definition for a configuration file.
🛠️ It defines various models and their properties that can be used to configure actions and triggers.
🔄 The models include actions like commenting, setting issue titles, crawling folders, executing bash commands, etc.
🔗 The models can also be used in iterable workflows where they can be iterated over a list of inputs.
📝 The file provides detailed descriptions and types for each property of the models.
🔀 The file also defines triggers like label triggers, comment triggers, and push triggers.
📜 The purpose of this file is to provide a structured way to define and configure actions and triggers for a workflow.
💡 It serves as a guide for developers to understand the available options and parameters for each action and trigger.
🚀 This file can be used as a reference to create and customize workflows based on the defined models and properties.


### `ven`

This folder contains files related to different aspects of a software project. The "etc" folder contains a configuration file for an application that uses the pydeck extension. The "include" folder contains a file used for working with Greenlets in Python, which are a lightweight concurrency library. The "share" folder contains JavaScript modules and a summary file for a project related to creating and manipulating WebGL contexts for interactive 3D graphics.


### `workflow_schema.json`

📄 This file contains a JSON object representing a workflow definition.
🔑 The main object has properties like "title", "type", and "additionalProperties".
📝 There are several definitions within the file, each describing a specific type of action or declaration.
🔀 The definitions have different properties such as "title", "description", and "type".
🔄 The definitions can be referenced by other definitions or used directly within the workflow steps.
🚀 The workflow steps define the sequence of actions to be executed in the workflow.
🔢 Each step can be a string referring to a definition, or a nested array of steps.
🧩 The workflow can include various types of actions like commenting, crawling folders, running bash commands, and more.
📝 The workflow can also include conditional logic and variable assignments.

<!-- Living README Summary -->