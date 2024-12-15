import requests
from bs4 import BeautifulSoup
import json
from config import user_agent
from datetime import date
from time import sleep

def agg_params(role, text, date_from=str(date.today())) -> dict:
	params = {
		'date_from' : date_from,
		'professional_role': role,
		'text': text
		}
	return params


def get_json_from_site(url, tag) -> json:
	headers = {"user-agent": user_agent}
	req = requests.get(url=url, headers=headers)
	soup = BeautifulSoup(req.text, "lxml")
	json_data = json.loads(soup.find(tag).get_text())
	# json_data = json.loads(soup.get_text())
	return json_data

def get_json_from_site_1(url, tag) -> json:
	headers = {"user-agent": user_agent}
	req = requests.get(url=url, headers=headers)
	soup = BeautifulSoup(req.text, "lxml")
	json_data = soup.find(tag).get_text() #json.loads(soup.find(tag).get_text())
	# json_data = json.loads(soup.get_text())
	return json_data


def create_request(url: str, params: dict) ->str:
	list_params = []
	for key, value in params.items():
		list_params.append(str(key) + '=' + str(value))
	new_url = url + '?' + '&'.join(list_params)
	return new_url


def print_dict(d: dict):
	for k, v in sorted(d.items()):
		print(f'{k}. {v}')
		

def send_count_vacancy(count) -> str:
	message = ''
	if count % 10 == 1:
		message = 'Найдена ' + str(count) + ' вакансия.\n'
	elif count % 10 in [2,3,4]:
		message = 'Найдено ' + str(count) + ' вакансий.\n'
	else:
		message = 'Найдено ' + str(count) + ' вакансии.\n'
	print(message)
	return message

# i['schedule']['name'] == 'Удаленная работа' \
def get_vacancy(arr_vacancy) -> int:
	actual_vacancy = []
	for i in arr_vacancy['items']:
		if i['name'].lower().find('senior') == -1 \
		and i['name'].lower().find('scientist') == -1 \
		and i['experience']['id'] != 'between3And6' \
		and i['name'].lower().find('backend') == -1:
			sleep(1)
			key_skills = get_json_from_site_1(i['url'], 'body')
			print(key_skills)
			actual_vacancy.append({
				'name' : i['name'],
				'company' : str('"' + i['employer']['name'] + '"'),
				'experience' : i['experience']['name'],
				'schedule' : i['schedule']['name'],
				'created_at' : i['created_at'],
				'url' : i['alternate_url']
				})
		# if i['alternate_url'].lower().find('108832024') != -1:
			# json_data = get_json_from_site(i['url'], 'body')
			# print(json_data['key_skills'])

			# json_data = json.loads(soup)
			# print(soup.prettify())
			# with open('answer.txt', 'w') as text:
			# 	print(soup.prettify())
			# 	text.write(req.text)
				# print(soup.find('noindex').find('template'))
			# print(i['name'], str('"' + i['employer']['name'] + '"'), i['experience']['name'], i['schedule']['name'], i['created_at'])
			# print(i['alternate_url'], '\n')
	return actual_vacancy

"""
{'id': '108832024',
 'premium': False, 
 'name': 'Программист Python', 
 'department': None, 
 'has_test': False, 
 'response_letter_required': False,
  'area': {'id': '2760', 'name': 'Бишкек', 'url': 'https://api.hh.ru/areas/2760'}, 
  'salary': None, 
  'type': {'id': 'open', 'name': 'Открытая'}, 
  'address': {'city': 'Бишкек', 'street': 'улица Насирдина Исанова', 'building': '105/3', 'lat': 42.87772, 'lng': 74.592247, 'description': None, 'raw': 'Бишкек, улица Насирдина Исанова, 105/3',
   'metro': None, 'metro_stations': [], 'id': '15349100'},
	'response_url': None, 
	'sort_point_distance': None, 
	'published_at': '2024-12-14T10:14:12+0300', 
	'created_at': '2024-12-14T10:14:12+0300', 
	'archived': False, 
	'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=108832024', 
	'show_logo_in_search': None, 
	'insider_interview': None, 
	'url': 'https://api.hh.ru/vacancies/108832024?host=hh.ru', 
	'alternate_url': 'https://hh.ru/vacancy/108832024', 
	'relations': [], 
	'employer': {'id': '4398836', 'name': 'ОсОО ОСМП', 'url': 'https://api.hh.ru/employers/4398836', 'alternate_url': 'https://hh.ru/employer/4398836', 
	'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/6617558.png', '90': 'https://img.hhcdn.ru/employer-logo/6617557.png', 
	'original': 'https://img.hhcdn.ru/employer-logo-original/1249282.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4398836', 
	'accredited_it_employer': False, 'trusted': True}, 
	'snippet': {'requirement': 'Отличное знание Python и его основных библиотек. Опыт работы с базами данных (SQL, NoSQL). Опыт работы на Django(или Flask). ', 
	'responsibility': 'Разработка и поддержка программного обеспечения на Python. Участие в проектировании и архитектуре программных решений. Тестирование и отладка кода. '}, 
	'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 
	'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 
	'accept_temporary': False, 
	'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 
	'accept_incomplete_resumes': False, 
	'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'}, 
'employment': {'id': 'full', 'name': 'Полная занятость'}, 
'adv_response_url': None, 
'is_adv_vacancy': False, 
'adv_context': None}
"""
