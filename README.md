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

This folder contains files and folders related to a Streamlit application called ProfitPilot. It includes a Dockerfile and a docker-compose.yml file for containerization, as well as configuration files for authentication and token endpoints. The app.py file contains the code for the Streamlit application, while the example.py file utilizes the ProfitPilot class to automate sales conversations. There are also files related to the LangChain project, a Python script for listing inputs in the Streamlit app, and configuration files for a Python project and workflow definitions.


### `.streamlit`

This folder contains a configuration file named `config.toml` that is used to customize the theme and user interface (UI) of an application. The file specifies settings such as the base theme, primary color, and whether the sidebar navigation should be hidden. Developers can edit this file to modify the appearance of the application, but it's important to understand each section before making changes.


### `Dockerfile`

📦 This file is a Dockerfile used to build a Docker image.  
🐍 It uses the official Python 3.8-slim runtime as the base image.  
📂 The working directory inside the image is set to "/app".  
📥 The contents of the current directory are copied into the "/app" directory of the image.  
🛠️ Required tools and dependencies are installed using apt-get.  
🔍 Several Python packages are installed using pip.  
🔌 The application inside the image will run on port 80.  
🏃 The command to run the application is "python3 example.py".  



### `LICENSE`

📄 This file contains the license information for Clarifai, Inc.
🔒 It is licensed under the Apache License, Version 2.0.
📝 The license allows usage of the file in compliance with the license terms.
🌐 The license can be obtained from http://www.apache.org/licenses/LICENSE-2.0.
⚖️ The license covers the distribution of software on an "AS IS" BASIS.
🔐 It specifies that there are no warranties or conditions of any kind.
🔒 The license should be reviewed to understand its limitations and requirements.
📜 The license is governed by applicable law and requires written agreement.
📝 The file's purpose is to provide legal information and guidelines for usage.
💡 It is important to read and understand the license before using the software.    


### `app.py`

📝 This file contains code for a Streamlit application.
🤖 The application uses a class called ProfitPilot to automate sales conversations.
🔧 It imports necessary modules and sets the layout for the Streamlit app.
📝 The app allows users to enter sales leads' emails and information for personalized deal flow.
🏃‍♀️ When the "Run" button is clicked, the app runs the ProfitPilot instance with a predefined task.
📨 Users can also input their own response and click the "Send" button to run the ProfitPilot with their response.
📧 The predefined task is an email template that introduces the company and its newest product to the prospect.
📝 The app displays the response generated by the ProfitPilot for both the predefined task and user input.
📝 The file includes a main function that sets up the Streamlit app and runs the ProfitPilot when the buttons are clicked.
🔒 The ProfitPilot instance is created with various parameters, including the prospect's name and the salesperson's name.


### `docker-compose.yml`

📝 This file is written in YAML format.     
🐳 It is used to define a Docker Compose configuration.     
🏭 The configuration defines a service named "app".     
🔨 The service is built using a Dockerfile in the current directory.     
🔌 The service will be accessible on port 8501.     
💾 The current directory will be mounted as a volume in the container.     
🌐 The environment variable STREAMLIT_SERVER_PORT is set to 8501.


### `docs`

This folder contains configuration files for client and service agent authentication, as well as various files related to the LangChain project. The configuration files provide authentication and token endpoints for secure authentication, while the LangChain project files provide information about contextual compression in document retrieval systems and serve as a guide for implementing contextual compression techniques.


### `example.ipynb`

📋 This file contains code to clone a GitHub repository and install its dependencies.   
📦 The purpose of the file is to set up and run the example code from the ProfitPilot repository.   
🚀 It provides a quick and convenient way to get started with the ProfitPilot project.   
💻 The code is executed in a code cell.   
🔗 The GitHub repository being cloned is "https://github.com/kyegomez/ProfitPilot.git".   
🔍 The file also changes the directory to the ProfitPilot folder.   
🔧 The file installs the required packages listed in the "requirements.txt" file.   
▶️ Finally, it runs the "example.py" script.   
👩‍💻 This file is suitable for someone new to the ProfitPilot project.   
📄 It provides clear instructions on how to set up and run the example code.


### `example.py`

📝 This file is a script that utilizes the ProfitPilot class to automate cold email conversations.
📩 It defines variables and creates an instance of the ProfitPilot class with specified parameters.
📧 The script generates a task in the form of an email introducing a new product to a prospect.
🌐 The email is personalized with the prospect's name and includes information about the company and product.
🚀 The task is then executed using the ProfitPilot instance to automate the email sending process.



### `pages`

This folder contains a Python script called "first_page.py" which demonstrates a simple example of listing inputs in a Streamlit app using the Clarifai library. The script retrieves a list of inputs from the Clarifai API based on the user's selection, extracts relevant information, and displays it in a table on the Streamlit app. It also includes error handling for cases where the user doesn't provide the number of inputs or if the number of inputs is zero.


### `profit`

This folder contains files for a conversational AI agent called "ProfitPilot" and a text generation tool called "LLama". The "agent.py" file defines the "Agent" class, which serves as an interface for interacting with an AI model and includes tools for file manipulation and website querying. The "main.py" file creates an instance of the "ProfitPilot" class, which engages in conversations with potential prospects. The "llama.py" file contains the "LLama" class, used for text generation using a pre-trained language model. The "tools.py" file provides tools and functions for processing data, scraping webpages, and querying information.


### `pyproject.toml`

📝 This file is a configuration file for a Python project using Poetry.
🔧 It specifies the project name, version, description, license, and authors.
🔗 It also includes project metadata such as homepage, documentation, and repository URLs.
🔍 The file defines keywords and classifiers to categorize the project.
📦 It lists the packages and their include patterns for packaging.
🐍 The dependencies section lists the required Python version and various libraries.
🔧 The dev-dependencies section is for development-specific dependencies.
📝 The file is written in TOML format.


### `requirements.txt`

📋 This file lists the dependencies required for a language modeling or natural language processing project.


### `trigger_schema.json`

📋 This file is a JSON schema definition for a configuration file. 
🔗 It defines various models and their properties that can be used in the configuration file. 
🔖 The models include actions such as commenting, setting issue title, crawling folders, running bash commands, etc. 
📝 Each action has its own set of inputs and outputs. 
🔀 There are also iterable versions of the actions that can be used to iterate over a list. 
🔄 The file also includes trigger configurations for labels, comments, and push events. 
🔑 The purpose of this file is to provide a standardized schema for defining workflows and actions in a configuration file. 
📖 It allows users to easily create and customize workflows for their projects. 
⚙️ The configuration file can be used by a workflow engine to execute the defined actions based on the trigger events. 
🌟 Overall, this file serves as a blueprint for creating automated workflows for various software development processes.


### `ven`

This folder contains three subfolders: "etc", "include", and "share". The "etc" folder contains a configuration file for enhancing data visualization capabilities. The "include" folder contains a header file that serves as the interface for creating and manipulating greenlets. The "share" folder contains files related to a JavaScript library for creating interactive maps and data visualizations, including configuration files, WebGL setup, and shader programs.


### `workflow_schema.json`

📄 This file is a JSON schema representing a workflow definition.
🔗 It defines various types of actions that can be performed in a workflow.
🌟 These actions include commenting, setting issue titles, crawling folders, running bash commands, committing and pushing to a repository, writing into files, inserting content into text, prompting for input, and reading files.
🔀 The workflow definition allows for conditional branching using if statements and lambda expressions.
📝 Each action has its own set of inputs and outputs.
🛠️ The workflow definition also includes steps that specify the sequence of actions to be executed.
💡 The purpose of this file is to provide a standardized structure for defining and executing workflows.

<!-- Living README Summary -->