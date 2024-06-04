import sender_stand_request
import data


def get_kit_body(kit_name):
    current_name = data.kit_body.copy()
    current_name["name"] = kit_name
    return current_name


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


def negative_assert(kit_name: object) -> object:
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    token = new_user_response.json().get('authToken')
    kit_name_test = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_name_test, token)

    assert new_user_response.status_code == 201
    assert kit_response.status_code == 400
    assert new_user_response.json()["authToken"] != ""
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "El nombre de kit que ingresaste es incorrecto."


def negative_assert_no_name(kit_body: object) -> object:
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    token = new_user_response.json().get('authToken')
    kit_response = sender_stand_request.post_new_client_kit(token, kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


# Pruebas
# Prueba 1: El numero permitido de caracteres (1)
def test_create_kit_1_letter_get_success_response():
    positive_assert(data.one_letter)


# Prueba 2: El numero permitido de caracteres (511)
def test_create_kit_511_letter_get_success_response():
    positive_assert(data.five_hundred_eleven_letter)


# Prueba 3: El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_name_get_error_response():
    negative_assert(data.empty_letter)


# Prueba 4: El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letter_get_bad_request_response():
    negative_assert(data.five_hundred_twelve_letter)


# Prueba 5: Se permiten caracteres especiales
def test_create_kit_special_symbol_get_success_response():
    positive_assert(data.special_symbol)


# Prueba 6: Se permiten espacios
def test_create_kit_space_get_success_response():
    positive_assert(data.space)


# Prueba 7: Se permiten números
def test_create_kit_string_number_get_success_response():
    positive_assert(data.string_number)


# Prueba 8: El parámetro no se pasa en la solicitud
def test_create_kit_no_name_get_bad_request_response():
    negative_assert(data.no_name)


# Prueba 9: Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_number_name_get_bad_request_response():
    negative_assert(data.type_number)
