import urllib
import urllib.request


def request(url):
  try:
    urllib.request.urlopen(url)
  except Exception as erro:
    print(f'Falha ao requisitar o endereço \n{url}')
    print('Tipo de erro:', erro)
  else:
    print(f'Request aceita')
    print(f'{url}')


while True:
  url = str(input('URL: '))
  print()
  request(url)
  print()
