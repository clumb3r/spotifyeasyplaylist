from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from colorama import Fore

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
URL = 'https://open.spotify.com/'
user_agent = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
              'AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/39.0.2171.95 Safari/537.36')
options.add_argument(f'user-agent={user_agent}')

def header():
    print(Fore.MAGENTA + """   ________  ___  __   _____  ____   ______________
  / __/_  / / _ \/ /  / _ \ \/ / /  /  _/ __/_  __/
 / _/  / /_/ ___/ /__/ __ |\  / /___/ /_\ \  / /   
/___/ /___/_/  /____/_/ |_|/_/____/___/___/ /_/    
                                                 """)
    print(Fore.GREEN + "Easy playlist generator created by clumber! Generate playlists seamlessly and quickly using spotify's built in queue system.\nPlease read https://github.com/SubwooferLullaby/spotifyeasyplaylist for full"
                         " documentation! If there are any issues create a pull request or contact me on discord at clumber#7126. ")


header()


def auth():
    driver.get(URL)
    time.sleep(1)
    driver.find_element(By.XPATH, """/html/body/div[3]/div/div[2]/div[1]/header/div[5]/button[2]/div""").click()
    print(Fore.CYAN + "Choose the auth type you would like:")
    print(Fore.RED + "1: Email/Username and Password")
    print(Fore.RED + "2: Facebook")
    print(Fore.RED + "3: Apple")
    print(Fore.RED + "4: Google")
    inp = int(input("Enter a number: "))
    if inp == 1:
        email = input(Fore.RED + "Email/Username: ")
        password = input(Fore.RED + "Password: ")
        driver.find_element(By.ID, 'login-username').send_keys(email)
        time.sleep(1)
        driver.find_element(By.ID, 'login-password').send_keys(password)
        time.sleep(1)
        driver.find_element(By.XPATH,"""/html/body/div[1]/div/div[2]/div/div/div[2]/div[3]/div[2]/button/div[1]""").click()  #update login button
        time.sleep(1)
        time.sleep(3.5)
        driver.find_element(By.XPATH, """//*[@id="onetrust-close-btn-container"]/button""").click()  # remove cookie
    if inp == 2:
        print(Fore.RED + "Auth type not finished.")
    if inp == 3:
        print(Fore.RED + "Auth type not finished.")
    if inp == 4:
        print(Fore.RED + "Auth type not finished.")


auth()


def createplaylist():
    driver.find_element(By.XPATH, """//*[@id="main"]/div/div[2]/nav/div[1]/div[2]/div/div[1]/button""").click()
    time.sleep(2)
    driver.find_element(By.XPATH, """//*[@data-testid="more-button"]""").click()
    time.sleep(.3)
    driver.find_element(By.CSS_SELECTOR, """#context-menu > ul > li:nth-child(4) > button""").click()
    time.sleep(.3)
    driver.find_element(By.XPATH, """//*[@data-testid="playlist-edit-details-name-input"]""").clear()
    time.sleep(.3)
    driver.find_element(By.XPATH, """//*[@data-testid="playlist-edit-details-name-input"]""").send_keys("Queue Playlist!") #c
    time.sleep(.3)
    driver.find_element(By.XPATH, """//*[@data-testid="playlist-edit-details-description-input"]""").send_keys("Automatically move your songs from the queue to a playlist! Made with <3 by clumber. https://github.com/SubwooferLullaby/spotifyeasyplaylist")
    time.sleep(.3)
    driver.find_element(By.XPATH, """//*[@data-testid="playlist-edit-details-save-button"]""").click() #save checkpoint
    time.sleep(2)

def movesongs():
    print(Fore.BLUE + "Started moving songs!")
    driver.find_element(By.XPATH, """//*[@data-testid="control-button-queue"]""").click()
    while True:
        try:
            driver.find_element(By.XPATH, """//*[@data-testid="more-button"]""").click()
            driver.find_element(By.XPATH, """//*[@id="context-menu"]/ul/li[7]/button""").click()
            driver.find_element(By.XPATH, """/html/body/div[16]/div/ul/li[7]/div/ul/div/li[2]/button""").click()
            driver.find_element(By.XPATH, """//*[@data-testid="control-button-skip-forward"]""").click()
            time.sleep(1.7)
        except Exception as e:
            pass


func = input(Fore.CYAN + "Do you already have a queue playlist? y/n?\n")
if func == 'y':
    movesongs()
if func == 'n':
    createplaylist()
    movesongs()

