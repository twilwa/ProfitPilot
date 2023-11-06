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

This folder contains various files and folders related to a project. It includes configuration files, scripts for web scraping and email drafting, a web application file, license information, a JSON schema for workflow configurations, and a requirements file for Python packages. The files serve different purposes such as configuring program settings, performing web scraping and email drafting tasks, running a web application, defining workflow structures, and specifying required dependencies. The folder provides the necessary components for developing and running the project.


### `.streamlit`

This folder contains a single file called "config.toml". The file serves as a configuration file for a program, defining its theme and UI settings. It specifies a light theme with a primary color of "#356dff" and a hidden sidebar navigation. The file can be modified to change the appearance of the program.


### `EXAMPLE_USAGE.py`

💡 This file is a script that performs several tasks related to web scraping and email drafting. Here's a summary of its purpose:

🔍 It imports modules for email drafting, web scraping, and data parsing.
🔧 It requires service agent and client JSON objects from Google for email functionality.
🔌 The script needs to be piped into "llama" for further processing.
🏭 The script needs to run the scraper before running the drafter.
🕷️ The scraper is activated to collect data from the specified website.
📋 The data is then parsed to extract relevant information.
📊 The scraped data is used to generate a report or draft an email.
📧 The email draft function is called to generate the email using the drafted content.

Note: Some sections of the code are commented out, indicating optional functionality that can be enabled if needed.


### `LICENSE`

✍️ The file contains the license information for the Clarifai, Inc. software.
✍️ It is licensed under the Apache License, Version 2.0.
✍️ The license allows usage of the software in compliance with its terms.
✍️ The license can be obtained from the provided URL.
✍️ The software is distributed on an "AS IS" basis.
✍️ There are no warranties or conditions associated with the software.
✍️ The license specifies the rights and limitations of the software's usage.
✍️ The file is important for understanding the legal aspects of using the software.
✍️ Compliance with the license is required by applicable law.
✍️ The license ensures the software is used responsibly and within legal boundaries.


### `app.py`

🔧 The file is written in Python and uses the Streamlit library.    
📄 It contains code for a web application with two pages: Home and Chat.    
🔗 The user can select a page from the sidebar on the left.    
🏠 If the user selects "Home", a message will be displayed asking them to choose a specific page.    
💬 If the user selects "Chat", an instance of the LlamaClarifaiChat class will be created.    
🤖 The LlamaClarifaiChat class likely contains logic for a chatbot using the Clarifai API.    
💻 The file is using a wide layout for the Streamlit web app.    
✨ There are some commented out lines related to CSS styling.    
🚀 The file's purpose is to serve as the main entry point for the web application.    
💡 It provides an interface for the user to navigate between the Home and Chat pages.


### `docs`

This folder contains two subfolders and one file. The subfolder "PUT_GOOGLE_CREDS_HERE" contains configuration files for authentication and authorization in the Google Cloud Platform. The subfolder "collected_data" contains various files related to a project, including summaries, documentation, and URLs. The file "input.json" is currently empty but can be used for storing information, such as documentation or programming code.


### `example.py`

📝 This file defines variables and creates an instance of the ProfitPilot class. 
🌐 The purpose is to send a cold email introducing a new product to a prospect. 
📧 The email is personalized with the prospect's name and includes information about the company and product. 
🤖 The ProfitPilot instance runs the task, which sends the email using the defined variables. 
👥 The email is sent from a sales representative named John Doe, representing ABC Company. 
💼 The company specializes in software development and values quality, innovation, and customer satisfaction.


### `profit`

This folder contains a variety of files and folders with different purposes. It includes files for setting up an agent that can perform various tasks, such as reading and writing files, processing CSV data, querying websites, and interacting with humans. There are also files for running an email drafting process, creating a chat interface using the Clarifai API, generating text using a pre-trained language model, and implementing a chat interface using Streamlit. Additionally, there are files for a conversational agent template for sales purposes, a collection of tools and functions for data processing and web scraping, and several Python scripts for web scraping and data parsing.


### `pyproject.toml`

🔧 The file is a configuration file for Poetry, a dependency management and packaging tool for Python     
📦 It specifies the required build system and build backend for the project     
📝 The file contains metadata about the project, such as name, version, description, license, authors, and homepage     
🔗 It includes information about the project's repository and documentation     
🔑 Keywords are provided to describe the project's focus and purpose     
🔬 Classifiers are used to categorize the project for different audiences     
📦 The file lists the packages and their inclusion patterns for the project     
🔍 Dependencies are specified for the project, including Python version and various libraries     
🧪 Dev dependencies can be added for development purposes     
💼 The file provides an overview of the project and its dependencies for easy setup and management


### `requirements.txt`

📋 The file contains a list of Python packages and their versions.  
🔍 The packages are related to machine learning, natural language processing, and data manipulation.  
🔧 It seems to be a requirements file for a Python project.  
🔬 The packages included are clarifai-grpc, streamlit, streamlit-chat, pydantic, langchain, openai, transformers, faiss-gpu, langchain-experimental, clarifai, transformers, torch, and pandas.  
🚀 These packages may be used for developing machine learning models, creating interactive web applications, and working with natural language processing tasks.  
⚙️ The specific versions of some packages are specified (faiss-gpu==1.7.2).  
🔧 The file may be used to ensure that the project has the required dependencies installed.  
📚 It is important to have these packages installed in the correct versions to ensure compatibility and functionality.  
💻 Developers or data scientists may refer to this file to set up their development environment or reproduce the project.  
📝 The file can be updated or modified to add or remove packages as per project requirements.


### `trigger_schema.json`

📄 This file is a JSON schema that defines the structure and properties of various action models and trigger configurations. 
🔍 It provides a template for defining different actions that can be performed in a workflow, such as commenting, setting issue titles, crawling folders, running bash commands, etc.
🚀 The schema also includes iterable versions of some actions, allowing them to be performed multiple times in a loop.
💡 It specifies the required inputs, outputs, and parameters for each action, as well as any additional properties or constraints.
🔧 The schema also defines different triggers that can initiate the workflow, such as label triggers, comment triggers, and push triggers.
📋 Each trigger has its own set of properties and configuration options.
🔖 The purpose of this file is to provide a standardized structure for defining and configuring actions and triggers in a workflow automation system.
💻 It serves as a reference for developers and users to understand the available actions and how to configure them correctly.
📝 Developers can use this schema to validate and enforce the structure of action and trigger configurations in their workflows.
🌟 Overall, this file serves as a blueprint for building and configuring automated workflows with different actions and triggers.


### `ven`

This folder contains three subfolders: "etc," "include," and "share." The "etc" folder contains a configuration file for enabling the Pydeck extension in a Jupyter Notebook environment. The "include" folder provides tools and documentation for working with Greenlets in Python, including the necessary interface file. The "share" folder contains JavaScript files used for working with WebGL graphics, including utility functions and shader programs for rendering physically-based materials.


### `workflow_schema.json`

📋 This file is a JSON schema for defining workflow configurations.
🔑 It contains various definitions for different types of actions and declarations used in workflows.
🔗 These definitions can be referenced and used to create complex workflow structures.
🗺️ The `WorkflowDefinition` object is the main structure that defines a workflow.
📚 It includes properties such as name, description, inputs, outputs, and steps.
🚀 Steps can be simple actions or more complex structures like conditionals and nested workflows.
💡 There are predefined action models for actions like commenting, crawling folders, executing bash commands, etc.
🔀 Conditionals can be defined using `IfLambda`, which evaluates a Python lambda expression.
🔗 Workflows can be invoked using `WorkflowInvocation` or `IterableWorkflowInvocation`.
🔁 The file also includes definitions for different types of declarations and inputs used in actions and conditionals.

<!-- Living README Summary -->