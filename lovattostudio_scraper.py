from asyncio import wait
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import json
# from fake_useragent import UserAgent
import re
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
    
ua_arr = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/571.37 (KHTML, like Gecko) Chrome/104.0.2153 Safari/537.36',
      'Mozilla/5.0 (Linux; Android 10; AKA-L29; HMSCore 6.12.2.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.2.311 Mobile Safari/537.36',
      'Mozilla/5.0 (Linux; arm; Android 13; 22101316UG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.83 YaBrowser/23.9.5.83.00 SA/3 Mobile Safari/537.36',
      'Mozilla/5.0 (Linux; Android 14; M2012K11C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69',
      'Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0 (Edition Yx GX 03)',
      'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.98',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 SberBrowser/9.2.63.1',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
      'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55',
      'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0',
      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.1',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.4',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3',
      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.3',
      'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
      'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0']
options =webdriver.ChromeOptions()




# options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(f"useragent={ua_arr[random.randint(0, len(ua_arr) - 1)]}")

driver = webdriver.Chrome(options=options)

result = []
old_card_list = []
new_card_list = []
new_card_item_list = []
break_out_flag = False
flag = True

try:
    driver.maximize_window()
    driver.get("https://www.lovattostudio.com/en/shop/")
    driver.implicitly_wait(5)

    while flag == True:
        card_list = driver.find_element(By.CSS_SELECTOR,"ul.products").find_elements(By.CSS_SELECTOR,"li")
        for card in card_list:
            card_name = card.find_element(By.CSS_SELECTOR,"h3 > a").text      
            card_price_web_el = card.find_element(By.CSS_SELECTOR,"span.price")  
            # обработка цен бандлов со скидкой 
            card_price = ''
            if len(card_price_web_el.text)>7: 
                card_price = re.findall(r'(?<=Current price is: )\$[0-9][0-9]\.[0-9][0-9]', card_price_web_el.text) 
                try: 
                    card_price = card_price[0]    
                except:
                    card_price = card_price_web_el.text     
            else:
                card_price= card_price_web_el.text   
            card.location_once_scrolled_into_view
            driver.implicitly_wait(5)
            card_img = card.find_element(By.CSS_SELECTOR,"div.product-loop-inner > figure > a > div.kleo-woo-image.kleo-woo-front-image > img").get_attribute("src")  
            card_link = card.find_element(By.CSS_SELECTOR,"div > figure > a").get_attribute("href")  

            print(card_name)
            print(card_price)
            print(card_img)
            print(card_link)

            result.append(
                {
                'card_name': card_name,
                'card_price': card_price,
                'card_img': card_img,
                'card_link': card_link
                }
            )
            

        try:
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/section[2]/div/div/div[1]/div/nav/ul/li[3]/a")
            driver.execute_script("arguments[0].click()",element)
        except:
            flag = False

    # with open(r"card.json", 'w', encoding='utf-8') as file:
    #     json.dump(result, file, ensure_ascii=False, indent=2)

    # сравнение новой информации с имеющиеся 
    # записать названия бандлов в словари, новую информацию берет из результатов парсинга, старую с json

    with open(r'card.json', encoding="utf-8") as file:
        data  = json.load(file)      
        for item in data:          
            old_card_list.append(item)
        number_of_old_item = len(old_card_list)
    for item in result:        
        new_card_list.append(item)                
    number_of_new_item = len(new_card_list)

    # если появились новые бандлы, обновить информацию в json + записать информацию в json для новых бандлов
    if (number_of_old_item == number_of_new_item):
        print('новых карт нет')  
    else:
        print('вышли новые карты!') 

        # запись новых карт в отдельный json

        for new_item in new_card_list:
            if new_item not in old_card_list:   
                print('найдена новая карта!')
                print(new_item['card_name'])       

                new_card_item_list.append(new_item)
                with open(r"card_info_new.json", 'w', encoding='utf-8') as file:
                    json.dump(new_card_item_list, file, ensure_ascii=False, indent=2)
                break_out_flag = True

            
            
        # обновить данные в главном json 
        with open(r"card.json", 'w', encoding='utf-8') as file:
            json.dump(result, file, ensure_ascii=False, indent=2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
        

    