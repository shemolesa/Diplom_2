
URL = 'https://stellarburgers.nomoreparties.site/'
URL_CUSTOMER_REG = 'https://stellarburgers.nomoreparties.site/api/auth/register'
URL_CUSTOMER = URL + 'api/auth/user'
URL_CUSTOMER_LOGIN = URL + 'api/auth/login'
URL_INGREDIENTS = URL + 'api/ingredients'
URL_ORDERS = URL + 'api/orders'


TEST_CUSTOMER = {
    'email': 'test-email112111@yandex.ru',
    'password': 'test_passwordz11111',
    'name': 'test_namez12111121'
}
NEW_CUSTOMER = {
    'email': 'new-1emai2l111@yandex.ru',
    'password': 'new_1pass2wordz111',
    'name': 'new_1na2mez12111'
}


MENU_BUNS = ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6c']
MENU_FILLINGS = ['61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa70', '61c0c5a71d1f82001bdaaa71', '61c0c5a71d1f82001bdaaa6e','61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa77', '61c0c5a71d1f82001bdaaa78', '61c0c5a71d1f82001bdaaa79', '61c0c5a71d1f82001bdaaa7a']
MENU_SAUCES = ['61c0c5a71d1f82001bdaaa72', '61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa75']

REGISTRATION_MESSAGE_403 = 'User already exists'
REGISTRATION_MESSAGE_NOT_ENOUGH_DATA_403 = 'Email, password and name are required fields'
AUTHORIZATION_MESSAGE_INCORRECT_DATA_401 = 'email or password are incorrect'
CHANGE_MESSAGE_403 = 'User with such email already exists'
CHANGE_MESSAGE_UNREGISTERED_401 = 'You should be authorised'
CREATE_ORDER_MESSAGE_400 = 'Ingredient ids must be provided'
GET_ORDERS_MESSAGE_401 = 'You should be authorised'
