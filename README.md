
# White Box Testing Project

## 📝 Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Viewing Coverage Report](#viewing-coverage-report)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Introduction

Welcome to the **White Box Testing Project**! This project utilizes `pytest` for testing and `pytest-cov` for measuring code coverage. The goal is to ensure the reliability and robustness of the `micarrito` module through comprehensive testing.

## 📋 Prerequisites

Before getting started, ensure you have the following installed on your system:

- **Python 3.6+**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (comes bundled with Python)
- **Git**: Version control system (optional, for cloning the repository)

## 🛠 Installation

### 1. **Clone the Repository**

If you haven't already cloned the repository, do so using Git:

```bash
git clone https://github.com/valefazio/WHITE-BOX-TESTING/tree/matteo-branch
cd white-box-testing
```



### 2. **Install Dependencies**

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```


## 🧪 Running Tests

Ensure you're in the project's root directory and your virtual environment is activated.

### **Basic Test Execution**

Run all tests using `pytest`:

```bash
pytest
```

### **Verbose Output**

For more detailed output, use the `-v` flag:

```bash
pytest -v
```


### **Generating Coverage Reports**


```bash
pytest
```

### **Explanation of Flags**

- `--cov=micarrito`: Measures coverage for the `micarrito` module.
- `--cov-report=term`: Displays a coverage summary in the terminal.
- `--cov-report=html:coverage_report`: Generates a detailed HTML coverage report in the `coverage_report/` directory.

### **Viewing the HTML Coverage Report**

After running the coverage command, open the HTML report in your default web browser:

- **On macOS:**

  ```bash
  open coverage_report/index.html
  ```

- **On Windows:**

  ```bash
  start coverage_report\index.html
  ```

- **On Linux:**

  ```bash
  xdg-open coverage_report/index.html
  ```

*Alternatively, navigate to the `coverage_report/` directory and open `index.html` manually.*



## 📚 Additional Resources

- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/en/latest/)
- [Coverage.py Documentation](https://coverage.readthedocs.io/en/coverage-5.5/)
- [GitHub Guides](https://guides.github.com/)

---

