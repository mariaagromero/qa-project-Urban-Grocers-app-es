import configuration
import requests
import data


# Creacion de Cuenta
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=user_body ,
                        headers=data.headers)

response = post_new_user(data.user_body)

#Funcion para el authToken
def auth_token():
    user = post_new_user(data.user_body)
    user_json = user.json()

    if "authToken" in user_json:
        return user_json["authToken"]
    else:
        return None

    # Creacion del kit
def post_new_client_kit(kit_body_key):
    token = auth_token()
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {token}"

    kit_body = kit_body_key

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH ,
                         json=kit_body ,
                         headers=headers)