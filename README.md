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

This folder contains various files and folders related to a project. It includes configuration files for the user interface and Docker containers, a license file, documentation files, a Python script for email generation, a folder for profit maximization and web scraping, configuration files for package management, a requirements file for Python dependencies, JSON schemas for defining actions and workflows, and files related to data visualization and a JavaScript project. Overall, the contents of this folder serve different purposes such as configuring the project, managing dependencies, generating emails, defining actions and workflows, and performing profit maximization and web scraping tasks.


### `.streamlit`

This folder contains a configuration file called "config.toml" that controls the user interface settings. The file specifies a light theme with a primary color of "#356dff" and hides the sidebar navigation.


### `Dockerfile`

🐍 This file is a Dockerfile for building a Docker image using the official Python 3.8-slim runtime.
🔧 It sets the working directory in the image to /app.
📂 The contents of the current directory are copied into the container at /app.
🛠️ Required tools and dependencies are installed using apt-get.
📦 Multiple Python packages are installed using pip.
🔌 The application runs on port 80, which is exposed by the image.
🏃 The command to run the application is "python3 example.py".



### `LICENSE`

📜 This file contains the Apache License, Version 2.0
🔒 The license grants permission to use the file under certain conditions
📝 The purpose of the file is to specify the terms and conditions for using the software
🌐 The license can be obtained from the provided URL
⚖️ The license ensures compliance with applicable laws
💻 The file covers software distribution and usage rights
📚 The license provides a disclaimer of warranties and limitations
📝 The file is important to understand the legal rights and obligations associated with the software
🗒️ The license is applicable to all versions of the software
📃 The file highlights the importance of complying with the license terms


### `docker-compose.yml`

🏢 This file is used to configure a Docker container for an application.     
🔧 The container is built using the specified Dockerfile.     
🔌 The application will be accessible on port 8501.     
💾 The current directory is mounted as a volume in the container.     
⚙️ The application can use the environment variable STREAMLIT_SERVER_PORT with a value of 8501.


### `docs`

This folder contains important configuration files for integrating with Google services and accessing Google Cloud. It also includes various files related to the LangChain project, such as an executive summary, contextual compression information, integration data, and URLs for resources. Additionally, there is an empty input file.


### `example.py`

💡 Purpose: This file is used to introduce a new product to a prospect via a cold email. It utilizes the ProfitPilot class to automate the email generation and sending process.


### `profit`

This folder contains a collection of files and folders related to profit maximization, email drafting, language generation, conversation agents for sales calls, and web scraping. The files include modules for profit maximization, an agent class, email drafting scripts, a language model implementation, a conversation agent class, tools for data processing and web scraping, and scripts for web scraping and data extraction. Each file and folder serves a specific purpose, such as providing functionality for profit maximization, generating draft emails, implementing a language model, building a conversation agent for sales calls, and performing data processing and web scraping tasks.


### `pyproject.toml`

📋 This file is a configuration file for the Poetry package manager.
📦 It defines the project name, version, description, and license.
🔗 It includes links to the project's homepage and repository.
🔧 It specifies the required dependencies for the project.
📚 It provides classifiers to categorize the project.
📁 It defines the packages that should be included in the project.
🔧 It specifies the Python version and additional dev dependencies.
🧪 Dev dependencies are used for development purposes.
⚙️ The file is written in TOML format.


### `requirements.txt`

📝 This file contains a list of Python packages and libraries.  
🔍 It seems to be related to machine learning and natural language processing.  
📦 The file includes packages like Clarifai, Streamlit, Pydantic, and Transformers.  
🔬 It also mentions experimental libraries like Langchain and Langchain-experimental.  
💻 Torch and Pandas are included as well, which are commonly used in data analysis and machine learning.  
📄 The file has duplicate entries for Transformers, Torch, and Pandas.  
👀 Overall, this file appears to be a record of dependencies or requirements for a project.


### `trigger_schema.json`

📋 The file contains a JSON schema for defining various action models and trigger configurations.
🔧 It provides definitions for different types of actions such as commenting, setting issue titles, crawling folders, running bash commands, etc.
🎯 The schema also includes iterable versions of some actions, allowing for iteration over a collection of items.
🔀 Triggers are defined in the "TopLevelTriggerConfig" section, including label triggers, comment triggers, and push triggers.
📝 Each action model has properties such as name, description, inputs, and outputs.
📚 The schema also defines various types of declarations, such as template declarations, variable declarations, constant declarations, and lambda declarations.
🚀 The purpose of this schema is to provide a standardized way to define and configure actions and triggers for a workflow or automation system.
📄 The file can be used as a reference to understand the structure and properties of different action models and trigger configurations.
💡 It can be used as a starting point to create workflow configurations or to validate and generate code based on the defined schema.


### `ven`

This folder contains files related to data visualization, Greenlet objects in Python, and a JavaScript project. The "pydeck.json" file is used for configuring data visualization settings in Python notebooks. The "greenlet.h" file provides an interface and functions for working with Greenlet objects in Python. The JavaScript files include an IPython extension setup, utility functions for object manipulation, and WebGL rendering code.


### `workflow_schema.json`

📄 This file is a JSON representation of a workflow definition.
🔑 It contains various definitions for different types of actions that can be performed in the workflow.
📝 Each action has its own properties and requirements.
⚙️ The workflow definition includes the name, description, inputs, outputs, and steps of the workflow.
🔀 The steps can be a combination of actions, comments, workflow invocations, and conditional statements.
🔄 The workflow can be iterated over a specified number of times or based on a condition.
📥 The inputs and outputs of each action can be customized.
📝 Comments can be added to provide additional information or context.
🔍 The file also includes definitions for various types of declarations and templates used within the workflow.
📂 Overall, this file serves as a blueprint for creating and executing workflows.

<!-- Living README Summary -->