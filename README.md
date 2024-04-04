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

This folder contains files related to a software application. It includes configuration files for customizing the application's theme and user interface, a Dockerfile for setting up a Python environment, a license file that specifies permissions and limitations for using the software, Python scripts for running the application and performing sales-related tasks, a Docker Compose file for defining services, a notebook with code for cloning a GitHub repository, files related to AI-powered sales conversations, a file for managing project dependencies, a JSON schema for defining actions and triggers in a workflow, and configuration and JavaScript files for Jupyter Notebook extensions.


### `.streamlit`

This folder contains a file called "config.toml" which is used to customize the theme and user interface (UI) of a software application. It allows for easy modification of visual elements without changing the code. The file includes settings for the base theme, primary color, and sidebar navigation.


### `Dockerfile`

📋 This Dockerfile sets up a Python environment for running an application.
🏭 It uses the official Python 3.8-slim image as the base.
🔧 The working directory is set to /app in the container.
📥 The contents of the current directory are copied into the container.
🛠️ Required tools and dependencies are installed using apt-get.
🐍 Python packages like clarifai, streamlit, pydantic, etc. are installed using pip.
🔌 The application will run on port 80.
📜 The command to run the application is "python3 example.py".



### `LICENSE`

📄 This file contains the license information for the software.     
📝 It is licensed under the Apache License, Version 2.0.     
🔗 The full text of the license can be found at the provided URL.     
⚖️ The license grants permissions and sets limitations for using the software.     
👥 It is important to comply with the license when using the software.     
📢 The license is applicable to all versions of the software.     
🔒 The software is distributed on an "AS IS" basis without warranties.     
🔐 The license ensures that the software is used responsibly and legally.     
👍 Compliance with the license is required by applicable law.     
📜 The license details can be referred to for further information.     


### `app.py`

📝 This file is a script written in Python using the Streamlit framework.  
📊 It uses the ProfitPilot class from the profit module to perform sales-related tasks.  
🎨 The script also includes CSS styling from the ClarifaiStreamlitCSS module.  
📄 The main function sets up the Streamlit app and displays a title and description.  
🔍 The app allows users to input sales leads emails and information for personalized deal flow.  
🏃‍♂️ Clicking the "Run" button runs the ProfitPilot instance with a predefined task.  
✉️ Clicking the "Send" button allows users to input their own response and run the ProfitPilot instance with it.  
📧 The predefined task is an email template that introduces the company's newest product to a prospect.  
🤖 The ProfitPilot class handles the AI-driven sales conversation with the prospect.  
🚀 The script is executed when the file is run as the main module.


### `docker-compose.yml`

📋 This file is written in YAML format.     
🔧 It is used to define services for a Docker Compose application.     
🏗️ The `app` service is being built using the specified Dockerfile.     
🔌 The `app` service is exposing port 8501 on the host machine.     
💾 The current directory is being mounted to the `/app` directory in the container.     
🌐 The `STREAMLIT_SERVER_PORT` environment variable is set to 8501.


### `example.ipynb`

💻 This file contains code to clone a GitHub repository.     
📦 It then navigates into the cloned repository.     
🔧 The file installs the necessary requirements.     
🚀 Finally, it runs an example script.     



### `example.py`

📝 The file defines variables and creates an instance of the ProfitPilot class.   
📧 It generates an email template to introduce a new product to a prospect.   
🤖 The ProfitPilot class is used to run the task and automate the email sending process.   
🔑 The OpenAI API key is required to use the ProfitPilot class.   
🏢 The variables contain information about the company, salesperson, and prospect.   
💼 The task is customized with the company and prospect details.   
💌 The email is personalized and aims to engage the prospect in a conversation.   
📩 The email subject and body are adjusted based on the defined variables.   
❗️ The file assumes that the ProfitPilot class and necessary dependencies are available.   
🔀 The ProfitPilot instance and task can be modified to suit different use cases.


### `profit`

This folder contains files related to AI-powered sales conversations using the ProfitPilot system. The main.py file implements the ProfitPilot class, which conducts the conversations by utilizing the Agent class and external tools. The agent.py file defines the Agent class, which sets up and runs the AI agent for various tasks. The llama.py file provides a wrapper class for a language model. The tools.py file contains code for various tools and agents used in natural language processing tasks.


### `pyproject.toml`

📝 This file is a `pyproject.toml` file, which is used by the Poetry dependency management tool in Python projects.
📦 It specifies the build system and dependencies for the project.
🔧 The `[build-system]` section defines the build requirements and backend.
🧪 The `[tool.poetry]` section contains metadata about the project, such as name, version, description, license, authors, and homepage.
📚 It also specifies the project's documentation, readme file, repository, keywords, and classifiers.
📦 The `[tool.poetry.dependencies]` section lists the project's dependencies, including Python version and various libraries.
🧪 The `[tool.poetry.dev-dependencies]` section can be used to list development dependencies.
💡 The purpose of this file is to manage the project's dependencies and provide metadata for packaging and distribution.
🔍 It is commonly used in Python projects to ensure consistent and reproducible environments.


### `requirements.txt`

📝 This file contains a list of Python packages and libraries needed for a specific project.


### `trigger_schema.json`

📝 This file is a JSON schema definition.
📋 It defines various object structures for different actions and triggers.
🔗 The objects are organized under the "definitions" key.
🔀 The file includes definitions for actions like "comment", "set_issue_title", "crawl_folder", "bash", etc.
🔄 It also includes definitions for triggers like "push", "label", and "comment".
📚 Each definition specifies the properties and types of the objects.
💡 Some definitions have additional properties like "title" and "description".
🔁 The definitions can be used to validate JSON objects against the schema.
📖 The top-level trigger configuration is defined under the "TopLevelTriggerConfig" key.
💡 The purpose of this file is to provide a structured schema for defining actions and triggers in a workflow.


### `ven`

This folder contains configuration files, include files, and JavaScript files. The configuration files enable different extensions in associated software, the include files define the interface and functionality of a Python object, and the JavaScript files configure and provide support for Jupyter Notebook extensions.


### `workflow_schema.json`

📋 The file is a JSON representation of a workflow definition.
🧩 It contains various definitions for different types of actions and declarations used in the workflow.
🔢 The definitions include templates, variable declarations, constant declarations, lambda declarations, and parameter declarations.
🔀 There are also different action models defined, such as commenting, crawling folders, executing bash commands, committing and pushing changes, writing into files, inserting content into text, prompting, and reading files.
🔄 Some action models are defined as iterable, allowing for iteration over a specified range or list.
🔀 The workflow definition itself is represented by a "WorkflowDefinition" object, which includes a name, description, inputs, outputs, and a sequence of steps.
🧩 The steps can include actions, invocations of other workflows, and control flow constructs such as conditionals and variable assignments.
🎯 The purpose of this file is to provide a structured definition of a workflow that can be executed by a workflow engine.
📚 The definitions and models in the file serve as building blocks for creating complex workflows with various actions and logic.
📝 The file can be used as a reference for understanding the structure and components of a workflow definition.

<!-- Living README Summary -->