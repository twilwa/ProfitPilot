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

This folder contains various files and folders related to different functionalities. It includes configuration files for Streamlit and Google API clients, scripts for web scraping and email drafting, license information for Clarifai, Inc., and files for running the ProfitPilot program, managing conversations with prospects, generating email drafts, providing a chat interface with an AI assistant, and performing data processing and web scraping tasks. Additionally, there are files for defining trigger configurations and workflows, as well as configuration files for Jupyter notebooks. The folder represents a collection of resources for language processing, machine learning, and web application development.


### `.streamlit`

This folder contains a configuration file named config.toml. It is used to define the theme and UI settings for an application. The file specifies that the base theme is set to "light", the primary color is set to "#356dff", and the sidebar navigation is hidden in the UI.


### `EXAMPLE_USAGE.py`

📋 This file is a script that combines various modules to perform specific tasks. 
🔍 It includes imports from different packages for functionality.
🔧 The purpose of this script is to scrape data from a specific website using a web scraper module.
📊 The scraped data is then used to generate a report or draft an email using other modules.
🔑 Service agent and client JSON objects from Google are required for email functionality.
🐪 The result of the script is piped into "LLAMA".
🔁 The script includes commented-out code for web scraping and generating reports, which can be uncommented and executed as needed.
📧 The main function "draft_email" is responsible for drafting the email.
🌐 The web scraper is set to scrape data from "https://huggingface.co/".


### `LICENSE`

📄 This file contains the license information for Clarifai, Inc.
🔒 It is licensed under the Apache License, Version 2.0.
📝 The license allows usage of the file in compliance with the license terms.
🔗 The license can be obtained from the provided URL.
💻 The file pertains to software distributed by Clarifai, Inc.
🚫 There are no warranties or conditions associated with the software.
📚 The license covers the specific language and limitations of use.
📝 The file is important for understanding the legal usage of the software.
🔐 Compliance with the license is required by applicable law.
📝 The license is crucial for understanding the limitations and rights granted.


### `app.py`

📝 This file is a Python script.  
🔧 It uses the Streamlit library for creating interactive web applications.  
📚 It imports a module called "LlamaClarifaiChat" from a package called "profit.llamachat".  
🔧 The script sets the page configuration of the Streamlit app to a wide layout.  
🔧 It defines a sidebar with two options: "Home" and "Chat".  
🔀 Depending on the user's choice, it either displays a message or instantiates the "LlamaClarifaiChat" class.


### `docs`

This folder contains configuration files for Google API clients, including client settings and service account credentials. It also contains various files related to different topics, such as a Python script for web scraping, documents discussing contextual compression, and a list of URLs and file paths. Additionally, there is an empty input.json file.


### `example.py`

📝 This file sets up a ProfitPilot instance to perform a sales-related task.
🤖 The ProfitPilot class is imported from the profit.main module.
🔧 Various variables are defined to configure the ProfitPilot instance.
📧 An email task is created, customized with the defined variables.
🚀 The task is then executed using the ProfitPilot instance.



### `profit`

This folder contains files and folders related to various functionalities. It includes files for running the ProfitPilot program, an autonomous agent, email drafting, a chat interface, text generation, and web scraping. The files serve different purposes such as initializing and configuring the program, managing conversations with prospects, generating email drafts, providing a chat interface with an AI assistant, and performing data processing and web scraping tasks.


### `pyproject.toml`

🏢 The file is a configuration file for a Python project.
📦 It uses Poetry as the build system and specifies its requirements.
🔧 The file defines the project name, version, description, license, and authors.
🌐 It includes links to the project's homepage, documentation, readme, and repository.
🔑 The file specifies keywords and classifiers for the project.
📦 It lists the packages and their inclusion patterns.
🐍 The file defines the project's dependencies and dev-dependencies.



### `requirements.txt`

🔍 This file contains a list of Python packages.    
✨ The packages listed here serve various purposes.    
📦 Some packages are related to natural language processing and machine learning, such as `openai`, `transformers`, and `torch`.    
💡 Other packages include `clarifai` for image recognition and `faiss-gpu` for fast similarity search.    
🔧 There are also utility packages like `pydantic` for data validation and `pandas` for data manipulation.    
🌐 `streamlit` and `streamlit-chat` are frameworks for building interactive web applications.    
🚀 `langchain` and `langchain-experimental` are likely custom packages for language-related tasks.    
📋 Overall, this file represents the dependencies needed for a Python project with a focus on language processing, machine learning, and web application development.


### `trigger_schema.json`

📋 This file is a JSON schema definition for a trigger configuration model. 
🔍 It defines various types of triggers and their properties. 
💡 The triggers include label triggers, comment triggers, and push triggers. 
🚀 Each trigger has specific fields and actions associated with it. 
📝 The schema also defines different types of actions such as commenting, setting issue titles, crawling folders, running bash commands, etc. 
🔧 Each action has its own set of inputs and outputs. 
🔀 The schema allows for iterating over actions and defining parameters. 
📑 The top-level trigger configuration model contains an array of triggers. 
💼 The purpose of this file is to provide a standardized schema for defining triggers and actions in a workflow or automation system.


### `ven`

This folder contains files related to the configuration and functionality of Jupyter notebooks. It includes a configuration file for enabling the pydeck extension, a file defining the interface for the Greenlet object in Python, and JavaScript files that enhance data visualization capabilities in Jupyter notebooks.


### `workflow_schema.json`

📋 This file is a JSON schema for defining workflows.
🔢 It contains definitions for various types of actions that can be performed in a workflow.
🔀 Actions include commenting on an issue, crawling a folder, executing a bash command, and more.
🔄 Workflows can be defined as a sequence of steps, where each step can be an action or another workflow.
✏️ Inputs and outputs can be specified for workflows and actions.
🔂 Workflows can also include conditional logic and iteration.
🚀 Overall, this file provides a structured way to define and configure workflows for automation.

<!-- Living README Summary -->