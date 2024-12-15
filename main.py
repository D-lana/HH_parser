from ProfessionalRoles import ProfessionalRoles
from utils import print_dict, create_request, agg_params, get_json_from_site, send_count_vacancy, get_vacancy
from config import url_vacancy_raw
from datetime import date, timedelta

if __name__ == "__main__":
    professional_roles = ProfessionalRoles(11, 96)
    # category = professional_roles.get_all_professional_categories()
    # print_dict(category)
    # 11. Информационные технологии
    # professional_roles.set_category_id(11)

    # roles = professional_roles.get_all_roles_in_category()
    # print_dict(roles)
    # 96. Программист, разработчик
    # professional_roles.set_role_id(96)

    search_parameters = 'sql+AND+python'
    date_start = date.today() - timedelta(days=3)
    params = agg_params(professional_roles.role_id, search_parameters, date_start)
    
    
    req = create_request(url_vacancy_raw, params)
    json_req = get_json_from_site(req, 'p')
    
 
    vacancies = get_vacancy(json_req)
    send_count_vacancy(len(vacancies))
    # for i in vacancies:
    #     i['url']
    # print(vacancies)


    # print(json_req['items'][0]['name'])
    


    """
{'id': '112749730', 'premium': False, 'name': 'Backend разработчик (Python DRF)',
 'department': None, 'has_test': False, 'response_letter_required': False, 
 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 
 'salary': None, 
 'type': {'id': 'open', 'name': 'Открытая'}, 
 'address': {'city': 'Москва', 'street': 'Профсоюзная улица', 
 'building': '76', 'lat': 55.66076, 
 'lng': 37.54356, 'description': None, 
 'raw': 'Москва, Профсоюзная улица, 76', 
 'metro': {'station_name': 'Калужская', 
 'line_name': 'Калужско-Рижская', 
 'station_id': '6.41', 'line_id': '6', 
 'lat': 55.656682, 'lng': 37.540075}, 
 'metro_stations': [{'station_name': 'Калужская', 'line_name': 'Калужско-Рижская', 'station_id': '6.41', 'line_id': '6', 'lat': 55.656682, 'lng': 37.540075}], 'id': '654983'}, 
 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-12-15T10:48:49+0300', 
 'created_at': '2024-12-15T10:48:49+0300', 
 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=112749730', 
 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/112749730?host=hh.ru', 
 'alternate_url': 'https://hh.ru/vacancy/112749730', 'relations': [], 'employer': {'id': '1579449', 'name': 'idaproject', 'url': 'https://api.hh.ru/employers/1579449', 
 'alternate_url': 'https://hh.ru/employer/1579449', 'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/6861154.png', 
 'original': 'https://img.hhcdn.ru/employer-logo-original/1310224.png', '240': 'https://img.hhcdn.ru/employer-logo/6861155.png'}, 
 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1579449', 'accredited_it_employer': True, 'trusted': True}, 
 'snippet': {'requirement': 'Уверенное знание python3. Знание сетевых протоколов HTTP, WebSocket. Продвинутое знание Django (Django REST Framework). 
 Знание SQL, опыт работы с...', 'responsibility': 'Разрабатывать и внедрять решения в новые или существующие продукты наших клиентов. 
 Будем вместе проводить нагрузочное тестирование и по его итогам...'}, 'contacts': None, 
 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 
 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 
 'accept_temporary': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 
 'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'}, 
 'employment': {'id': 'full', 'name': 'Полная занятость'}, 
 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}

    """