---
tags:
  - dbms
  - intro_db
---
1. Data refers to raw, unprocessed facts that can be analyzed to make decisions. 
2. It can be 
	1. structured (organized in a specific format like rows and columns),
	2. semi-structured (like JSON or XML), 
	3. unstructured (such as images, videos, and text files).

### Structured Data

1. Is highly organized and easily searchable databases.
2. It confirms to a predefined schema and its typically relational in nature. 
3. Each Column refers to a specific attribute.
4. Each record refers to a specific entry.

Examples:
- **Customer Data**: Name, age, address, email, etc., stored in a table format.
- **Transaction Records**: Date, amount, transaction ID, customer ID.
- **Sensor Data**: Timestamp, sensor value, location. 


**Advantages**:

- **Easily Searchable**: Structured data is easy to query using SQL (Structured Query Language).
- **Efficient Storage**: Since it is stored in a defined schema, structured data can be efficiently stored and accessed.
- **Data Integrity**: Enforcing schemas ensures consistency and integrity across datasets.

**Limitations**:

- **Inflexibility**: It requires a strict schema, which can limit adaptability to new types of data.
- **Data Volume**: Structured data is not always suitable for massive, complex datasets that don't fit neatly into rows and columns.

### Semi-Structured Data

1. Doesn't confirm to a rigid structure but still contains tags, markers to separate elements and define hierarchy. 

Examples:

- **JSON (JavaScript Object Notation)**: Widely used in web applications and APIs to transmit data between client and server.
- **XML (Extensible Markup Language)**: Used in configuration files, data interchange formats, and document structures.
- **YAML**: A human-readable data serialization format often used for configuration files.

**Advantages**:
- **Flexibility**: It allows for more fluid structures, making it adaptable for storing complex, hierarchical data.
- **Interoperability**: Formats like JSON and XML are platform-independent and can be used across various systems.
- **Widely Used**: Semi-structured data is common in data exchanges between applications, making it crucial for web services and cloud computing.

**Limitations**
- **Complex Querying**: Semi-structured data may require specialized tools or languages (like XPath for XML) to query and extract insights.
- **Potential for Inconsistency**: Since there is no strict schema, data may lack the same level of consistency found in structured datasets.

### Unstructured Data 
1. Doesn’t have a predefined data model or organization.
2. Typically requires significant preprocessing and sophisticated analysis methods to extract meaningful information.

Examples:
- **Text Data**: Emails, social media posts, news articles, and documents.
- **Multimedia**: Images, videos, audio files.
- **Log Files**: Machine logs, error reports, and system performance data.
- **Emails**: A combination of text and metadata (like sender, subject, and timestamps).

**Advantages**:
- **Richness of Information**: Unstructured data contains vast amounts of detailed, real-world information, offering deep insights when analyzed properly.
- **Availability**: Most data generated today, such as social media content or web interactions, is unstructured.
- **Diverse Applications**: Unstructured data can be used for sentiment analysis, image recognition, natural language processing (NLP), etc.

**Limitations**:
- **Complex Storage and Processing**: Managing unstructured data requires advanced techniques, such as data lakes and specialized databases like Hadoop.
- **Difficult to Analyze**: Requires advanced algorithms and machine learning techniques to parse, categorize, and analyze data effectively.
- **Costly**: Analyzing and processing unstructured data can be resource-intensive, both in terms of computing power and expertise.