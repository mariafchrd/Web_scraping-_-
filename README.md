# Web-scraping-
using Selenium 

I wanted to save the links of some pdf's (containing my classes notes) to an excel sheet so i can have acces to them even if my username and password stopped being active .I didn't want to use up space in my computer and i found this to be the most efficient method.  

I started this project using Beautifulsoup, but i soon realized that because of the authentication that was needed to access the page, my program wouldn't return any objects. And i couldn't find a way to do it with Beautifulsoup. So that's why i used Selenium.

The goal of this project was to get past the authentication wall and get to the page that contained the notes. That page had all of the class titles and under each one of them, all of the subunits. The text of the subunit is also a link and if you click that you get access to the pdf. 
I also used dataframes so i can save it to an excel .

So the information that is scrapped is the title of the unit , the title of the subunit and lastly the link of the pdf (for all units and subunits). If one subunit or unit is empty then it moves on until it reaches the end of the page.

(The code containes a lot of comments so i think is readable.)
