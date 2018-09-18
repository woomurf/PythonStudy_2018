from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

# Using Chrome Webdriver

driver = webdriver.Chrome('/home/user/dev/chromedriver')
driver.implicitly_wait(1)

# Login into Everytime

driver.get('https://everytime.kr/login')

driver.find_element_by_name('userid').send_keys('dngusdnd')
driver.find_element_by_name('password').send_keys('glglt523')

driver.find_element_by_class_name('submit').click()

base_url = 'https://everytime.kr/374614/p/'
url = base_url + str(1)
print(url)

# go to kookmin university pages

base_url = 'https://everytime.kr/374614/p/'
count = 0
url = 'http://everytime.kr'
list1 = []
for i in range(1, 2):
    single_page = base_url + str(i)
    driver.get(single_page)                              # open chrome single_page

    sleep(1)

    page_html = driver.page_source                       # get source single_page
    soup = BeautifulSoup(page_html, 'html.parser')       # parsing single_page
    notices = soup.select('#container > div.wrap.articles > article > a')
#    print(notices)
#container > div.wrap.articles > article:nth-child(2) > a > ul > li.vote
    if len(notices) < 1:
        print('error')
    else:
        for n in notices:

            href = n.get('href')
            vote = n.select('ul > li.vote').text()

            if len(list1) < 1:
                list1.append(href)
                list1.append(vote)
            else:
                old_vote = int(list1[1])
                if old_vote < int(vote):
                    list1[0] = href
                    list1[1] = vote

            count += 1
#print('href: {}, vote: {}'.format(href,vote))
print('count : ',count)
