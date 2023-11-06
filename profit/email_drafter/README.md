

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains three files: `email_generator.py`, `gmail.py`, and `run.sh`. 

- `email_generator.py` is responsible for running an email drafting process using the OpenAI GPT-3.5 Turbo model. It extracts domain names from URLs, generates draft emails using the OpenAI model, and sends the draft emails using subprocesses.
- `gmail.py` creates and inserts draft emails using the Gmail API. It requires authentication, uses command line arguments to provide email content and recipient information, and interacts with the Gmail API to create drafts.
- `run.sh` is an empty file.


### `__init__.py`

📄 This file appears to be empty.


### `email_generator.py`

📝 This file contains code for running an email drafting process using the OpenAI GPT-3.5 Turbo model.
🔑 It imports necessary libraries and sets up environment variables.
🔍 The `extract_domain_name` function extracts the domain name from a given URL.
🔐 The OpenAI API key is loaded from the environment variables.
📨 The `call_openai` function makes a request to the OpenAI ChatCompletion API to generate a response.
📝 The `run_email_draft` function reads input data, splits it into chunks, and generates a draft email using the OpenAI model.
👥 The company profile and prospect information are combined to create a final report.
📧 The draft email, user email, and email subject are extracted from the response and saved to a file.
📩 The `send_draft_email` function is called to send the draft email using a subprocess.
🔚 The output of the email drafting process is returned as a string.


### `gmail.py`

📝 The purpose of this file is to create and insert a draft email using the Gmail API.
🔑 It requires authentication through credentials stored in token.json and CLIENT_SECRET.json.
📥 The email content, subject, and recipient are provided as command line arguments.
📧 The script uses the Google API client library to interact with the Gmail API.
🔒 The SCOPES variable defines the permissions required for the script to access Gmail.
💾 The draft email is encoded and sent to the Gmail API to create a draft.
📨 The draft's ID and message details are printed as output.
🚫 If an error occurs during the process, it is caught and displayed.
🔁 The script can be executed directly to create the draft email.
📚 The script is dependent on several external libraries and files.


### `run.sh`

💡 This file is empty.

<!-- Living README Summary -->