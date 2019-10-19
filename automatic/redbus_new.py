import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#driver = webdriver.Chrome(executable_path='/home/rohit/web_crawling/chromedriver')
fn = open("city.csv","r")

for line in fn:
    fields = line.split(",")

    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=options,executable_path=r"/home/prince/programs/web_crawling/chromedriver")


    driver.get('https://www.redbus.in')

    time.sleep(2)
    driver.maximize_window()
    source=driver.find_element_by_xpath('//*[@id="src"]')

    source.click()
    source.clear()


    source.send_keys(fields[0])
    time.sleep(1)
    source.send_keys('\n')

    time.sleep(2)

    destination=driver.find_element_by_xpath('//*[@id="dest"]')

    destination.click()
    destination.clear()
    destination.send_keys(fields[1])
    time.sleep(1)
    destination.send_keys('\n')


    time.sleep(2)


    select_month= driver.find_element_by_xpath('//div[@class="rb-calendar"]/table[@class="rb-monthTable first last"]/tbody/tr[@class="rb-monthHeader"]/td[@class="monthTitle"]')

    select_date=driver.find_element_by_xpath('//div[@class="rb-calendar"]/table[@class="rb-monthTable first last"]/tbody/tr/td[@class = "current day"]')
    month_year = fields[2]

    while(select_month.text != month_year):
        driver.find_element_by_xpath('//*[@id="rb-calendar_onward_cal"]/table/tbody/tr[1]/td[3]/button').click()
        select_month= driver.find_element_by_xpath('//div[@class="rb-calendar"]/table[@class="rb-monthTable first last"]/tbody/tr[@class="rb-monthHeader"]/td[@class="monthTitle"]')



    date = str(fields[3].strip('\n'))
    i = 3
    j = 1
    while(i <= 8):
            while(j <= 7):
                select_date=driver.find_element_by_xpath('//*[@id="rb-calendar_onward_cal"]/table/tbody/tr[%d]/td[%d]'%(i,j))
                if(select_date.text==date):
                    break
                j=j+1
            if(select_date.text==date):
                break
            i=i+1
            j=1

    select_date.click()
    time.sleep(3)
    driver.find_element_by_id('search_btn').click()

    time.sleep(5)
    element=driver.find_elements_by_id('onward_view')

    #for ele in element:
    #	fp.write(ele.get_attribute('innerHTML'))
    #print(y.getText())
    html=driver.page_source
    driver.quit()
    soup=bs(html,"lxml")
    ext=soup.find_all('div',class_='clearfix bus-item-details')
    fp=open("/home/prince/automatic/" + fields[0] + "_" + fields[1] + "_" + fields[3].strip('\n') + "_" + ''.join(fields[2].split()) + ".csv","w")
    fp.write("Bus_Name,Service_Name,Departure_Time,Arrival_Time,Duration,Fare\n");
    for x in ext:
    	y=x.find('div',class_='travels lh-24 f-bold d-color')
    	fp.write(str(y.getText())+",")

    	y=x.find('div',class_='bus-type f-12 m-top-16 l-color')
    	fp.write(str(y.getText())+",")

    	y=x.find('div',class_='dp-time f-19 d-color f-bold')
    	fp.write(str(y.getText())+",")

    	y=x.find('div',class_='bp-time f-19 d-color disp-Inline')
    	fp.write(str(y.getText())+",")

    	y=x.find('div',class_='dur l-color lh-24')
    	fp.write(str(y.getText())+",")

    	y=x.find('div',class_='fare d-block')
    	fp.write(str(y.getText().split(" ")[1])+",\n")

    	#fp.write(str(x))

    	#print("beautiful soup:-",y.getText())
    #fp.write(str(ext[0]))
    fp.close()
