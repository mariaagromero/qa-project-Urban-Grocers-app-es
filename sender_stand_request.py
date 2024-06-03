import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=body,
                        headers=data.headers)

def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers['Authorization'] = f'Bearer {auth_token}'
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)
def get_kits_table():
    response = requests.get(configuration.URL_SERVICE + configuration.KITS_TABLE_PATH)
    table_data = response.content.decode('utf-8').split('\n')
    kits_number = len([row for row in table_data if row.strip()]) - 1
    return kits_number
