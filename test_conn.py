import requests
from bs4 import BeautifulSoup
from datetime import date
import json
import os

url_industries = 'https://api.hh.ru/industries' 

url_professional_roles = 'https://api.hh.ru/professional_roles'

url_1 = 'https://hh.ru/oauth/authorize?response_type=code&client_id=42390166'

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
		AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 \
			YaBrowser/23.5.2.625 Yowser/2.5 Safari/537.36"


def get_data_from_site(user_agent, url) ->BeautifulSoup:
	headers = {"user-agent": user_agent}
	r = requests.get(url=url, headers=headers)
	soup = BeautifulSoup(r.text, "lxml")
	return soup


req_2 = get_data_from_site(user_agent, url_professional_roles)

req_2 = req_2.find('p').string.strip()

json_s = json.loads(req_2)

id_roles = 0


for item in json_s['categories']:
	if item['name'] == 'Информационные технологии':
		for role in item['roles']:
			if role['name'] == 'Программист, разработчик':
				id_roles = role['id']


url_vacancy_raw = 'https://api.hh.ru/vacancies'


def create_request(url: str, params: dict) ->str:
	list_params = []
	for key, value in params.items():
		list_params.append(key + '=' + value)
	new_url = url + '?' + '&'.join(list_params)
	return new_url


params = {
	'date_from' : str(date.today()),
	'professional_role': id_roles,
	'text': 'sql+AND+python'
}

url_vacancy = create_request(url_vacancy_raw, params)

print(url_vacancy)

req_vacancy = get_data_from_site(user_agent, url_vacancy)

arr_vacancy = json.loads(req_vacancy.find('p').get_text())['items']




