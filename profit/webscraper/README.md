

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains several Python scripts for web scraping and data parsing. The "main.py" script uses the SeleniumWire library to collect data from a target URL, while the "parse_data.py" script is used for parsing information from an HTML file. The "scraper.py" script is another web scraping script that uses Selenium Wire, and the "setup.bat" file is empty.


### `__init__.py`

📄 This file is empty
🔍 It does not contain any code or content
❌ There are no imports or functions defined
📝 Its purpose is yet to be determined
💡 It could be a placeholder or template file
🔒 It might be a starting point for future development
⚠️ Please consult the project requirements for further information
👀 This file is intended for someone new to the project
👌 Feel free to modify or delete it as needed


### `main.py`

📝 This file contains a Python script that uses the SeleniumWire library to collect data from a target URL.
🔍 The script can be run in two modes: "scout" and "collect".
🌐 In "scout" mode, the script visits the target URL, saves the HTML content, and logs the URLs of all requests made by the page.
📊 In "collect" mode, the script does the same as "scout" mode, but also saves the responses received from the requests in a JSON file.
🖥️ The script uses the Chrome webdriver and the loguru library for logging.
📑 The target URL can be provided as a command-line argument or read from a file.
🔧 The script can be customized by modifying the global variables at the beginning of the file.
⚙️ The script can be executed directly or imported as a module.
📖 Detailed documentation of the script's functionality can be found in the comments within the code.


### `parse_data.py`

📋 This file contains a script for parsing information from an HTML file.
🔍 The script uses the BeautifulSoup library to extract paragraphs and anchors from the HTML content.
📝 It also collects platform information and integrations mentioned in the HTML.
📞 Additionally, it searches for contact information such as email addresses, phone numbers, and addresses.
📂 The collected data is then written to separate text files.
🧩 The script supports the collection of data from WordPress, Shopify, Google Analytics, Facebook, Twitter, LinkedIn, Pinterest, YouTube, SalesForce, HubSpot, Wix, and Squarespace platforms.
🔗 It also identifies integrations like Google Analytics, Facebook, Twitter, LinkedIn, Pinterest, YouTube, SalesForce, HubSpot, Wix, Squarespace, Shopify, and WordPress.
📝 The main function of the script is `parse_info`, which takes an optional HTML file path as input and returns the collected data as a string.
🔍 The script can be executed independently when run as a standalone file.


### `scraper.py`

📄 This file contains a Python script for scraping data from web pages using Selenium Wire.
🌐 The script uses the Chrome driver to interact with web pages and collect information.
🔍 It has two modes: "scout" and "collect".
🎯 In "scout" mode, it visits a target URL and saves the HTML content and the URLs of all requests made.
💾 In "collect" mode, it also saves the responses received from the requests as JSON.
🔧 The script can be run from the command line with optional arguments to specify the mode.
⚙️ The target URL can be provided as a command line argument or read from a file.
📝 The collected data is saved in separate files for the responses and the HTML content.
🔽 The script uses various libraries such as Selenium Wire, loguru, and argparse for functionality and logging.
👀 The main function is called when the script is run directly and it handles the execution flow.


### `setup.bat`

📄 This file is empty.

<!-- Living README Summary -->