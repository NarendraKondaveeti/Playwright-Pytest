# Python + Playwright + Pytest Framework Notes

## Goal

Automation Framework ni scratch nundi create cheyyadam.

Target Website:

https://the-internet.herokuapp.com/

Scenario:

1. Launch website
2. Open Basic Auth page
3. Authenticate using username/password
4. Validate "Congratulations!" message

---

# Project Structure Created

```text
Playwright-Pytest/
│
├── tests/
│   ├── ui/
│   └── api/
│
├── pages/
├── locators/
├── fixtures/
├── utils/
├── config/
├── test_data/
├── reports/
├── screenshots/
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env
└── README.md
```

---

# requirements.txt

Purpose:

Install project dependencies.

```txt
playwright
pytest
pytest-playwright
allure-pytest
python-dotenv
pytest-html
requests
faker
```

Command:

```bash
pip install -r requirements.txt
playwright install
```

---

# .env

Purpose:

Store environment data.

```env
BASE_URL=https://the-internet.herokuapp.com

USERNAME=admin
PASSWORD=admin

HEADLESS=False
BROWSER=chromium
TIMEOUT=30000
```

---

# pytest.ini

Purpose:

Pytest configuration.

```ini
[pytest]

addopts=-v

testpaths=tests

python_files=test_*.py
```

---

# config/settings.py

Purpose:

Read values from .env.

```python
Settings.BASE_URL
Settings.USERNAME
Settings.PASSWORD
Settings.BROWSER
```

Used across framework.

---

# fixtures/browser_fixture.py

Purpose:

Launch browser.

```python
@pytest.fixture
def page():
```

Provides Playwright page object.

Added:

```python
slow_mo=1000
```

For slow execution.

---

# conftest.py

Purpose:

Load fixtures globally.

```python
from fixtures.browser_fixture import *
```

No need to import fixture in every test.

---

# pages/base_page.py

Purpose:

Common reusable methods.

Methods:

```python
open()
click()
fill()
get_text()
```

Every page class inherits this.

---

# locators/login_locators.py

Purpose:

Store locators.

```python
BASIC_AUTH_LINK

SUCCESS_MESSAGE
```

No hardcoded locators in tests.

---

# pages/login_page.py

Purpose:

Page Object Model.

Methods:

```python
click_basic_auth()

get_success_message()
```

Business actions stored here.

---

# test_data/basic_auth_data.py

Purpose:

Store test data.

```python
USERNAME="admin"

PASSWORD="admin"
```

---

# tests/ui/test_login.py

Purpose:

Execute test scenario.

Test:

```python
def test_basic_auth():
```

Flow:

1. Open Basic Auth URL
2. Authenticate
3. Read success message
4. Validate text

Assertion:

```python
assert "Congratulations!" in actual_text
```

---

# Authentication Learning

Original Thought:

```text
Click Link
↓
Popup Appears
↓
Enter Username
↓
Enter Password
↓
Sign In
```

Reality:

Browser Authentication Popup is NOT HTML.

It is a Browser Security Dialog.

Playwright cannot use normal locators on it.

---

# Real Industry Approach

Instead of handling popup:

```python
https://username:password@website.com
```

Example:

```python
https://admin:admin@the-internet.herokuapp.com/basic_auth
```

Browser authenticates automatically.

Popup never appears.

---

# Why Popup Did Not Appear

Because test used:

```python
page.goto(
"https://admin:admin@the-internet.herokuapp.com/basic_auth"
)
```

Flow:

```text
Browser Open
↓
Credentials passed in URL
↓
Authentication Success
↓
Popup Skipped
↓
Page Opened
↓
Validation Done
```

Hence popup not visible.

---

# Current Status

Completed:

✅ Framework Structure

✅ Playwright Installation

✅ Pytest Configuration

✅ Environment Configuration

✅ Browser Fixture

✅ Base Page

✅ Locator File

✅ Page Object

✅ Test Data File

✅ Basic Auth Test

✅ Validation

Test Result:

```text
PASSED
```

Framework is working successfully.
