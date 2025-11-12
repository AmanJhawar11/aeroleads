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

2. Get Your LinkedIn Cookie: This script requires you to be authenticated.

Log in to LinkedIn in your browser (e.g., Chrome).
Open Developer Tools (F12).
Go to the Network tab.
In search box type graphl.
Click on any request to linkedin.com (you may need to refresh the page).
In the "Request Headers" section, find the cookie: field.
Copy the entire value of the cookie.
paste this cookie in scraper.py (where its return PASTE_YOUR_LINKEDIN_COOKIES_HERE)
