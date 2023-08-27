

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains scripts and files related to generating and sending sales emails for a start-up called Move Right. The `email_generator.py` script uses the OpenAI API to generate email content based on input examples and system instructions, and then calls the `gmail.py` script to send the draft email using Gmail. The `marketing_report.py` script is for running a marketing report by retrieving data from a company's website and summarizing it using OpenAI's Chat API. The `url_parse.py` script extracts the domain name from a given URL. The `run.sh` file is currently empty and serves no purpose.


### `__init__.py`

📦 This file contains two imported scripts: "marketing_report" and "url_parse"
🔍 The purpose of this file is to provide a list of the scripts available for use



### `email_generator.py`

💡 This file is an executable script that generates and sends draft sales emails to prospects for a start-up called Move Right.
💡 It uses the OpenAI API and a chat model to generate the email content based on input examples and system instructions.
💡 The script reads the input text from a file, splits it into chunks, and passes it to the chat model for generating the email response.
💡 The generated email, along with the user's email and subject, are written to an output file.
💡 The script then calls another script to send the draft email using Gmail.
💡 The purpose of this file is to automate the process of drafting and sending sales emails to prospects for Move Right.
💡 It utilizes the OpenAI API and follows specific guidelines for tone, language, and response format.
💡 The input examples and system instructions can be customized to tailor the email generation process.
💡 The file requires the OpenAI API key and dotenv library for loading environment variables.
💡 The script assumes the presence of input and output files in a specific directory structure.


### `gmail.py`

📝 This file is a Python script for creating and inserting a draft email in Gmail.
📧 It uses the Gmail API to authenticate and interact with the user's Gmail account.
🔑 The script requires user credentials and token files to authorize access to the Gmail API.
📥 The script takes command-line arguments for the draft email subject, user email, and draft email content.
✉️ The draft email is created with the specified subject, recipient, and content.
🔒 The email message is encoded and sent as a raw message using the Gmail API.
💾 The draft email is saved in the user's Gmail drafts folder.
🚀 The script prints the ID and message details of the created draft email.
❌ If any errors occur during the process, they are printed to the console.
💡 The script can be customized and extended for different use cases involving Gmail draft emails.


### `marketing_report.py`

📋 This file is a Python script for running a marketing report.
🔑 It imports various modules and defines functions.
🔍 The main function, `run_marketing_report`, takes a company path as input.
🌐 It retrieves data from the company's website and splits it into documents.
📝 It then generates prompts and uses OpenAI's Chat API to summarize the documents.
💾 The output summary is saved to a file.
📝 There are commented-out sections for iterating over a list of companies.
🔧 The script requires the dotenv and pandas libraries, as well as other custom modules.
🚀 The script can be executed directly to run the marketing report for a specific company.


### `run.sh`

📄 The file is currently empty    
🤷‍♂️ There is no content or code in the file    
👀 This file serves no purpose at the moment    
🔒 No information or functionality is present in the file    
📝 It is a blank slate, ready for use    
💡 The file is waiting to be populated with content    
🚫 No data or code has been written in the file    
💤 The file is currently dormant or inactive    
👥 It is a placeholder file with no specific purpose    
❌ The file does not contain any information or instructions


### `url_parse.py`

📄 This file contains a function to extract the domain name from a given URL.

<!-- Living README Summary -->