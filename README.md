
# White Box Testing Project

## 📝 Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Writing Tests](#writing-tests)

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

### Viewing the HTML Coverage Report
After running the coverage command, open the HTML report in your default web browser:

On macOS:


```bash
open coverage_report/index.html
```

On Windows:


```bash
start coverage_report\index.html
```

On Linux:


```bash
xdg-open coverage_report/index.html
```




## Writing Tests

Here's a step-by-step guide to adding a new test:

### **a. Create a New Test File**

- Create a new file in the `tests/` directory.
- Ensure the file name start with `test_*`.
- Example:
  ```bash
  touch tests/test_new_feature.py
  ```

### **b. Import Necessary Modules**

- Import the module or function you want to test.
- Adjust the import paths as necessary.
- Example:
  ```python
  import project.some_module
  ```

### **c. Write Test Functions**

- Define test functions starting with `test_`.
- Use assertions to verify expected outcomes.
- Example:
  ```python
  def test_new_feature_behavior():
      result = project.some_module.new_feature()
      assert result == expected_value
  ```





## 📚 Additional Resources

- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/en/latest/)
- [Coverage.py Documentation](https://coverage.readthedocs.io/en/coverage-5.5/)
- [GitHub Guides](https://guides.github.com/)

---





