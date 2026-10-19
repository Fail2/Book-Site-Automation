# Book Site Automation

## Project Overview
Automated testing of a book website using Playwright and Pytest.

## Features
- Homepage validation
- Random book navigation
- Book data consistency
- Hyperlink and image validation
- Pagination testing
- HTML and Allure reports
- Docker support
- GitHub Actions CI/CD

## Tech Stack
- Python
- Playwright
- Pytest
- pytest-html
- Allure
- Docker
- GitHub Actions

## Installation Guide
```bash
git clone https://github.com/Fail2/Book-Site-Automation
cd Book-Site-Automation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```
## Allure Installation

`allure-pytest` is installed automatically from `requirements.txt`.

Install Java and Allure CLI globally on Ubuntu/Linux Mint:

```bash
sudo apt install default-jre
sudo npm install -g allure-commandline
```

Verify installation:

```bash
allure --version
```

**Prerequisites:** Node.js and npm must be installed.

## Environment Setup
Configure the target website URL if required. Keep environment variables and credentials out of version control.

## Running Tests
```bash
pytest
```

## Project Structure
```text
Book-Site-Automation/
├── tests/
│   ├── test_homepage.py
│   ├── test_book_navigation.py
│   ├── test_book_data_consistency.py
│   ├── test_broken_links.py
│   ├── test_product_images.py
│   └── test_login.py
├── reports/
├── allure-results/
├── allure-report/
├── playwright-artifacts/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .gitignore
├── .github/
│   └── workflows/
│       └── playwright.yml
└── README.md
```

## Test Case Coverage
- Homepage
- Five random book navigation tests
- Five random book data consistency tests
- Hyperlinks
- Images
- Pagination

## Report Generation Guide
Run `pytest` to generate the configured HTML report and Allure raw results.

## HTML Report Guide
Report location: `reports/test-report.html`

## Allure Report Guide
Generate the Allure HTML report:

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## Docker Execution
```bash
docker compose up --build
```

## GitHub Actions Setup
The workflow runs automatically on push and pull request events. Test reports and artifacts are uploaded, and the Allure report is deployed to GitHub Pages when configured successfully.

## Design Decisions
- Playwright for browser automation.
- Pytest for test execution and fixtures.
- `pytest.ini` for centralized configuration.
- Docker for consistent execution.
- GitHub Actions for automated CI/CD.

## Known Limitations
- Tests depend on website availability.
- Website changes may require test updates.
