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

This folder contains a variety of files and folders related to different aspects of a project. It includes configuration files for setting up a Python environment, a Dockerfile for containerization, license information, documentation files, code examples, and files related to building an autonomous agent. There are also files for managing dependencies, defining trigger configurations, and defining workflows. Further investigation is needed to understand the specific purpose and functionality of each file.


### `.streamlit`

This folder contains a configuration file, "config.toml", which is used to define the theme and UI settings of an application. The base theme is set to "light" with a primary color of "#356dff". Additionally, the UI setting "hideSidebarNav" is set to true, indicating that the sidebar navigation should be hidden.


### `Dockerfile`

🏭 This Dockerfile sets up a Python environment for running an application.  
📦 It installs required tools and dependencies.  
🔧 It installs several Python packages.  
🔌 It exposes port 80 for the application.  
⚙️ The command to run the application is specified as "python3 example.py".


### `LICENSE`

📜 This file contains the copyright and licensing information for Clarifai, Inc.
🔒 It is licensed under the Apache License, Version 2.0.
💼 The purpose of this file is to outline the terms and conditions for using the software.
📚 It provides a link to obtain a copy of the license.
📝 The license ensures compliance with applicable laws.
🔧 The file covers the distribution of the software on an "AS IS" basis.
🚫 It disclaims any warranties or conditions associated with the software.
🔐 The license sets limitations on the use of the software.
📑 The file is essential to understanding the legal rights and obligations for using the software.
👀 It is important to review this file before using the software.


### `docker-compose.yml`

📝 This file is written in YAML format
🐳 It is used to define a Docker Compose configuration
🔧 The configuration includes a service named "app"
🔨 The "app" service is built using the Dockerfile in the current directory
🔌 The service exposes port 8501
📂 The current directory is mounted as a volume in the container
🌐 An environment variable "STREAMLIT_SERVER_PORT" is set to 8501 for the service


### `docs`

This folder contains configuration files for Google API clients and service accounts, as well as various text files providing summaries and information on different aspects of a project. There is also an input.json file that appears to be empty and its purpose is currently unknown. Further investigation is needed to determine its purpose.


### `example.ipynb`

📋 This file contains a code cell with several commands.    
🔍 The purpose of the file is to clone a Github repository, install the required dependencies, and run an example script.    
💻 The commands are written in Python and executed in a Jupyter notebook or similar environment.    
📦 The repository being cloned is named "ProfitPilot" and is hosted on GitHub.    
📥 The `requirements.txt` file contains a list of dependencies that need to be installed.    
🔧 The `example.py` script is meant to demonstrate the functionality of the code in the repository.    
🚀 The commands can be run sequentially to set up and run the example code.    
👀 It is assumed that the person reading the file has some familiarity with Python and Jupyter notebooks.    
❗️ The file assumes that the necessary tools and libraries are already installed.    
🔗 Additional information about the repository and its purpose can be found on its GitHub page.


### `example.py`

📝 The file defines variables and creates an instance of the ProfitPilot class.    
📧 The purpose of the file is to send a cold email introducing a new product to a prospect.    
🤖 The ProfitPilot class is used to automate the email sending process.    
📝 The email template is customized with the prospect's and salesperson's information.    
📧 The email highlights the company's values and offers to discuss the new product.    
👥 The email is sent from the salesperson to the prospect.    
💼 The company specializes in software development.    
🔍 The email's subject line mentions the prospect's name and the new product.    
✉️ The email is expected to generate a response from the prospect.    
🚀 The ProfitPilot instance runs the task to send the email.


### `profit`

This folder contains files for building an autonomous agent and conducting sales conversations. The "agent.py" file defines the Agent class, which represents the autonomous agent. It can perform various tasks like reading and writing files, processing CSV data, querying websites, and interacting with humans. The "llama2.py" file contains the LLama2 class for text generation using a pre-trained language model. The "main.py" file provides a framework for sales conversations, utilizing the AI agent to generate responses. The "tools.py" file includes code for processing CSV files, browsing web pages, and extracting information.


### `pyproject.toml`

📝 This file is a configuration file for the Poetry package manager.
📦 It defines the project name, version, description, and license.
👥 It specifies the author and homepage of the project.
📚 It includes the README file and provides a link to the repository and documentation.
🔑 It lists keywords and classifiers for the project.
📦 It defines the project's dependencies and dev dependencies.
🔧 The file is written in TOML format.
✨ The purpose of this file is to manage the project's dependencies and provide metadata for the package.


### `requirements.txt`

📋 This file contains a list of Python packages and libraries.  
📦 The packages listed here are used for various purposes, such as machine learning, natural language processing, and data manipulation.  
🔍 Some of the notable libraries include Clarifai, Streamlit, Pydantic, OpenAI, Transformers, Faiss-GPU, Torch, Pandas, and Sentencepiece.  
🔬 There are also experimental versions of the Langchain library listed.  
❗️ The file may be incomplete or contain duplicates, as some packages are listed multiple times.


### `trigger_schema.json`

📄 This file is a JSON schema definition.
🔗 It defines a data model for a trigger configuration.
🔀 The trigger configuration can include different types of triggers such as label, comment, and push triggers.
📝 Each trigger type has its own set of properties and actions.
🔧 The actions include various operations like commenting on an issue, crawling a folder, running a bash command, and more.
📚 The actions can be used individually or in an iterable workflow.
🗂️ The file also defines different input and output fields for the actions.
🔑 The trigger configuration can have parameters and branch names.
📥 The purpose of this file is to provide a structured definition for creating and configuring triggers and their associated actions.


### `ven`

This folder contains configuration files and code related to the PyDeck and PyGreenlet extensions. It includes a configuration file for the PyDeck extension, a header file for the PyGreenlet object interface in Python, and JavaScript modules for a Physically Based Rendering shader and a module called `@deck.gl/jupyter-widget`.


### `workflow_schema.json`

📋 This file contains a JSON schema for defining workflows.
🔗 It defines various action models and their properties.
🔀 Action models include actions like commenting, crawling folders, running bash commands, and more.
💼 Each action model has its own set of inputs and outputs.
🔄 Workflows can be defined as a sequence of steps, which can be action models or other workflow invocations.
🔁 Workflows can also have iterable versions, allowing for iteration over a set of values.
📝 Workflows can include conditions and branching logic using if statements.
🔧 The file also defines various declarations and templates that can be used within the action models.
📄 The purpose of this file is to provide a standardized way to define and execute workflows.

<!-- Living README Summary -->