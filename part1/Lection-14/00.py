# сначала нужно установить библиотеку requests
# для этого в консоли наберите и запустите:
# pip install requests
import requests  

link = 'https://pcoding.ru/csv/11.txt'
# s = requests.get(link).text

# txt = requests.get(link)
# txt.encoding = 'utf-8'
# s = txt.text

s = requests.get(link).content.decode('utf-8')

print(s)
