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

This folder contains files related to the ProfitPilot project, which is an AI-based application for managing sales leads and generating personalized deal flow. The main files include "app.py" and "example.py" which contain the code for running the ProfitPilot application and sending personalized email introductions to prospects. There is also a Dockerfile and docker-compose.yml file for containerizing the application, as well as other configuration and utility files. The project uses various Python libraries and packages, and includes a JSON schema for defining workflows and trigger configurations. Overall, the folder contains the necessary files to set up and run the ProfitPilot project.


### `.streamlit`

This folder contains a single file called "config.toml" which is a configuration file. It defines the base theme as "light" and the primary color as "#356dff". It also hides the sidebar navigation in the user interface.


### `Dockerfile`

🔧 This file is a Dockerfile for creating a Docker image.  
📦 It sets the parent image as Python 3.8-slim.  
📁 The working directory is set to /app in the Docker image.  
📂 The current directory contents are copied into the /app directory of the container.  
🔧 Required tools and dependencies are installed using apt-get.  
📦 Various Python packages are installed using pip.  
🔓 Port 80 is exposed for the application to run on.  
🚀 The command to run the application is specified as "python3 example.py".  



### `LICENSE`

📄 This file contains the license information for the software.     
🔒 It is licensed under the Apache License, Version 2.0.     
📋 The license grants permissions and sets limitations for using the software.     
💻 The file is important for understanding the terms and conditions of use.     
🚫 It is necessary to comply with the license when using the software.     
📜 The license can be obtained from the provided URL.     
🔐 The license ensures that the software is distributed on an "AS IS" basis.     
🔍 The license does not provide any warranties or conditions.     
📝 The file is crucial for legal compliance and understanding the rights and limitations.     
💡 It is recommended to read and understand the license before using the software.     


### `app.py`

📝 The file contains code written in Python using the Streamlit library.  
📊 The purpose of the file is to create an interactive web application called "ProfitPilot" for managing sales leads and generating personalized deal flow.  
🔧 The file imports modules and defines variables necessary for the ProfitPilot class.  
📧 The file also includes a task definition for sending personalized email introductions to prospects.  
💼 The main function sets up the Streamlit interface and allows users to run the ProfitPilot.  
🚀 When the "Run" button is clicked, the ProfitPilot runs the task and displays the response.  
💬 Users can also input their own response and click the "Send" button to get a response from ProfitPilot.  
📝 The ProfitPilot class is instantiated with the defined variables.  
🔁 The main function is called to run the ProfitPilot.  
📩 The ProfitPilot sends personalized email introductions to prospects based on the defined task.


### `docker-compose.yml`

🏢 This file is a docker-compose file written in version 3.8. 
🐳 It defines a service called "app" that will be built using the specified Dockerfile. 
🔌 The service will expose port 8501 on the host and container. 
💾 It will mount the current directory to the /app directory inside the container. 
🌐 The service will run a Streamlit server on port 8501.


### `example.ipynb`

📁 The file contains commands to clone a GitHub repository
🔧 It installs the required dependencies using pip3
🚀 It runs an example Python script called "example.py"
👥 The purpose of the file is to set up and run the ProfitPilot project
💻 It is likely part of a larger project or workflow



### `example.py`

📝 This file is a script that uses the ProfitPilot class to send a cold email introducing a new product to a prospect. 
🔧 It sets up various variables and creates an instance of the ProfitPilot class.
📧 The email content is defined in the 'task' variable using string formatting.
🚀 The 'pilot.run(task)' command executes the email task using the ProfitPilot instance.
💼 The script can be customized with different values for variables like AI name, company name, salesperson name, etc.
🌐 It can be used for sales representatives to automate and personalize cold email outreach.
📩 The email subject and content can be easily adjusted for different prospects.
⚙️ The ProfitPilot class likely includes functionality to send the email through an email service or API.
🔑 An OpenAI API key is required for the script to work.
👩‍💼 The script assumes that the recipient's name is provided in the 'PROSPECT_NAME' variable.


### `profit`

This folder contains files related to an AI chatbot and an autonomous agent. The main files are "__init__.py" which initializes and runs the ProfitPilot application, "agent.py" which defines the Agent class for the chatbot, "clarifi.py" which uses the Clarifai model to generate responses, "clarifi_agent.py" which provides a framework for creating and running autonomous agents, "llama.py" which provides a wrapper for the LLama language model, and "main.py" which serves as an interface for running the AI agent in a sales context. There are also utility files such as "tools.py" for processing CSV files and querying web pages.


### `pyproject.toml`

📋 This file is a configuration file for a Python project. 
📦 It uses Poetry as the build system and package manager. 
🔧 The project is named "ProfitPilot" and is at version 0.2.8. 
📝 It is a collection of AI agents for profit optimization. 
🔑 The project is licensed under MIT and has authors listed. 
🏠 The homepage and repository are hosted on GitHub. 
📚 There is no documentation mentioned. 
🔍 The project has keywords and classifiers defined. 
📦 It has several dependencies and dev-dependencies listed.


### `requirements.txt`

📁 The file contains a list of Python libraries and packages.  
🔍 It includes libraries for natural language processing (NLP) like transformers, langchain, and sentencepiece.  
🔥 It also includes faiss-gpu, which is a GPU-accelerated library for similarity search.  
📚 The file includes torch, a popular deep learning framework.  
🐼 pandas is included for data manipulation and analysis.  
🌐 There are several packages related to Google APIs, such as google-api-python-client, google-auth-oauthlib, and google-auth-httplib2.  
🔑 The file includes beautifulsoup4, a library for web scraping.  
🖼️ clarifai is included, which is an AI platform for image and video recognition.  
🚀 langchain-experimental==0.0.10 is a specific version of the langchain experimental library.  
🎯 tiktoken is included, which is a tokenization library.


### `trigger_schema.json`

💡 This file is a JSON schema that defines the structure and properties of various action models and trigger configurations. It provides a template for defining different actions and triggers in a workflow or automation system.


### `ven`

This folder contains configuration files and code related to various Python packages and widgets. The "pydeck.json" file enables the "pydeck" extension in a Python package, allowing for interactive data visualization. The "greenlet.h" file defines the interface for the Greenlet object, which is used for lightweight multitasking in Python. The JavaScript files in the "jupyter" folder configure and provide functionality for a Jupyter widget called "@deck.gl/jupyter-widget", which enables physically based rendering (PBR) features for mapping and visualization.


### `workflow_schema.json`

📝 The file is a JSON schema representing a workflow definition.
📝 It defines various types of actions that can be performed in a workflow.
📝 Each action has its own set of properties and can be invoked in a step of the workflow.
📝 The workflow can also include conditional statements and iterations.
📝 The schema provides a structured way to define and validate workflows.
📝 The purpose of the file is to serve as a template for creating and managing workflows.
📝 It allows users to define the inputs, outputs, steps, and conditions for their workflows.
📝 The file can be used by workflow management systems to automate and orchestrate complex processes.
📝 It provides a standardized format for defining workflows across different platforms and tools.
📝 The file can be customized and extended to meet specific workflow requirements.

<!-- Living README Summary -->