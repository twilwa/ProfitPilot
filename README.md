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

This folder contains files and folders related to an application called "ProfitPilot". It includes configuration files for Docker and Streamlit, as well as code files for running tasks and automating sales outreach. There are also folders for documentation, AI agent files, and project dependencies. The files and folders serve different purposes such as defining the application's theme and UI settings, setting up a Python environment, generating emails, integrating with Google APIs, and providing instructions and summaries for various topics.


### `.streamlit`

This folder contains a configuration file, `config.toml`, which is used to define the theme and UI settings for an application. The file specifies the base theme, primary color, and whether the sidebar navigation should be hidden or not.


### `Dockerfile`

🐍 This Dockerfile sets up a Python environment for running an application.  
📁 It sets the working directory to `/app` in the container.  
📥 It copies the contents of the current directory into the container at `/app`.  
🛠️ It installs required tools and dependencies.  
📦 It installs various Python packages using pip.  
🔌 It exposes port 80 for the application to run on.  
📜 It specifies the command to run the application (`example.py`).


### `LICENSE`

📝 This file contains the license information for the software.     
⚖️ It is licensed under the Apache License, Version 2.0.     
📜 The license can be obtained from the provided link.     
🔒 The software is distributed under the license on an "AS IS" basis.     
🚫 No warranties or conditions are provided.     
📚 The license specifies the rights and limitations for using the software.     
📅 The copyright is held by Clarifai, Inc.     
📝 The purpose of the file is to provide legal information for the software.     
🔑 Compliance with the license is required to use the software.     
🗒️ The file does not contain any code or implementation details.    


### `app.py`

📝 This file defines variables and creates an instance of the ProfitPilot class.
📧 It generates an email task to introduce a new product to a prospect.
🚀 The purpose is to automate and streamline the sales outreach process.
👥 The email is personalized with the prospect's name and the salesperson's name.
📩 The task is then executed using the ProfitPilot instance.
🔍 The email content includes information about the company's specialization and values.
💼 The email aims to explore how the new product can benefit the prospect's team.
📌 The file can be customized with different variables for different sales scenarios.
⚙️ The ProfitPilot class handles the execution of tasks and can be extended for more complex sales automation.


### `docker-compose.yml`

🏭 This file is used to define a Docker Compose configuration for a service.     
🔨 The service is named "app".     
🐳 It will be built using the specified Dockerfile in the current directory.     
🌐 The service will be accessible on port 8501 of the host machine.     
💾 The current directory will be mounted as a volume inside the container.     
🔧 An environment variable STREAMLIT_SERVER_PORT will be set to 8501.


### `docs`

This folder contains files related to Google API integration, contact information collection, data analysis automation, system integration, and documentation. Some files are credentials for Google API integration, while others provide information, instructions, and summaries for their respective topics. Some files are currently empty or need to be populated.


### `example.ipynb`

📁 This file contains code for cloning a GitHub repository.     
📦 It installs the required dependencies.     
🏎️ It contains an example script to run.     
🔍 The purpose of the file is to demonstrate the usage of ProfitPilot.     
🌐 The GitHub repository is located at https://github.com/kyegomez/ProfitPilot.git.


### `example.py`

📝 This file defines variables and creates an instance of the ProfitPilot class. 
📧 The purpose of the file is to run a task using the ProfitPilot instance, which involves sending a cold email to a prospect. 
🌐 The email introduces the prospect to the company's newest product and aims to explore potential benefits for the prospect's team. 
🔧 The file includes variables for customizing the email content, such as the names, company information, and values. 
💼 The ProfitPilot class is responsible for automating the task and running the email using the defined variables.


### `profit`

This folder contains files related to an AI agent called "ProfitPilot" and its supporting classes and tools. The "agent.py" file defines the main Agent class, which can perform various tasks using tools like reading and writing files, processing CSV data, querying websites, drafting emails, and scraping data. The "llama.py" file provides a wrapper for a language model called "LLama2" and allows for text generation based on a given prompt. The "main.py" file contains the ProfitPilot class, which interacts with users through conversations. The "tools.py" file provides a collection of tools for data processing, web scraping, and web querying.


### `pyproject.toml`

🔧 This file is a configuration file for a Python project.
📦 It uses Poetry as the build system.
🏷️ The project name is "ProfitPilot" with version 0.0.3.
📚 The project is described as "ProfitPilot - AI Agents" and is licensed under MIT.
👥 The author of the project is Kye Gomez with the email kye@apac.ai.
🌐 The project homepage is "https://github.com/kyegomez/ProfitPilot".
📦 It lists the dependencies and dev-dependencies required for the project.
🔍 The project has keywords related to artificial intelligence, deep learning, optimizers, and Prompt Engineering.
🐍 The project requires Python version 3.6 or higher.
🗃️ The project uses various libraries including clarifai, streamlit, langchain, transformers, pydantic, openai, faiss-gpu, torch, and pandas.


### `requirements.txt`

📋 This file contains a list of Python packages and libraries that are being used in a project.
📦 The packages listed here are related to natural language processing (NLP) and machine learning.
💡 The purpose of this file is to document the dependencies required for the project.
🔍 It provides a quick overview of the key libraries being utilized.
🔧 The listed packages include langchain, transformers, faiss-gpu, langchain-experimental, torch, pandas, and sentencepiece.
✅ These libraries are likely used for tasks such as language translation, text classification, and data manipulation.
🚀 They enable the project to leverage advanced NLP and machine learning capabilities.
👩‍💻 Developers can refer to this file to ensure they have the necessary packages installed.
📄 It serves as a handy reference document for managing the project's dependencies.


### `trigger_schema.json`

📝 This file is a JSON schema definition for a configuration file.
📑 It defines various action models and trigger models for a workflow.
🔀 The trigger models include LabelTrigger, CommentTrigger, and PushTrigger.
🔀 The action models include comment, set_issue_title, crawl_folder, bash, commit_and_push, write_into_file, insert_content_into_text, prompt, read_file, summarize_pr, reformat_results, summarize_file, summarize_folder, generate_summary, generate_readme_summaries, and insert_into_readme.
📋 Each action model has specific inputs and outputs defined.
💡 The purpose of this file is to provide a structured way to define and configure actions and triggers for a workflow.
🔧 It allows users to define and customize their own workflow by combining different actions and triggers.
📂 The workflow can be triggered by events like label creation, comment creation, or push to a specific branch.
🔗 The configuration file serves as a blueprint for defining the behavior and actions of the workflow.


### `ven`

This folder contains three subfolders. The "etc" folder contains a configuration file for the PyDeck extension, which enables PyDeck visualizations. The "include" folder contains a C API file for the Greenlet object, used for lightweight cooperative multitasking in Python. The "share" folder contains JavaScript files for a WebGL rendering project, including files for configuring libraries, rendering graphics, and implementing physically-based rendering with lighting and textures.


### `workflow_schema.json`

📝 This file contains a JSON representation of a workflow definition. It defines a workflow with multiple steps and allows for the execution of actions like commenting, crawling folders, executing bash commands, and more. The workflow can be invoked with inputs and produces outputs. It also supports conditional branching and iteration.

<!-- Living README Summary -->