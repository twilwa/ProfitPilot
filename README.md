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

This folder contains a variety of files and folders related to a project. It includes configuration files for Docker and Streamlit, a license agreement, documentation files, Python scripts for automating sales conversations, a JSON schema for workflow automation, and configuration files for data visualization and workflow definitions. There are also files related to dependencies and package management. Overall, this folder represents a collection of resources and tools for developing and running a project involving natural language processing, machine learning, and workflow automation.


### `.streamlit`

This folder contains a configuration file named "config.toml" which is used to customize the appearance of a program. It sets the theme, UI options, and primary color. The sidebar navigation is hidden.


### `Dockerfile`

📋 This Dockerfile sets up a Python environment for running an application.  
📦 It installs necessary tools and dependencies.  
🐍 It installs various Python packages.  
🔌 It exposes port 80 for the application.  
🏃 The application is run using the command `python3 example.py`.


### `LICENSE`

📄 This file is the license agreement for Clarifai, Inc.
📝 It is licensed under the Apache License, Version 2.0.
🔒 The license grants permissions and sets limitations for the use of the software.
🌐 The full text of the license can be found at http://www.apache.org/licenses/LICENSE-2.0.
⚖️ The license is legally binding and must be followed when using the software.



### `docker-compose.yml`

📋 This file is written in YAML format.     
🐳 It is used to define the configuration for a Docker Compose file.     
🔧 It specifies the version of Docker Compose being used.     
🏭 The file defines a service named "app".     
🔨 The "app" service is built using the Dockerfile in the current directory.     
🔌 Port 8501 is mapped from the host to the "app" service container.     
💾 The current directory is mounted to the "/app" directory in the container.     
🌐 An environment variable is set to specify the port for the Streamlit server running in the container.     



### `docs`

This folder contains configuration files for authentication with Google services, including OAuth authentication and service account authentication. It also includes various files related to contact information, executive summaries, integrations, contextual compression for document retrieval, platform information, and URLs for LangChain documentation and resources. The folder serves as a repository of information and resources for understanding and working with LangChain.


### `example.py`

📝 This file creates an instance of the ProfitPilot class and runs a task using it. 
🏢 The task is to send a cold email introducing the company's newest product to a prospect. 
📧 The email is personalized with the prospect's name and includes information about the company and the product. 
💼 The email is sent from a sales representative named John Doe representing ABC Company. 
💡 The purpose of the email is to explore how the product could benefit the prospect's team. 
🔍 The email subject line mentions the product and the prospect's company. 
🚀 The ProfitPilot class is a tool for automating sales conversations. 
🔧 The class is instantiated with various parameters like the AI name, company name, and conversation purpose. 
📨 The run method of the ProfitPilot instance is used to execute the task. 
🎯 The goal is to generate leads and initiate conversations with potential customers.


### `profit`

This folder contains files that serve different purposes. The "__init__.py" file provides the main functionality and logic for the ProfitPilot application. The "agent.py" file defines a class called "Agent" which serves as an interface for running tasks using an AutoGPT model. The "llama2.py" file contains a class called "LLama2" that serves as an interface to a language model for text generation. The "main.py" file defines a class called "ProfitPilot" that serves as a conversational agent for sales purposes. The "tools.py" file provides a collection of tools for various language processing tasks.


### `pyproject.toml`

📋 This file is a configuration file for the Poetry build system and package manager.    
⚙️ It specifies the requirements and settings for the project.    
🔧 The file includes information such as the project name, version, description, license, and authors.    
📦 It lists the dependencies required for the project, including Python version and various packages.    
📚 The file also includes information on the project's homepage, documentation, and repository.    
🔍 Keywords and classifiers are provided to describe the project's focus and intended audience.    
📂 The file specifies the packages to be included in the project.    
🛠️ Development dependencies can be added separately.    
🌟 The project is currently in beta development stage.    
🐍 The project is written in Python 3.6.


### `requirements.txt`

📋 This file contains a list of Python packages and libraries. 
💻 It seems to be related to natural language processing (NLP) and machine learning tasks. 
🔍 The file includes dependencies for tools like Clarifai, Streamlit, Pydantic, and Transformers. 
⚙️ It also mentions specific components like Faiss-gpu, Langchain, and Sentencepiece. 
🔧 Some packages are repeated, indicating their importance in the project. 
👩‍💻 The file may be used for developing NLP models or building language-related applications. 
🔬 It could be a requirements.txt file for setting up the project's environment. 
📦 The presence of Torch and Pandas suggests data manipulation and deep learning capabilities. 
🧪 The inclusion of experimental versions (e.g., Langchain-experimental) indicates testing or exploration. 
📄 Overall, this file is a snapshot of the project's dependencies and tools for NLP and machine learning tasks.


### `trigger_schema.json`

📝 This file is a JSON schema that defines the structure of a configuration file for a workflow automation tool. 
🔍 It contains various definitions for different types of actions that can be performed in the workflow. 
📋 Each action has its own model with properties like name, description, and inputs. 
🚀 The file also includes trigger configurations, such as PushTrigger, LabelTrigger, and CommentTrigger, which define when the workflow should be executed. 
📁 The schema provides a structured way to define and validate workflows, ensuring consistency and ease of use. 
💡 It serves as a reference for developers and users to understand and create workflows using the automation tool. 
🔧 The configuration file can be customized by modifying the properties and adding or removing actions and triggers as needed. 
💻 The file can be used to generate user interfaces or command-line interfaces for configuring workflows. 
🔗 It enables automation of repetitive tasks and streamlines the development and deployment processes. 
📚 The schema documentation can be used as a guide to understand the available actions, their inputs, and how to configure the triggers.


### `ven`

This folder contains configuration files, C API functions, and JavaScript files. The configuration file enables and customizes a data visualization extension for Python. The C API file defines the interface for a Greenlet object in Python 3.10. The JavaScript files include utility functions, a shader program for WebGL rendering, and configurations for a project using the requirejs library.


### `workflow_schema.json`

📄 This file is a JSON schema definition for a workflow definition.
🔗 It defines various types of actions that can be performed in a workflow.
🌟 The file contains definitions for actions such as commenting on an issue, crawling a folder, running a bash command, and more.
🔖 Each action has its own set of inputs and outputs.
📝 The workflow definition itself is represented as a series of steps, each step being an action or a control flow construct.
🔧 Control flow constructs include if statements, for loops, and function invocations.
💡 The purpose of this file is to provide a standardized structure for defining workflows and their actions.
🔍 It allows developers to easily create, modify, and validate workflows in a consistent manner.
✨ The file also includes definitions for different types of declarations and parameters that can be used within the actions.

<!-- Living README Summary -->