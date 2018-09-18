from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import sqlite3


conn = sqlite3.connect('everytime.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Articles
    (id INTEGER PRIMARY KEY ,subject TEXT UNIQUE,article TEXT,like_count INTEGER,
    scrap_count INTEGER,comment_count INTEGER,write_time DATE )''')

# Using Chrome Webdriver

driver = webdriver.Chrome('/home/user/dev/chromedriver')

# Login into Everytime

driver.get('https://everytime.kr/login')

driver.find_element_by_name('userid').send_keys('your ID')
driver.find_element_by_name('password').send_keys('your password')

driver.find_element_by_class_name('submit').click()

base_url = 'https://everytime.kr/374614/p/'
url = base_url + str(1)
print(url)


# go to kookmin university pages

base_url = 'https://everytime.kr/374614/p/'

for i in range(31, 100):
    all_page = base_url + str(i)
    driver.get(all_page)

    sleep(0.5)

    page_html = driver.page_source
    soup = BeautifulSoup(page_html, 'html.parser')
    articles = soup.select('#container > div.articles > article > a.article')

    if len(articles) < 1:
        print('error')

    for a in articles:
        single_link = 'https://everytime.kr' + str(a['href'].strip())

        driver.get(single_link)

        sleep(1)

        single_page_html = driver.page_source
        soup = BeautifulSoup(single_page_html, 'html.parser')
        articles = soup.select('#container > div.articles > article > a.article > p.large')
        subjects = soup.select('#container > div.wrap.articles > article > a > h2')
        votes = soup.select('#container > div.wrap.articles > article > a > ul > li.vote')
        comments = soup.select('#container > div.articles > article ul.status li.comment')
        scraps = soup.select('#container > div.articles > article ul.status li.scrap')
        times = soup.select('#container > div.articles > article time.large')

        if len(articles) < 1:
            print('single error')
        else:
            subject = subjects[0].text.strip()
            article = articles[0].text.strip()
            vote = votes[0].text.strip()
            comment = comments[0].text.strip()
            scrap = scraps[0].text.strip()
            created_time = times[0]['title']
            if created_time < '2018-09-01 00:00:00':
                break

            print('subect :', subject)
            print('article :',article)
            print('vote :', vote)
            print('comment :',comment)
            print('scrap :',scrap)
            print('time :',created_time)

            cur.execute('''INSERT OR IGNORE INTO Articles (subject,article,like_count,scrap_count,comment_count,write_time)
            VALUES (?,?,?,?,?,?)''', (subject,article,vote,scrap,comment,created_time ))

            conn.commit()
conn.commit()
