# Flask Template Project

## Overview

This project is a robust Flask template using Poetry for dependency management. It provides a solid foundation for building Flask-based web applications with a well-organized structure, CORS support, and integrated testing.
Features

🐍 Python 3.9+
🌶️ Flask web framework
🎭 Flask-CORS for handling Cross-Origin Resource Sharing (CORS)
📦 Poetry for dependency management
🧪 pytest for unit testing
🏗️ Modular project structure
🚀 Ready-to-use API endpoints

### Prerequisites

Before you begin, ensure you have the following installed on your system:

Python 3.9 or higher
Poetry

Quick Start

Clone the repository:
Copygit clone https://github.com/yourusername/flask-template.git
cd flask-template

Install dependencies:
Copypoetry install

Run the application:
Copypoetry run python run.py

Access the application at http://localhost:5000

Project Structure
Copyflask-template/
├── pyproject.toml
├── README.md
├── run.py
├── flask_template/
│ ├── **init**.py
│ ├── app.py
│ └── routes/
│ └── **init**.py
└── tests/
├── **init**.py
└── test_app.py
API Endpoints

GET /: Returns a "Hello, World!" message
GET /api/data: Returns a sample data array

Running Tests
To run the test suite:
Copypoetry run pytest
Development

Activate the Poetry shell:
Copypoetry shell

Run the application in debug mode:
Copypython run.py

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
This project is open source and available under the MIT License.
