# Enterprise UI Automation Framework – Books to Scrape

## Project Overview

An automated UI testing framework built with Playwright and Pytest to validate website functionality, book data consistency, navigation, hyperlinks, images, and pagination.

**Repository:** [Enterprise UI Automation Framework – Books to Scrape](https://github.com/Fail2/Enterprise-UI-Automation-Framework-Books-to-Scrape)

## Target Websites

### 1. Books to Scrape

URL: https://books.toscrape.com/index.html

Used for:
- Homepage validation
- Random book navigation
- Book data consistency
- Broken link validation
- Product image validation
- Pagination testing

### 2. Quotes to Scrape

URL: https://quotes.toscrape.com/

Used for:
- Homepage and login page validation
- Login functionality
- Logout link validation

## Features

- Homepage and heading validation
- Random navigation across five books
- Book title and price consistency checks
- Hyperlink response validation
- Product image attribute validation
- Pagination testing across up to five pages
- HTML and Allure reports
- Screenshots, videos, and traces on test failures
- Docker-based execution
- GitHub Actions CI/CD integration

## Tech Stack

- Python
- Playwright
- Pytest
- pytest-html
- Allure Report
- Docker
- GitHub Actions

## Installation Guide

### 1. Clone Repository

```bash
git clone https://github.com/Fail2/Enterprise-UI-Automation-Framework-Books-to-Scrape.git
cd Enterprise-UI-Automation-Framework-Books-to-Scrape
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browser

```bash
playwright install chromium
```

## Allure Installation

The `allure-pytest` plugin is installed through `requirements.txt`.

### 1. Install Java

If Java is not already installed, run:

```bash
sudo apt install default-jre
```

### 2. Install Allure CLI

**Prerequisites:** Node.js and npm must be installed. Then run:

```bash
npm install -g allure-commandline
```

### 3. Verify Installation

```bash
java -version
allure --version
```

**Note:** If the Allure CLI installation fails due to permission issues, configure npm's global directory or use `sudo npm install -g allure-commandline` if appropriate for your system.


## Environment Setup

- Configure target website URLs if required by the tests.
- Keep credentials and sensitive environment variables out of version control.
- Provide suitable test credentials if the login test requires authentication.
- Ensure the required dependencies and tools are installed in the environment where tests will run.

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_homepage.py
```

Replace the example filename with an existing test file from the `tests/` directory.

## Project Structure

```text
Enterprise-UI-Automation-Framework-Books-to-Scrape/
├── tests/
├── pytest.ini
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .github/
│   └── workflows/
│       └── playwright.yml
└── README.md
```

Report and artifact directories are generated during execution according to the project configuration.

## Test Case Coverage

### Test Case 1: Homepage Validation

- Verify the homepage URL and title.
- Validate visible headings and non-empty heading text.
- Confirm the books section is visible and contains at least one book.

### Test Case 2: Random Book Navigation

- Randomly select five books.
- Open each book's details page.
- Verify the details page title matches the selected book.
- Confirm book information is visible.
- Return to the homepage between selections.

### Test Case 3: Book Data Consistency

- Randomly select five books.
- Compare homepage titles and prices with their details pages.
- Verify that the displayed data matches.

### Test Case 4: Broken Link Validation

- Collect unique hyperlink URLs.
- Send requests to the URLs.
- Validate the response status codes.

### Test Case 5: Product Image Validation

- Verify images are visible.
- Validate non-empty `src` and `alt` attributes.
- Confirm the image class contains `thumbnail`.
- Validate images across up to five pages or until pagination ends.

### Test Case 6: Login and Logout Link Validation

- Open Quotes to Scrape.
- Navigate to the login page.
- Submit the login form with suitable credentials.
- Verify the authenticated page state.
- Verify the logout link is visible and enabled.

## Report Generation Guide

Run the tests:

```bash
pytest
```

The configured Pytest options generate the HTML report and Allure raw results. Screenshots, videos, and traces are retained on failure according to the configuration.

## HTML Report Guide

HTML report location:

```text
reports/test-report.html
```

Open the generated report in a browser after test execution.

## Allure Report Guide

Generate the Allure HTML report and open the report

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

- `allure-results/` contains raw test results.
- `allure-report/` contains the generated HTML report.

## Docker Execution

Build the image and run the tests:

```bash
docker compose up --build
```

Ensure the Playwright version in the Docker image matches the version installed through the project dependencies.

## GitHub Actions Setup

Workflow location:

```text
.github/workflows/playwright.yml
```

The workflow is configured to run on push, pull request, and manual execution events.

Pipeline responsibilities:

- Check out the repository.
- Install Python dependencies and Playwright browsers.
- Execute the tests.
- Generate Allure reports.
- Upload HTML reports and test artifacts.
- Deploy the Allure report to GitHub Pages when deployment is configured and successful.

## Design Decisions

- **Playwright:** Browser automation and page interaction.
- **Pytest:** Test execution and fixtures.
- **pytest.ini:** Centralized test discovery and reporting configuration.
- **Allure and pytest-html:** Test reporting.
- **Docker:** Consistent execution environment.
- **GitHub Actions:** Automated CI/CD and report publishing.

## Known Limitations

- Tests depend on target website availability and structure.
- Website changes may require test updates.
- Random book selection can vary between runs.
- External links may fail due to network or third-party server issues.
- Login tests depend on suitable test credentials if authentication is required.

## References

- [Books to Scrape](https://books.toscrape.com/index.html)
- [Quotes to Scrape](https://quotes.toscrape.com/)
- [Playwright Python Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [pytest-html Documentation](https://pytest-html.readthedocs.io/)
- [Allure Report Documentation](https://allurereport.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
