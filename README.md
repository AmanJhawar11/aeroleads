# LinkedIn Company Employee Scraper

This Python script scrapes LinkedIn for a list of employees from a specific company page. It extracts the person's name, profile URL, designation, and location, then saves the results to a CSV file named `leads.csv`.

This project is for educational purposes only.

## ⚠️ Important Warning
This script is **not** an official API. Scraping LinkedIn is against their Terms of Service, and running this script could lead to your account being restricted or banned. **Use at your own risk.**

## Features
* Fetches the internal Company ID from a public LinkedIn company URL.
* Paginates through employee search results.
* Saves extracted data (Profile Link, Name, Designation, Location) to `leads.csv`.

## ⚙️ How to Use

**1. Install Dependencies:**
   You must have Python 3 installed.
   ```bash
   pip install -r requirements.txt
