<h1>Welcome to Soo Min's Github space!</h1>

<h3>This is for OSS project using raspberry pi.</h3>

<h4>1. Name of the project:</h4> Twitter bot for Korean baseball League
<h4>2. Role:</h4> The bot helps tweeting the updated ranking of Korean baseball teams. The updates occur every hour.
(Constraint: raspberry pi should be connected to wifi)
<h4>3. Usefulness:</h4> Anyone around the world can get an easy access to the ranking of Korean baseball teams through Twitter. Twitter is a world-wide platform. Therefore, Korean baseball League can be widely known by making the information easily reachable to foreigners as well as Koreans.
Also, this regularly updates the ranking so that people does not have to manually check the ranking on their own.
<h4>4. Getting started:</h4> 

1. Prepare a Raspberry pi and wifi network.
2. Implement an operating system of your preference in the Raspberry pi.
3. Create a twitter application and twitter account.
(Make sure to get your own access token, access token secret, API key, and API secret key)
4. Download proper packages, modules, environments for accessing Twitter using the Raspberry pi.
5. Write a code using any language. 
(Python is used in my project - You can reference to my code)
The "tweet.py" is a practice code, and the "baseball.py" is an actual code for my project. Twython is used to interface with Twitter. If you want to scrape information from a certain website, you can implement web scraping techniques.
6. If you want your code to be executed regularly, you can make a setting using CRON (In the terminal, type "crontab -e") 
7. Run!
You can visit my twitter page to see the result => https://twitter.com/RaspberrybotSo1
<h4>5. What is used in the project:</h4>

1. Shell script
2. git
3. vim
4. Python programming language(version 3)
5. twython - module for interfacing with Twitter
6. Web scraping - using urllib and BeautifulSoup
7. CRON - task scheduler
8. Timestamp
(etc)
<h4>6. Explanation Video:</h4> If you want a summarized information and demostration, check out this video => https://youtu.be/p3DI5NfQqb4
<h4>7. Reference source & my additional contribition:</h4> 

- https://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/ <- This website includes a step-by-step instruction about how to connect raspberry pi and twitter application. 
- In addition to this, I additionally implemented **web scraping** and **CRON** techniques. 
- By extracting certain information from a website, I was able to print out the same type of information without having to search it repeatedly. 
- Also, CRON task scheduler enabled the python program to be executed periodically by itself. 
- **Timestamp** was also used to provide the updated information at different times.
<h4>If you have any question, please contact me.(21700524@handong.edu)</h4>
