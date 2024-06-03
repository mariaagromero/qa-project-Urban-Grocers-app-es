##### Maria Romero - Proyecto 7 - Cohort 10
#### Automatización de pruebas de la aplicación web

### Descripcion
Este proyecto contiene un conjunto de funciones y pruebas automatizadas para verificar la creación de kits de usuarios en la pagina web de Urban Grocers. Utiliza requests para interactuar con la API y assert para validar los resultados esperados.

El objetivo de este proyecto es automatizar la verificación de la creación de kits con diferentes nombres y parámetros, asegurando que el sistema maneje correctamente una variedad de casos. Los nombres de los kits pueden incluir caracteres especiales, espacios y números, y también se prueban casos límite como la longitud máxima y mínima de los nombres permitidos.

### Archivos y Estructura

##### sender_stand_request.py
Contiene funciones para interactuar con los endpoints API para la creación de usuarios y kits.

- post_new_user(body): Envía una solicitud POST para crear un nuevo usuario.
- post_new_client_kit(kit_body, auth_token): Envía una solicitud POST para crear un nuevo kit con el token de autorización proporcionado.
- get_kits_table(): Recupera el número actual de kits.
##### data.py
Contiene los datos utilizados en las pruebas, incluidos los cuerpos de los usuarios y varios parámetros para probar diferentes escenarios.
##### create_kit_name_kit_test.py
Contiene las funciones de prueba y aserciones.

- get_kit_body(kit_name): Genera el cuerpo del kit con el nombre especificado.
- positive_assert(kit_name): Prueba la creación de un kit con un nombre válido.
- negative_assert(kit_name): Prueba la creación de un kit con un nombre inválido.
- negative_assert_no_name(kit_body): Prueba la creación de un kit sin proporcionar un nombre.

####Casos de Prueba
#####Pruebas Positivas

- test_create_kit_1_letter_get_success_response(): Prueba la creación de un kit con un nombre de una sola letra.
- test_create_kit_511_letter_get_success_response(): Prueba la creación de un kit con un nombre de 511 letras.
- test_create_kit_special_symbol_get_success_response(): Prueba la creación de un kit con caracteres especiales.
- test_create_kit_space_get_success_response(): Prueba la creación de un kit con espacios.
- test_create_kit_string_number_get_success_response(): Prueba la creación de un kit con números.
##### Pruebas Negativas

- test_create_kit_0_letter_name_get_error_response(): Prueba la creación de un kit con un nombre vacío.
- test_create_kit_512_letter_get_bad_request_response(): Prueba la creación de un kit con un nombre de 512 letras.
- test_create_kit_no_name_get_bad_request_response(): Prueba la creación de un kit sin parámetro de nombre.
- test_create_kit_number_name_get_bad_request_response(): Prueba la creación de un kit con un nombre numérico.

### Ejecución de las Pruebas
Para ejecutar las pruebas, utiliza el siguiente comando en la terminal:
###### pytest create_kit_name_kit_test.py

#### Configuración
##### configuration.py
Contiene la configuración para las URLs y rutas del servicio APIDOC.
