

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains three files: `email_generator.py`, `gmail.py`, and `run.sh`. 

`email_generator.py` is a script that generates email drafts using the OpenAI ChatCompletion API. It reads input data, splits it into chunks, and processes the result. The extracted information is written to an output file and used to send a draft email using `gmail.py`.

`gmail.py` is a script that creates and inserts a draft email using the Gmail API. It handles authentication and authorization, and takes command-line arguments for the draft email subject, user email, and content. It interacts with the Gmail API to create a draft email.

`run.sh` is an empty file.


### `__init__.py`

📄 This file appears to be empty.


### `email_generator.py`

📄 This file contains code for running an email drafting process.
🔑 It imports various libraries and sets up the necessary environment variables.
🔗 It defines functions for extracting domain names from URLs and calling the OpenAI ChatCompletion API.
📝 The `run_email_draft()` function reads input data, splits it into chunks, and generates email drafts using the OpenAI model.
🔍 It also includes a JSON schema for the expected response format and a profile of a company.
🧩 The final result is processed, and the user email, draft email, and subject are extracted.
📧 The extracted information is written to an output file and then used to send a draft email using a separate script.
🔁 The draft email sending process is executed in a separate subprocess.
✔️ The output file is read and returned as the final result of the script.



### `gmail.py`

📝 This file is a script for creating and inserting a draft email using the Gmail API.
🔒 It handles authentication and authorization using Google OAuth2 credentials.
📧 The script takes command-line arguments for the draft email subject, user email, and draft email content.
🔑 It requires a token.json file for storing access and refresh tokens.
🔧 The script uses the `googleapiclient` library to interact with the Gmail API.
✉️ It creates an `EmailMessage` object, sets the content, recipient, sender, and subject, and encodes the message.
📨 The encoded message is then passed to the Gmail API to create a draft.
🔍 If any errors occur during the process, they are caught and displayed.
🔙 The created draft's ID and message details are printed.
🔁 The script can be executed directly to create a draft email.


### `run.sh`

📄 This file is empty.

<!-- Living README Summary -->