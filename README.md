# 🧪 Test Automation Framework
### Playwright · PyTest · Python · CI/CD

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-1.58-green?style=flat&logo=playwright)
![PyTest](https://img.shields.io/badge/PyTest-9.0-orange?style=flat&logo=pytest)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-black?style=flat&logo=githubactions)
![Tests](https://img.shields.io/badge/Tests-10_Passing-brightgreen?style=flat)

---

## 📌 What Is This Project?

This is a **production-style UI test automation framework** built from scratch using Python, Playwright, and PyTest.

The goal is not just to write test scripts — it's to build the kind of **scalable, maintainable testing infrastructure** used by real QA teams at software companies. Every design decision (folder structure, fixtures, page objects, CI pipeline) mirrors real-world industry practices.

> **Target application:** [SauceDemo](https://www.saucedemo.com/) — a practice e-commerce app designed for QA automation training.

---

## 🚀 Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.11** | Core programming language |
| **Playwright** | Browser automation (Chromium) |
| **PyTest** | Test runner and assertion framework |
| **pytest-html** | HTML test report generation |
| **GitHub Actions** | CI/CD — runs tests automatically on every push |

---

## 🏗️ Framework Architecture

This framework is built around the **Page Object Model (POM)** design pattern — separating *what to test* from *how to interact with the UI*.

```
test_automation_framework/
│
├── .github/
│   └── workflows/
│       └── tests.yml             → CI/CD pipeline (GitHub Actions)
│
├── pages/                        → UI interaction logic (HOW to test)
│   ├── __init__.py
│   ├── login_page.py             → LoginPage class with locators & methods
│   └── inventory_page.py         → InventoryPage class with locators & methods
│
├── tests/                        → Test cases (WHAT to test)
│   ├── __init__.py
│   ├── test_login.py             → 4 parametrized login scenarios
│   ├── login_test_data.py        → Login test data (credentials & expected results)
│   └── test_inventory.py         → 6 inventory page scenarios
│
├── utils/                        → Reusable helper functions
│   ├── __init__.py
│   └── screenshot.py             → Auto screenshot capture on failure
│
├── reports/                      → Generated after test run (gitignored)
│   ├── report.html               → Full HTML test report
│   └── screenshots/              → Failure screenshots
│
├── conftest.py                   → PyTest fixtures, logging, failure hooks
├── pytest.ini                    → PyTest configuration
├── requirements.txt              → Project dependencies
└── README.md
```

---

## 🧠 How It Works — The Full Flow

```
pytest -v
  │
  ├── pytest.ini           → sets testpaths, auto-generates HTML report
  ├── conftest.py          → opens fresh Chromium browser per test
  │     ├── saucedemo_page    → browser at saucedemo.com (used by login tests)
  │     └── logged_in_page    → browser already logged in (used by inventory tests)
  │
  ├── test_login.py        → 4 parametrized login scenarios
  │     └── login_page.py  → fills form, clicks login, verifies result
  │
  ├── test_inventory.py    → 6 inventory scenarios
  │     └── inventory_page.py → sorts, counts products, adds to cart
  │
  └── on failure → screenshot captured automatically → saved to reports/
```

**Key design decisions:**
- `scope="function"` on fixtures — every test gets a **fresh browser** with clean state, preventing test pollution
- **Fixture composition** — `logged_in_page` builds on top of `saucedemo_page`, so login logic is never repeated in test files
- `wait_for_url()` after login — waits for actual page navigation before asserting, preventing flaky tests
- `pytest_runtest_makereport` hook — automatically captures screenshots on failure without any extra code in test files

---

## ✅ Implemented Test Scenarios

### 🔐 Login Tests — `test_login.py` (4 tests)

All 4 scenarios driven by a single parametrized test function:

| # | Scenario | Credentials | Expected Outcome |
|---|---|---|---|
| 1 | Valid login | `standard_user` / `secret_sauce` | Redirected to inventory page |
| 2 | Invalid credentials | `invalid_user` / `wrong_password` | Error: "Username and password do not match" |
| 3 | Empty fields | ` ` / ` ` | Error: "Username is required" |
| 4 | Locked out user | `locked_out_user` / `secret_sauce` | Error: "Sorry, this user has been locked out" |

---

### 🛒 Inventory Tests — `test_inventory.py` (6 tests)

All tests start already logged in via the `logged_in_page` fixture:

| # | Scenario | What It Verifies |
|---|---|---|
| 1 | Page loads correctly | URL contains `/inventory.html` and title is "Products" |
| 2 | Six products displayed | Exactly 6 product cards are visible |
| 3 | Products are complete | Every card has a name, price and Add to Cart button |
| 4 | Sort by name A→Z | Product names appear in alphabetical order |
| 5 | Sort by price low→high | Prices appear in ascending order |
| 6 | Add to cart updates badge | Cart badge changes from 0 to 1 after adding a product |

---

## 📊 Test Reports & Screenshots

Every test run automatically generates:

- **`reports/report.html`** — full HTML report with test names, pass/fail status, logs and duration
- **`reports/screenshots/`** — screenshot of the browser at the exact moment a test fails

The HTML report is also uploaded as a **downloadable artifact** on every GitHub Actions run.

---

## ⚙️ Setup & Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/uditbh123/test_automation_framework.git
cd test_automation_framework
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright browser
```bash
python -m playwright install chromium
```

### 5. Run tests
```bash
pytest -v
```

The HTML report is automatically generated at `reports/report.html`.

---

## 🔁 CI/CD Pipeline

This project uses **GitHub Actions** to run the full test suite automatically on every push to `main` and on every pull request.

**What the pipeline does:**
1. Spins up a fresh Ubuntu machine
2. Installs Python 3.11 and all dependencies
3. Installs Chromium browser
4. Runs all 10 tests in headless mode (`CI=true`)
5. Uploads the HTML report as a downloadable artifact
6. Posts a test summary directly on the Actions page

> Tests run headless in CI automatically — the `conftest.py` checks for the `CI` environment variable and switches mode accordingly.

---

## 🗺️ Roadmap

| Phase | Feature | Status |
|---|---|---|
| 1 | Login tests — 4 scenarios | ✅ Complete |
| 2 | Inventory page tests — 6 scenarios | ✅ Complete |
| 3 | Cart functionality tests | 🔜 Next |
| 4 | Checkout flow tests | 🔜 Planned |
| 5 | End-to-end user journey test | 🔜 Planned |
| — | Cross-browser testing (Firefox, WebKit) | 🔜 Planned |
| — | Docker support | 🔜 Planned |
| — | API testing layer | 🔜 Planned |

---

## 📁 Key Files Explained

**`conftest.py`** — The backbone of the framework. Contains two fixtures: `saucedemo_page` (opens a fresh browser) and `logged_in_page` (builds on top of it, logs in automatically). Also handles session logging and the failure screenshot hook.

**`pages/login_page.py`** — Page Object for the login page. All locators and interactions live here. Tests never touch Playwright directly.

**`pages/inventory_page.py`** — Page Object for the inventory page. Handles product counting, sorting, price extraction and cart interactions. Converts price strings like `"$9.99"` to floats for reliable numeric comparison.

**`tests/login_test_data.py`** — Pure data file. No test logic, just the list of login scenarios. Keeping data separate from logic makes adding new scenarios trivial.

**`pytest.ini`** — Central configuration. Defines test discovery path, default CLI options, and live logging. Ensures `pytest` works correctly for everyone who clones the repo.

**`.github/workflows/tests.yml`** — The CI pipeline. Defines every step the GitHub Actions robot follows to install, run and report tests on every push.

---

## 👨‍💻 Author

**Udit** — building real-world QA automation skills through hands-on projects.