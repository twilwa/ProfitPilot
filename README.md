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

This folder contains various files and folders related to different aspects of a sales automation tool called ProfitPilot. It includes configuration files for Docker and Streamlit, scripts for running the tool, documentation files, and JSON schemas for defining workflows and actions. The files and folders serve different purposes, such as customizing the tool's theme, building Docker images, generating personalized email templates, and defining workflows for automated processes. Overall, the folder contains the necessary components for running and customizing the ProfitPilot tool.


### `.streamlit`

This folder contains a configuration file called `config.toml` that is used to customize the theme and UI settings for a specific application or website. The file specifies a light theme, a primary color of "#356dff", and a UI setting to hide the sidebar navigation.


### `Dockerfile`

🏭 This file is a Dockerfile used to build a Docker image.  
🐍 It uses the official Python 3.8-slim runtime as the base image.  
📁 The working directory inside the container is set to "/app".  
📥 The contents of the current directory are copied into the container at "/app".  
🔧 Required tools and dependencies are installed using apt-get.  
📦 Multiple Python packages are installed using pip.  
🔓 Port 80 is exposed for the application to run on.  
🏃 The command to run the application is specified as "python3 example.py".


### `LICENSE`

📝 The file contains the copyright notice and license information for Clarifai, Inc.
🔒 It is licensed under the Apache License, Version 2.0.
🌐 The license can be obtained from the provided URL.
💻 The file is related to software distribution and usage.
📜 It outlines the permissions and restrictions of the license.
📄 The license is based on an "AS IS" basis, without warranties.
🚫 It specifies limitations on the use of the software.
📝 The file is important for legal compliance.
🔑 It ensures proper usage and protection of Clarifai's intellectual property.
📚 It is recommended to read and understand the license before using the software.    


### `app.py`

📝 This file is a script for running a sales automation tool called ProfitPilot.
📧 It generates personalized email templates for sales representatives.
🧠 The script defines variables for the tool, such as the AI name, company information, and conversation details.
🚀 It creates an instance of the ProfitPilot class and defines the task to be performed.
📩 The task is to send an introductory email to a prospect, customized with their name and relevant information.
💼 The script includes a Streamlit interface for user interaction.
🏃‍♂️ When the "Run" button is clicked, the script runs ProfitPilot and displays the response.
✉️ Users can also input their own response and send it using the "Send" button.
📝 The script is organized into functions, with the main function being the entry point.
🔒 The main function is only executed if the script is run directly, not when imported as a module.


### `docker-compose.yml`

📋 This file is written in YAML format.  
🐳 It is used to define Docker services.  
🔨 The `app` service is being built using a Dockerfile in the current directory.  
🔌 The service is exposing port 8501.  
💾 The current directory is being mounted to the `/app` directory in the container.  
🔧 An environment variable `STREAMLIT_SERVER_PORT` is set to 8501.


### `docs`

This folder contains files related to authentication and configuration for accessing Google services, as well as various text files with documentation, summaries, and resources related to contact information, HTML content, integrations, contextual compression, platforms, and the LangChain project. There is also an empty file that serves no specific purpose.


### `example.ipynb`

📁 The file clones a GitHub repository.     
🔍 It navigates to the cloned repository.     
📦 It installs the required packages listed in the `requirements.txt` file.     
🔬 It runs the `example.py` script.     



### `example.py`

📝 This file sets up and runs a ProfitPilot instance for conducting a sales conversation. 
🔑 The variables at the beginning define key information such as the AI name, salesperson name, and prospect name. 
📧 The task variable contains an email template that introduces the company's newest product to the prospect. 
🚀 The ProfitPilot instance is then used to run the task and initiate the sales conversation.


### `profit`

This folder contains files related to a conversational AI sales agent. The main file, "main.py," provides a framework for building and running the agent. It imports the "Agent" class from the "agent.py" file, which represents the AI agent and handles generating responses based on given tasks. The "llama.py" file defines a class for text generation using a pre-trained language model. The "tools.py" file contains various tools and utilities for data processing, web scraping, and natural language processing. The "__init__.py" file is a script to run the "ProfitPilot" and "Agent" classes.


### `pyproject.toml`

📝 This file is a configuration file for a Python project using Poetry as the build system.
📦 It specifies the project name, version, description, license, authors, and homepage.
🔗 It also includes information about the project's repository, documentation, and keywords.
🐍 The file lists the project's dependencies, including specific versions for some packages.
🧪 There is a section for dev-dependencies, which are dependencies only needed for development.
✨ The file contains classifiers that describe the project's intended audience and topic.
📂 It specifies the packages to include in the project.
📝 The file is written in TOML format.
💡 The project is called "ProfitPilot" and is focused on AI agents.
🔧 Poetry is used as the build system for managing the project's dependencies.


### `requirements.txt`

📋 This file contains a list of dependencies for a project.    
🔧 It specifies the required packages and libraries needed for the project.    
📦 The listed packages include language models, machine learning frameworks, and data processing tools.    
🔬 Some of the packages are experimental and may not be widely used or stable.    
💻 The file helps ensure that all necessary dependencies are installed for the project to run.    
🔍 It includes both general-purpose packages like pandas and specialized ones like sentencepiece.    
🔧 The packages may be used for tasks such as language processing, model training, and data analysis.    
📚 The file provides a convenient reference for developers to see the required packages at a glance.    
⚙️ Developers can use this file to set up their development environment and install the necessary dependencies.    
🔒 It is important to keep this file updated to ensure compatibility and avoid dependency conflicts.    


### `trigger_schema.json`

📝 This file is a JSON schema for defining various action models and trigger configurations. It provides a structure for describing different actions and their inputs/outputs. It also defines triggers that can be used to initiate actions based on specific events or conditions.


### `ven`

This folder contains three subfolders: "etc," "include," and "share." The "etc" folder includes a configuration file for enabling the PyDeck extension in Jupyter Notebook. The "include" folder contains a file that defines the interface for the Greenlet object in Python. The "share" folder includes JavaScript files for a codebase utilizing WebGL for creating and manipulating vertex array objects.


### `workflow_schema.json`

📝 This file is a JSON schema for defining workflows.
📝 It includes definitions for various types of actions that can be performed within a workflow.
📝 Actions include commenting, setting issue titles, crawling folders, running bash commands, committing and pushing changes, writing into files, inserting content into text, prompting for user input, and reading files.
📝 Workflows can be defined with a series of steps, which can include actions, workflow invocations, and conditional statements.
📝 Conditional statements can be based on the output of a Python lambda expression or the presence of a variable in the context.
📝 Inputs and outputs can be defined for workflows.
📝 The file also includes definitions for various types of declarations and templates that can be used within actions.
📝 The purpose of this file is to provide a standardized way to define and execute workflows for automated processes.
📝 It serves as a guide for developers to create workflows and understand the available actions and their configurations.
📝 The file can be used by workflow engines or automation tools to validate and execute workflows based on this schema.

<!-- Living README Summary -->