# Web-scraping-
using Selenium 

This project automates the process of saving PDF lecture notes from a password-protected educational platform to an Excel spreadsheet. Since my access to these notes depended on temporary login credentials, I created this solution to maintain permanent access without storing the files locally and using unnecessary disk space.

Initially, I attempted to use BeautifulSoup for scraping, but quickly encountered limitations with the platform's authentication system. This led me to switch to Selenium, which could properly handle the login process and interact with the dynamic elements of the site. After authentication, the script navigates to the course page containing all class units and their subunits, where each subunit link leads directly to a PDF file.

The program extracts three key pieces of information for each entry: the unit title, subunit title, and PDF link. These are organized into a pandas DataFrame for clean structuring before being exported to Excel. The script is designed to skip any empty units or subunits, processing all available content until reaching the end of the page. Detailed comments throughout the code make each step clear and understandable.
