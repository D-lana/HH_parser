from utils import get_json_from_site

class ProfessionalRoles():
    def __init__(self, category_id, role_id):
        tag = 'p'
        url = 'https://api.hh.ru/professional_roles'
        self.json_req = get_json_from_site(url, tag)
        self.category_id = category_id
        self.role_id = role_id


    def get_all_professional_categories(self) -> dict:
        dict_category = {}
        for item in self.json_req['categories']:
            dict_category.update({int(item['id']) : item['name']})
        return dict_category


    def get_all_roles_in_category(self) -> dict:
        dict_roles = {}
        category_id = str(self.category_id)
        for item in self.json_req['categories']:
            if item['id'] == category_id: # 'Информационные технологии':
                for role in item['roles']:
                    dict_roles.update({int(role['id']) : role['name']})
        return dict_roles
    

    def set_category_id(self, category_id: int):
        self.category_id = category_id


    def set_role_id(self, role_id: int):
        self.role_id = role_id

