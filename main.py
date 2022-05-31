from user import User
from time import sleep

with open('account.txt') as f:
    email = f.readline().strip()
    password = f.readline().strip()
    target = f.readline().strip()
    targetUserName = f.readline().strip()

user = User(email, password, 'https://discord.com/login', target, targetUserName)

user.login()
sleep(5)
user.choose()
sleep(5)
#user.send_message("THIS IS A TEST OF AN AUTOMATED MESSAGING SYSTEM. DO NOT BE ALARMED.")
user.send_message("AUTOMATED MESSAGE: I'm playing Elden Ring LOL :zany_face:")
#sleep(10)
#user.quit()
quit()
# Instead of using user.choose(), you can put a longer sleep time and choose server and channel manually
# Note that the msg_xpath in user.send_message() may need to be changed if error occurs