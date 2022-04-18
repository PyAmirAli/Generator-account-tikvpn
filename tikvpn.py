from telegram_mail import *
import requests,time
from selenium.webdriver import Chrome
hed = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'accept': 'application/json',
    'content-type': 'application/json; charset=utf-8',
    'referer': 'https://www.tikvpn.com/sign/signup'
    }
email = mail()
print(email)
data = '{"email":"'+email+'","password":"password@123"}'
login = requests.post('https://www.tikvpn.com/web/account/signup',headers=hed,data=data)
print(login.text)
time.sleep(5)
driver = Chrome(executable_path='chromedriver.exe')
driver.get(code())
print(f'''login info
username:{email}
passord:password@123
''')
