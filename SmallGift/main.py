from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from playsound import playsound
from threading import Thread

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path='venv/chromedriver.exe', options=options)
driver.get('https://lyricvn.com/loi-bai-hat-ke-theo-duoi-anh-sang-huy-vac/')

try:
    elements = [0, 0]
    first_key = b'v\xe1\xbb\x9di'.decode()
    second_key = b'\xc4\x91\xc6\xb0\xe1\xbb\xa3c l\xc3\xa0'.decode()
    third_key = b'm\xc3\xacnh em'.decode()
    last_key = b'G\xe1\xbb\xadi t\xe1\xba\xb7ng c\xe1\xba\xadu, Crush c\xe1\xbb\xa7a m\xc3\xacnh <3'.decode()

    WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'h1.entry-title')))

    elements[0] = driver.find_element(By.CSS_SELECTOR, 'h1.entry-title')
    elements[1] = driver.find_element(By.CSS_SELECTOR, 'div.entry-content p:last-of-type')

    lyrics = elements[0].text[12:] + '\n\n' + elements[1].text[:elements[1].text.find(first_key) + 4]
    lyrics = lyrics[: lyrics.find(second_key) + 7] + '\t' + lyrics[lyrics.find(second_key) + 7:]
    lyrics = lyrics[: lyrics.find(third_key) + 7] + '\t' + lyrics[lyrics.find(third_key) + 7:]
    lyrics += '\n' + last_key

    if lyrics != '':
        thread = Thread(target=playsound, args=('y2mate.mp3',), daemon=True)
        thread.start()
        sleep(14)

    for text in lyrics:
        print(text, end='')
        if text == '\t':
            sleep(4.5)
        else:
            sleep(0.1)

    thread.join()
except Exception:
    pass
driver.quit()
