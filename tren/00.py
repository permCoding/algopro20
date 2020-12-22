# сначала нужно установить библиотеку requests
# для этого в консоли наберите и запустите:
# pip install requests
import requests

link = 'https://pcoding.ru/csv/11.txt'

# ver.1
# s = requests.get(link).text

# ver.2
# txt = requests.get(link)
# txt.encoding = 'utf-8'
# s = txt.text

# ver.3
s = requests.get(link).content.decode('utf-8')

print(s)