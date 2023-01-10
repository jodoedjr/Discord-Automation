from user import User
from time import sleep
from os.path import exists
from random import randrange

with open('account.txt') as f:
    email = f.readline().strip()
    password = f.readline().strip()
    target = f.readline().strip()
    targetUserName = f.readline().strip()

if exists('messages.txt') :
    print ('messages.txt exists')
    index = randrange(0,9,1)
    print(f"random index: {index}")
    with open('messages.txt.') as f:
        content = f.readlines()
        message = content[index]
        print(f"{content[index]}")
else:
    print ('messages.txt does not exist')
    message = "AUTOMATED MESSAGE: I'm playing Elden Ring LOL :zany_face:"

user = User(email, password, 'https://discord.com/login', target, targetUserName)

user.login()
sleep(5)
user.choose()
sleep(5)
#user.send_message("THIS IS A TEST OF AN AUTOMATED MESSAGING SYSTEM. DO NOT BE ALARMED.")
user.send_message(message)
#sleep(10)
user.quit()
quit()
# Instead of using user.choose(), you can put a longer sleep time and choose server and channel manually
# Note that the msg_xpath in user.send_message() may need to be changed if error occurs