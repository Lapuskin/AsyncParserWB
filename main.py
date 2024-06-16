import requests

menu_url = 'https://static-basket-01.wbbasket.ru/vol0/data/main-menu-by-ru-v2.json'
filters_url = 'https://catalog.wb.ru/catalog/bl_shirts/v4/filters?appType=1&' + 'QUERY_IN_JSON' + '&curr=rub&dest=-59202&spp=30'

response = requests.get(menu_url)
print(response.text)

