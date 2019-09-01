from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def run(user, pas):
    options = Options()  
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    user=user
    pas=pas

    driver = webdriver.Chrome(options=options)
    driver.get('https://tngportal.touchngo.com.my/tngPortal/login')
    # driver.save_screenshot('screen1.png')

    elem = driver.find_element_by_name('j_username')
    elem.send_keys(user)
    elem = driver.find_element_by_name('j_password')
    elem.send_keys(pas)
    elem.send_keys(Keys.RETURN)
    # driver.save_screenshot('screen2.png')

    titles = []
    cards = []

    try:
        table = driver.find_element_by_id('l_com_xerox_ts_domain_CardRegistration')
       
        theads = table.find_element_by_tag_name('thead').find_elements_by_tag_name('th')
        for th in theads:
            titles.append(th.text)

        tbodys = table.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        for tbody in tbodys:
            card = []
            for e in tbody.find_elements_by_tag_name('td'):
                card.append(e.text)
            
            cards.append(card)

    except NoSuchElementException:
        print("Wrong username or password ... ")

    driver.close()

    return titles, cards