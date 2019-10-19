import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
#options.add_argument('headless')
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome(chrome_options=options,executable_path=r"/home/rohit/web_crawling/chromedriver")



driver.get('https://www.ixigo.com/')

time.sleep(2)
driver.maximize_window()
source=driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[6]/div/div/div[1]/div/div[1]/input')
source.click()
source.clear()
source.send_keys('Kolkata')
time.sleep(1)
source.send_keys('\n')
destination=driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[6]/div/div/div[3]/div/div[1]/input')
destination.click()
destination.clear()
destination.send_keys('Mumbai')
time.sleep(1)
destination.send_keys('\n')

month_year='August 2019'
select_month=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div')

while(select_month.text!=month_year):
	button=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/button')
	button.click()
	select_month=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div')

date='16'
i=1
flag=0
while i<7:
	j=1
	while j<7:
		select_date=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/table/tbody/tr[%d]/td[%d]/div[1]'%(i,j))
		if select_date.text==date:
			flag=1
			break
		j=j+1
	if flag==1:
		break
	i=i+1
time.sleep(2)
select_date.click()

search_btn=driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[6]/div/div/div[6]/button/div')
search_btn.click()


time.sleep(5)


html=driver.page_source
soup=bs(html,"lxml")
ext=soup.find_all('div',class_='c-flight-listing-row')
fp=open("ixigo.csv","w")
fp.write("Flight_Name  ,Departure_Time  ,Arrival_Time  ,Duration  ,Fare\n");
for x in ext:
	y=x.find('div','u-uppercase u-text-ellipsis')
	fp.write(str(y.getText())+",")

	y=x.find('div','left-wing')
	z=y.find('div','time')
	fp.write(str(z.getText())+",")

	y=x.find('div','right-wing')
	z=y.find('div','time')
	fp.write(str(z.getText())+",")

	y=x.find('div','c-timeline-wrapper horizontal')
	fp.write(str(y.getText())+",")


	y=x.find('div','price-group')
	z=y.find('div','price')
	p=z.find('div','c-price-display u-text-ellipsis ')
	fp.write(str(p.getText())+"\n")
	#fp.write(str(x))

	#print("beautiful soup:-",y.getText())
#fp.write(str(ext[0]))
fp.close()

driver.quit()
