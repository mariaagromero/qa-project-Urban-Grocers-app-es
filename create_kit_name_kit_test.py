import sender_stand_request
import data


def get_kit_body(kit_name):
    current_name = data.kit_body.copy()
    current_name["name"] = kit_name
    return current_name

# Funcion de Prueba positiva
def positive_assert(kit_name):
    initial_kit_table = sender_stand_request.get_kits_table()
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    token = new_user_response.json().get('authToken')
    kit_name_test = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_name_test, token)

    assert new_user_response.status_code == 201
    assert kit_response.status_code == 201
    assert new_user_response.json()["authToken"] != ""

    update_kit_table = sender_stand_request.get_kits_table()
    assert update_kit_table == initial_kit_table + 1


def negative_assert(kit_name):
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    token = new_user_response.json().get('authToken')
    kit_name_test = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_name_test, token)

    assert new_user_response.status_code == 201
    assert kit_response.status_code == 400
    assert new_user_response.json()["authToken"] != ""
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "El nombre del kit es invalido."


def negative_assert_no_name(kit_body):
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    token = new_user_response.json().get('authToken')
    kit_response = sender_stand_request.post_new_client_kit(token, kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


# Pruebas
# Prueba 1: El numero permitido de caracteres (1)
def test_create_kit_name_1():
    kit_body = data.kit_body["one_character"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    positive_assert(kit_response , 201 , kit_body)

# Prueba 2: El numero permitido de caracteres (511)
def test_create_kit_name_2():
    kit_body = data.kit_body["maximum_characters"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    positive_assert(kit_response , 201 , kit_body["name"])


# Prueba 3: El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_name_3():
    kit_body = data.kit_body["empty_field"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    negative_assert(kit_response , 400)


# Prueba 4: El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_name_4():
    data.kit_body = data.kit_body["number_of_characters_is_higher"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    negative_assert(kit_response , 400)


# Prueba 5: Se permiten caracteres especiales
def test_create_kit_name_5():
    kit_body = data.kit_body["special_characters"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    positive_assert(kit_response , 201 , kit_body["name"])


# Prueba 6: Se permiten espacios
def test_create_kit_name_6():
    kit_body = data.kit_body["spaces"]
    kit_response = sender_stand_request.post_new_cliente_kit(data.kit_body)
    positive_assert(kit_response , 201 , kit_body["name"])


# Prueba 7: Se permiten números
def test_create_kit_name_7():
    kit_body = data.kit_body["numbers"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    positive_assert(kit_response , 201 , kit_body["name"])


# Prueba 8: El parámetro no se pasa en la solicitud
def test_create_kit_name_8():
    data.kit_body = data.kit_body["the_is_no_parameter"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    negative_assert(kit_response , 400)


# Prueba 9: Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_name_9():
    data.kit_body = data.kit_body["different_parameter_(number)"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    negative_assert(kit_response , 400)