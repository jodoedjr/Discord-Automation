from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from os import getcwd

class User:
    """Your discord account"""
    def __init__(self, email, password, url, target, targetUserName):
        # Your username and password
        self.email = email
        self.password = password

        # Url of the website you want to automatically access
        self.url = url

        # target url of your friend's chat (https://discord.com/channels/@me/540321061699452929), and their username (@whatever)
        self.target = target
        if targetUserName[:1] == '@':
            self.targetUserName = targetUserName
        else:
            self.targetUserName = '@' + targetUserName

        # Driver of the browser you use
        # use included chromedriver.exe, or configure or hardcode path to your own below
        #self.driver = webdriver.Chrome("C:/Users/jodoe/projects/Discord-Automation/chromedriver.exe")
        self.driver = webdriver.Chrome(getcwd() + "\chromedriver.exe")

        # Access to the website you want using the driver you want
        self.browse = self.driver.get(self.url)

    def login(self):
        """Login to discord"""
        self.driver.find_element_by_name('email').send_keys(self.email)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_name('password').send_keys(Keys.ENTER)

    def choose(self):
        """Choose where to send messages"""
        #self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[2]/div[2]').click()
        self.driver.get(self.target) #format -> "https://discord.com/channels/@me/999999999999999999"
        #self.driver.find_element_by_xpath('//*[@id="channels"]/div/div[4]').click()
        #self.driver.find_element_by_css_selector("[aria-label=\"Message @littleravens\"]").click()

    def send_message(self, msg):
        """Send messages to text channel"""
        #msg_xpath = '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div/div'
        #self.driver.find_element_by_xpath(msg_xpath).send_keys(msg)
        #self.driver.find_element_by_xpath(msg_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_css_selector("[aria-label=\"Message " + self.targetUserName + "\"]").send_keys(msg)
        self.driver.find_element_by_css_selector("[aria-label=\"Message " + self.targetUserName + "\"]").send_keys(Keys.ENTER)
        self.log(msg)

    def log(self, msg):
        """Msg log"""
        t = datetime.now().strftime('%H:%M:%S')
        print(f'[{t}] MESSAGE: {msg}')

    def quit(self):
        try: 
            self.driver.quit()
        except:
            print("ERROR QUITING WEBDRIVER")
