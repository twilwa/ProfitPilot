

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains a file named greenlet.h which serves as the interface for working with Greenlets in Python through the C API. It includes necessary headers, defines macros for accessing C API functions, and provides documentation for each function's usage. The file also sets up necessary macros and imports the Greenlet module if it is not already defined. Overall, this folder is focused on providing the necessary tools and documentation for working with Greenlets in Python.


### `greenlet.h`

📄 This file defines the interface for the Greenlet object in Python.
🔒 It includes the necessary headers and provides C API functions for working with Greenlets.
🔧 The Greenlet struct contains a weak reference list, a dictionary, and an implementation pointer.
🔢 The file defines macros for checking if an object is a Greenlet and for accessing specific C API functions.
🚫 There are also macros for defining exceptions related to Greenlets.
📝 The file provides documentation for each C API function and their usage.
🔌 If the GREENLET_MODULE is not defined, the file sets up the necessary macros and imports the Greenlet module.
⚠️ The file also includes some deprecated and undocumented aliases for certain C API functions.
🔄 The PyGreenlet_Import macro is used to import the Greenlet module and initialize the C API.
📚 Overall, this file serves as the interface for working with Greenlets in Python through the C API.

<!-- Living README Summary -->