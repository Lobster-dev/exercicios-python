from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(
                    executable_path='/home/robert/rpa-bentinho/geckodriver'
                    )

ListaAnimeUrl = []
ListaAnimeTxt = []
ListaAnime = []

with open("anime_op.txt", "r") as file:
    for anime in file:
        anime = f"{anime.strip()} OP 1"
        searchinput = anime

        driver.get('https://www.youtube.com/')
        sleep(2)

        inputYoutube = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//input[@id="search"]')))

        inputYoutube.send_keys(searchinput)

        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="search-icon-legacy"]'))).click()

        #class="style-scope ytd-video-renderer"
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="video-title"]'))).click()

        ListaAnimeUrl.append(driver.current_url)
        ListaAnimeTxt.append(anime)
        sleep(2)
        
driver.quit()

for Anime, url in zip(ListaAnimeTxt,ListaAnimeUrl):
    Lista = open("anime-rpa.txt","a")
    Lista.write(Anime+"\n")
    Lista.write(url+"\n")