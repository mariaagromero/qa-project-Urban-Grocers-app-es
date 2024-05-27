### Maria Romero - Proyecto 7 - Cohort 10
### Automatización de pruebas de la aplicación web


# Descripcion

Este proyecto contiene un conjunto de funciones y pruebas automatizadas para verificar la creación de kits de usuarios en la pagina web de Urban Grocers. Utiliza requests para interactuar con la API y assert para validar los resultados esperados.

El objetivo de este proyecto es automatizar la verificación de la creación de kits con diferentes nombres y parámetros, asegurando que el sistema maneje correctamente una variedad de casos. Los nombres de los kits pueden incluir caracteres especiales, espacios y números, y también se prueban casos límite como la longitud máxima y mínima de los nombres permitidos.

###Estructura del Proyecto
####Módulos Principales
##### sender_stand_request: 
Contiene las funciones para interactuar con la API, incluyendo la creación de usuarios y kits.
##### data: 
Almacena los datos necesarios para las solicitudes, como los cuerpos de las solicitudes y las cabeceras.
Funciones Principales
##### get_kit_body(kit_name)
Genera el cuerpo de la solicitud para la creación de un kit con un nombre dado.

##### positive_assert(kit_name)
Verifica que se pueda crear un kit con éxito.

##### negative_assert(kit_name)
Verifica que la creación de un kit falle cuando se proporcionan nombres no válidos.

##### negative_assert_no_name(kit_body)
Verifica que la creación de un kit falle cuando no se proporciona un nombre.

### Fuente de documentacion
#### ApiDoc
##### Documentación de la API: 
https://cnt-2ea12698-4873-4b81-a6e0-d83e214cc39f.containerhub.tripleten-services.com/docs/

### Descripcion de tecnicas usadas

Las pruebas se ejecutan para verificar diferentes escenarios de creación de kits:

##### test_create_kit_name_1_character: 
Verifica la creación de un kit con un nombre de un solo carácter.
##### test_create_kit_511_characters: 
Verifica la creación de un kit con un nombre de 511 caracteres.
##### test_create_kit_0_character: 
Verifica que falle la creación de un kit con un nombre vacío.
##### test_create_kit_512_characters: 
Verifica que falle la creación de un kit con un nombre de 512 caracteres.
##### test_create_kit_special_characters: 
Verifica la creación de un kit con caracteres especiales en el nombre.
##### test_create_kit_space: 
Verifica la creación de un kit con espacios en el nombre.
##### test_create_kit_string_number: 
Verifica la creación de un kit con números en el nombre.
##### test_create_kit_no_parameters: 
Verifica que falle la creación de un kit cuando no se pasa ningún parámetro.
##### test_create_kit_different_parameter_number: 
Verifica que falle la creación de un kit cuando se pasa un parámetro no válido (número).




