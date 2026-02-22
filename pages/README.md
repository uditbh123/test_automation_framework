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
