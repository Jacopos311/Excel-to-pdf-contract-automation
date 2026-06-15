# Excel to PDF Contract Automation

A simple, efficient Python tool that reads client data from an Excel sheet and automatically generates customized, formatted PDF contracts in seconds. 

## Why I Built This
While researching administrative bottlenecks on Reddit, I noticed that one of the biggest time-sinks for freelancers and small business owners is paperwork—specifically, wasting hours doing manual copy-paste to fill out standard client contracts in Word. This script aims to eliminate that overhead entirely.

## Features
* **External Templates:** The contract text is completely separated from the Python code. You can now change the entire contract by simply editing `contract_template.txt` without touching the script!
* **Automated Parsing:** Reads client name, service, and pricing data directly from Excel using `pandas`.
* **Instant PDF Generation:** Creates formatted PDF contracts ready to sign in seconds using `reportlab`.
* **Safe Testing:** Includes a secondary script to instantly generate 50 mock client records for secure testing.

## How to Run the Test

1. **Clone the repository** or download the python files to your machine.
2. **Install the required libraries** via your terminal:
   ```bash
   pip install pandas reportlab openpyxl
