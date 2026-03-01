# Test Automation Framework using Playwright and PyTest

## 📌 Project Overview

This project is a basic test automation framework built using Python, Playwright, and PyTest.

The goal of this project is to simulate real-world software testing automation practices used in companies by building a scalable and maintainable testing structure instead of writing simple automation scripts.

This framework follows the **Page Object Model (POM)** design pattern to separate test logic from UI interaction logic, improving readability, reusability, and maintainability.

---

## 🚀 Technologies Used

- Python
- Playwright
- PyTest
- PyTest HTML Reporting

---

## 🧱 Framework Architecture

The framework is divided into multiple layers for better scalability:
```
test_automation_framework
│
├── tests → Contains test cases (what to test)
├── pages → Contains UI interaction logic (how to test)
├── utils → Contains reusable helper functions
├── reports → Stores test reports and screenshots
├── requirements.txt → Project dependencies
└── README.md
```


---

## 📂 Folder Description

### tests/

Contains test cases which verify application behaviour.

Example:
- Valid login functionality test

---

### pages/

Implements the Page Object Model.

This layer contains UI element locators and interaction methods.

Example:
- Login page interaction logic

---

### utils/

Contains reusable helper functions.

Example:
- Screenshot capture on test failure

---

### reports/

Stores:
- HTML test execution reports
- Failure screenshots

---

## 🧪 Implemented Test Scenario

- Valid user login test using SauceDemo test application
- Assertion based validation for successful login
- Automatic screenshot capture on test failure
- HTML report generation after test execution

---

## 📌 25/02/2026

- Modified `tests/test_login.py` to include proper logging and improved test flow
- Updated `conftest.py` with a **PyTest fixture** for browser setup and teardown
- Integrated **Playwright** for browser automation (Chromium)
- Added **logging** to track test execution steps
- Verified that the login test runs successfully and logs execution info
- Reinforced project structure following **Page Object Model (POM)**
- Prepared virtual environment and installed all dependencies
- Ensured GitHub is clean by ignoring unnecessary folders (`venv/`, `logs/`, `.pytest_cache/`)

## 📌 01/03/2026 – Framework Update

### Refactored `pages/login_page.py` for robust login handling:
- Added safer navigation handling after login
- Improved verification logic (`is_login_successful`)
- Trimmed and cleaned error message retrieval

### Updated `tests/test_login.py` to use parametrized tests with structured test data:
- Added `tests/test_data_login.py` to manage multiple login scenarios:
  - Valid login
  - Invalid login
  - Empty credentials
  - Locked out user
- Replaced multiple individual test functions with a single `@pytest.mark.parametrize` test

### Fixed browser fixture in `conftest.py`:
- Created `saucedemo_page` fixture for launching Chromium
- Ensures clean browser setup and teardown for each test

### Verified framework stability:
- Ran 4 tests successfully (valid login, invalid login, empty credentials, locked out user)
- Added proper logging for test execution steps

### Reinforced Page Object Model (POM) structure and clean code practices:
- Clear separation of test logic (`tests/`) and UI interaction logic (`pages/`)
- Reusable fixtures and helper methods

## ⚙️ Setup Instructions

### 1. Clone Repository
```
git clone https://github.com/uditbh123/test_automation_framework.git

cd test_automation_framework
```

---

### 2. Create Virtual Environment

```
python -m venv venv
```


Activate it:

Windows:
```
venv\Scripts\activate
```


---

### 3. Install Dependencies
```
pip install -r requirements.txt
```


---

### 4. Install Playwright Browsers
```
python -m playwright install
```


---

## ▶️ Running Tests
```
pytest
```
---

## 📊 Generate HTML Test Report
```
pytest --html=reports/report.html
```

Open:
```
reports/report.html
```


to view the test execution report.

---

## 🎯 Future Improvements

- Logging system integration
- Cross-browser test execution
- CI/CD pipeline integration
- Docker support
- API testing layer

---

## 👨‍💻 Author

Udit
