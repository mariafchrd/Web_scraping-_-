from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Setup Chrome WebDriver
options = Options()
options.add_argument("user-agent=Mozilla/5.0")
driver = webdriver.Chrome(options=options)

# Step 1: Login to the site
driver.get("https://elearning.athensfashionclub.com/login/index.php")
driver.find_element(By.ID, 'username').send_keys('ssd_fot')
driver.find_element(By.ID, 'password').send_keys('Kala111!')
driver.find_element(By.ID, 'loginbtn').click()

# Wait for login to finish
time.sleep(5)

# Step 2: Go to the course page
driver.get("https://elearning.athensfashionclub.com/course/view.php?id=116")
time.sleep(5)

# Step 3: Scrape the data
data = []  # To store class title, activity name, and URL

sections = driver.find_elements(By.CSS_SELECTOR, "div.courseindex-section")

for section in sections:
    try:
        # Get section (class) title
        title_element = section.find_element(By.CSS_SELECTOR, ".courseindex-section-title .courseindex-link")
        title = title_element.text.strip()

        # Find activities within the section
        activity_links = section.find_elements(By.CSS_SELECTOR, "ul.courseindex-sectioncontent a.courseindex-link")
        for link in activity_links:
            activity_name = link.text.strip()
            url = link.get_attribute("href")
            data.append({
                "Class Title": title,
                "Activity Name": activity_name,
                "URL": url
            })

    except Exception as e:
        # Skip sections that don't follow the expected structure
        continue

# Close browser
driver.quit()

# Step 4: Save to Excel
df = pd.DataFrame(data)
df.to_excel("trial.xlsx", index=False)
print("✅ Saved to 'activities_by_class.xlsx'")
