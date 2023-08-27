

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains Python scripts for web scraping and data parsing. The main script, "main.py", uses the SeleniumWire library to scrape data from web pages in either "scout" or "collect" mode. The "parse_data.py" script uses the BeautifulSoup library to extract information from HTML files and writes the extracted data to separate text files. The "scraper.py" script provides functions for scouting request URLs, grabbing responses, and collecting data. The "setup.bat" file is empty.


### `__init__.py`

📄 This file is empty.


### `main.py`

📝 This file is a Python script that uses the SeleniumWire library to scrape data from web pages.
🌐 It collects data from a target URL and saves it in various formats, such as JSON and HTML.
🔎 The script can be run in two modes: "scout" and "collect". In scout mode, it retrieves the URLs of all requests made by the web page. In collect mode, it also captures the responses received from those requests.
🖥️ The script uses the Chrome webdriver and includes options to disable encoding and verify SSL.
📂 The collected data is saved in the "docs/collected_data" directory, with the results stored in "results.txt" and the HTML content in "html_content.html".
📄 The input URLs are read from a file named "input.txt" located in the "docs" directory.
⚙️ The script also includes a main function that can be called with a specific URL as an argument.
🔧 It provides a command-line interface with an optional argument to set the mode for data collection.
🔒 The script handles exceptions, closes the webdriver after execution, and logs information using the Loguru library.
👀 The script can be customized by modifying the MODE, RESULTS_PATH, HTML_PATH, and INPUT_URL_LIST variables at the top of the file.


### `parse_data.py`

📝 The file contains a Python script for parsing information from an HTML file.
🔍 The script uses the BeautifulSoup library to extract paragraphs and anchors from the HTML content.
📝 It also collects platform information and integrations used in the HTML file.
📁 The collected information is written to separate text files for paragraphs, URLs, contact info, platform info, and integrations.
📄 The script also appends the collected information to a results file.
📝 The script includes functions for writing content to files and for extracting contact information from the HTML.
🔧 The default HTML file path is specified as "./docs/collected_data/html_content.html".
🔧 The default output file paths are specified for paragraphs, URLs, contact info, platform info, and integrations.
🔍 The main function, "parse_info", is called when the script is executed directly.


### `scraper.py`

📝 This file is a Python script that uses the Seleniumwire library to scout or collect data from a target URL. 
🌐 It includes functions to set the mode (scout or collect), scout request URLs, grab responses, and collect data. 
🔗 The main function reads a target URL from a file and performs data collection based on the specified mode. 
📈 The collected data can be saved to files and includes request URLs and HTML content. 
🚀 The script can be run from the command line with optional arguments to specify the mode. 
💻 It uses the argparse library to parse command line arguments. 
🔧 The script also includes a logger for debugging and logging purposes. 
⚙️ The default mode is set to "collect" if no mode is specified. 
🧪 The script is designed to be flexible and can be easily customized for different data collection needs.


### `setup.bat`

📄 This file is empty.

<!-- Living README Summary -->