

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains a collection of Python files that provide modules and classes for various language processing tasks. The files include a module for vector database operations, a class for selecting and retrieving text embeddings, a class for selecting different types of document loaders, a class for selecting and initializing retrievers for language processing tasks, a base selector class for managing options, a module for defining and selecting text splitters, and a class for managing a vector store. These files provide a flexible and modular way to perform language processing tasks such as embedding selection, document loading, text retrieval, option selection, text splitting, and vector storage.


### `__init__.py`

📁 This file contains a module for vector database operations.


### `embeddings.py`

📝 This file defines a class called `EmbeddingSelector` that is used to select and retrieve different types of text embeddings. 
🔑 It utilizes the `openai` library to access OpenAI text embeddings and the `sentence-transformers` library for Sentence Transformer embeddings.
🔌 The class allows the user to specify the default embedding option when initializing an instance.
📚 It provides methods to retrieve OpenAI embeddings and Sentence Transformer embeddings.
🔧 The file also sets up the necessary configurations for the embeddings, such as API keys and model parameters.
🗃️ The class extends a base selector class and utilizes an enum to store the available embedding options.
📊 The progress bar and request timeout settings can be adjusted for the embeddings.
🔎 The logger module is used for logging informational messages during the initialization and retrieval of embeddings.
💡 The purpose of this file is to provide a convenient way to select and retrieve different types of text embeddings for natural language processing tasks.


### `loaders.py`

📚 This file contains the definition of a LoaderSelector class.
📝 The class is used to select different types of document loaders based on user preferences.
🔍 It provides methods to retrieve specific loaders such as PyPDFLoader, UnstructuredMarkdownLoader, etc.
📌 The default loader can be set during initialization.
🔧 The class initializes logger and maps the loader options.
📑 It also contains getter methods for each loader option.
🌐 The loaders can be used to load documents from various sources like PDF, markdown, text, Python code, directories, and Playwright URLs.
🔗 The LoaderOptions enum defines the available loader options.
📖 The purpose of this file is to provide a flexible way of selecting and retrieving document loaders.


### `retrivers.py`

📝 This file contains a class called "RetrieverSelector" which is used for selecting and initializing different types of retrievers for language processing tasks.
📥 It imports various retriever classes from the "langchain.retrievers" module.
📥 It also imports the "Enum" class from the "enum" module and the "logger" class from the "loguru" module.
📥 It imports the "BaseSelector" class from the "vectordb.selector" module.
🔧 The "RetrieverOptions" class is an enumeration that defines different options for retrievers.
🔧 The "RetrieverSelector" class initializes and manages the selection of retrievers based on the specified options.
🔍 It has methods for retrieving specific types of retrievers, such as "get_self_query_retriever", "get_ensemble_retriever", and "get_contextual_compression_retriever".
🖊️ The logger is used to log information during the initialization and retrieval process.
📥 This file serves as a part of a larger system for language processing and retrieval tasks.
🔧 It provides a flexible and extensible way to select and use different retrievers based on the specific requirements of the task.


### `selector.py`

📝 The file contains a class called BaseSelector.  
🔧 The purpose of the class is to provide functionality for selecting and managing options.  
📌 It has methods for initializing option maps, selecting options, adding new options, and retrieving the current option map and index.  
📜 It also includes logging statements using the loguru library.  
🔑 The class uses a dictionary to map option names to option objects.  
💡 The class stores the current selected option in an attribute called "embedding".  
🔍 The "select" method allows selecting an option by its name.  
🔧 The "add" method allows adding a new option.  
📊 The "get_maps" method returns the current option map and index as a tuple.


### `splitters.py`

📄 This file defines various text splitters and a splitter selector class.
🔀 The text splitters are used to split text into smaller units based on different criteria.
🔧 The splitter selector class provides methods to retrieve specific text splitters.
📝 The file also includes necessary imports and a logger.
🔍 The purpose of the file is to provide a modular and customizable way to split text.
💡 The text splitters can be used in various natural language processing tasks.
📚 The file utilizes an enum for easy selection of different text splitters.
🔀 The default text splitter can be specified when creating an instance of the splitter selector class.
📝 The logger is used to provide information about which splitter is being retrieved.
🔗 The file can be extended by adding new text splitters to the enum and implementing corresponding methods in the splitter selector class.


### `vectorstore.py`

🔧 This file defines a class called VectorStore.

<!-- Living README Summary -->