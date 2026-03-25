# Engeto_Projekt3 - Automated tests (Playwright)

## Description
This project contains automated end-to-end tests for the website https://vivaplus.tv/en-eur using the Playwright framework in Python.

The goal is to verify basic user flows and core functionality of the site.


## Technologies used
- Python
- Playwright
- Pytest


## Installation and launch
1. Clone the repository:
git clone <link-to-repository>
cd <project-name>

2. Install required packages:
pip install pytest playwright

3. Install Playwright browsers:
playwright install

4. Run the tests:
pytest



## Tests
The project includes the following test scenarios:
- Verify that the homepage loads correctly
- Verify navigation to the login page
- Verify that a product can be successfully added to the cart


## Notes
- Cookies handling is implemented as a helper function, as it represents test setup rather than a feature under test.
- The site uses a responsive design, so some elements (e.g. login button) are displayed differently depending on the viewport.
- Role-based locators (`get_by_role`) are used where possible for better stability and readability.