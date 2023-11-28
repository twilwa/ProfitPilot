

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains three files: `email_generator.py`, `gmail.py`, and `run.sh`. 

`email_generator.py` is a Python script that generates a draft email using the OpenAI ChatCompletion API. It imports necessary modules, reads input data from files, and generates an email based on a predefined schema. The generated email is written to an output file and sent as a draft email using a subprocess.

`gmail.py` is another Python script that uses the Gmail API to create and insert a draft email. It imports necessary modules, retrieves user-specific information, and constructs an email message with the provided content. The script can be executed directly to create and insert a draft email.

`run.sh` is an empty file.


### `__init__.py`

📄 This file appears to be empty.


### `email_generator.py`

📝 This file contains Python code for running an email drafting process using the OpenAI ChatCompletion API.
🔑 It imports necessary modules and sets up the OpenAI API key.
📃 The code defines functions for extracting domain names from URLs and calling the OpenAI ChatCompletion API.
📂 It reads input data from files and splits the text into smaller chunks using a text splitter.
💌 The code generates a draft email based on the collected data and a predefined email schema.
🏢 It includes information about the company and the prospect, and prompts the user to select options for the prospect.
📥 The code writes the generated email to an output file and sends it as a draft email using a subprocess.
📬 The final step is to read and return the content of the output file.



### `gmail.py`

📝 The file contains a Python script for creating and inserting a draft email using the Gmail API.
🔑 It imports necessary modules and libraries for working with Gmail and email messages.
🔧 It retrieves user-specific information such as email addresses and email subject from command line arguments.
🔑 It defines a function `gmail_create_draft()` that handles the creation and insertion of the draft email.
🔑 It checks for existing credentials or prompts the user to log in if necessary.
📧 It constructs an email message with the provided draft email content, recipient, sender, and subject.
🔑 It encodes the email message and creates a draft using the Gmail API.
📝 The draft's ID and message details are printed as output.
⚠️ If an error occurs during the process, an error message is printed.
🔑 The script can be executed directly to create and insert a draft email.


### `run.sh`

📄 This file appears to be empty.

<!-- Living README Summary -->