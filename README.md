﻿# Diplom_2

## Дипломный проект. Задание 2: API

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы тесты на эндпоинты сервиса: создание пользователя, логин пользователя, изменение данных пользователя, 
создание заказа, получение заказов пользователя


### Структура проекта

- `allure-resalts` - пакет c отчетом тестирования
- `tests` - пакет, содержащий тесты на эндпоинты
- - 'test_customer.py' - файл с тестами на изменение данных пользователя
- - - 'test_changing_authorized_customer_data_successfully(name_data, new_data, response_customer)' - 
            проверка изменение имэйла и имени авторизованного покупателя
- - - 'test_changing_unauthorized_customer_data_successfully(name_data, new_data, response_customer_unauthorized)' - 
            проверка изменение имэйла и имени неавторизованного покупателя
- - - 'test_changing_unauthorized_customer_data_successfully(name_data, new_data, response_customer_unauthorized)' - 
            проверка изменение имэйла и имени неавторизованного покупателя
- - - 'test_changing_customer_data_successfully(response, request)' - проверка одновременного изменения всех данных 
            авторизованного/неавторизованного покупателя
- - - 'test_changing_customer_data_error_403(response, request)' - проверка невозможности изменения почты, на уже 
            используемvю у авторизованного/неавторизованного покупателя
- - - 'test_changing_unregistered_customer_data_error_401(new_data)' - проверка невозможности изменения данных 
            без регистрации пользователя
- - 'test_customer_authorization.py' - файл с тестами авторизации пользователя
- - - 'test_authorization_customer_real_data_successfully(response_customer_unauthorized)' - Проверка успешной 
            авторизации покупателя с реальными данными
- - - 'test_authorization_customer_incomplete_data_error(payload_incorrect)' - Проверка авторизации покупателя 
            с некорректным логином/паролем
- - 'test_customer_registration.py' - файл с тестами страницы 'main_page'
- - - 'test_registration_customer_complete_data_successfully()' - Проверка успешной регистрации покупателя 
            с полным набором данных
- - - 'test_registration_customer_double_error(response_customer_unauthorized)' - Проверка невозможности регистрации 
            покупателя с повторяющимся логином
- - - 'test_registration_customer_incomplete_data_error(payload)' - Проверка невозможности регистрации пользователя 
            с неполными обязательными полями
- - 'test_order_create.py' - файл с тестами создания заказа и получения списка заказов пользователя
- - - 'test_create_order_unauthorized_ingredients_successfully(ingredients_order)' - Проверка успешного создания заказа 
            без авторизации(только булка, булка с начинкой, булка с начинкой и соусом)
- - - 'test_create_order_unauthorized_without_ingredients_error()' - Проверка невозможности без авторизации создать 
            заказ без ингредиентов
- - - 'test_create_order_without_authorzied_invalid_ingredient_error(ingredients_order)' - Проверка невозможности 
            без авторизации создать заказ с неверным хэшем ингредиента(с неверным хэшем,с неверным и 
            верным хэшами)
- - - 'test_create_order_authorized_with_ingredients_successfully(ingredients_order, response_customer)' - 
            Проверка успешного создания заказа c авторизацией(только булка, булка с начинкой, 
            булка с начинкой и соусом)
- - - 'test_create_order_authorized_without_ingredients_error(response_customer)' - Проверка невозможности 
            с авторизацией создать заказ без ингредиентов
- - - 'test_create_order_authorized_invalid_ingredient_error(ingredients_order, response_customer)' - 
            Проверка невозможности с авторизацией создать заказ с неверным хэшем ингредиента
            (с неверным хэшем,с неверным и верным хэшами)
- - - 'test_getting_orders_authorized_successfully(response_customer)' - Проверка получения заказов авторизованного 
            покупателя
- - - 'test_getting_orders_unauthorized_error()' - Проверка получения заказов без авторизации
- 'conftest.py' - файл с фикстурами
- - 'response_customer()' - Регистрация нового тестового покупателя, авторизация и последующее удаление
- - 'response_customer_unauthorized()' - Регистрация нового тестового покупателя и последующее удаление
- 'data.py' - файл с тестовыми данными
- 'helpers.py' - файл со вспомогательными функциями
- - 'generate_string()' - Генерация строкового значения
- - 'generate_email()' - Генерация email
- - 'generate_data_customer()' - Генерация данных покупателя для регистрации
- - 'generate_ingredient()' - Генерация ингредиента
- - 'customer_registration()' - Регистрация курьера
- - 'customer_authorization()' - Авторизация курьера
- - 'delete_customer()' - Удаление курьера
- 'requirements.txt' - файл с внешними зависимостями
    

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`
 
**Запуск автотестов и генерирация Allure-отчёта**

> `$ pytest --alluredir=allure_results'
> '$ allure serve allure_results'


