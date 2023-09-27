import os  # Импортируем библиотеку os для работы с директориями проекта
from classes import classes  # Импортируем необходимые классы, а именно класс Operation


def get_patch():
    os.chdir('..')  # Переходим в корневую директорию проекта
    dir_if_project = os.getcwd()
    patch = dir_if_project + '/operations.json'  # Записывае путь до файла 'operation.json'
    return patch


"""
Функция для определения корректного пути до файла 'operation.json'.
Т к проект будет загружен в удаленный репозиторий на github и 'operation.json'
расположен в корневой директории проекта. То у других пользователей с отличной
файловой системой от моей могут возникнуть проблемы, т к путь до вышеуказанного файла
будет другим.
Эта функция решают эту проблему, считывая путь до 'operation.json' самостоятельно и
возвращая этот путь.
"""


def executed_data(data: list):
    done_transfers = []  # Создаем пустой список, куда будем добавлять выполненные транзакции
    for transfer in data:  # Пробегаемся по транзакциям в списке
        if len(transfer) != 0:  # Исключаем попадания в список пустых строчек
            if transfer['state'] == 'EXECUTED':  # Добавляем в список транзакцию со статусом 'EXECUTED'
                done_transfers.append(transfer)
        else:
            continue
    return done_transfers


"""
Функция служит для отсеивания, незавершенных по различным причинам, транзакций.
Она возвращает список из упешно выполненных транзакций.
"""


def get_data_for_sort(res):
    return res['date']


"""
Функция нужна исключительно для следующий функции 'sorted_data_for_date'.
Она возвращает значение по ключу для дальнейшей сортировки.
"""


def sorted_data_for_date(data: list):
    return sorted(data, key=get_data_for_sort, reverse=True)  # Сортируем словарь


"""
Функция позволяет сортировать список из словарей по значениям определенного ключа.
Она нужна для сортировки в порядке убывания транзакций по дате.
Возвращает сортированный по датам список транзакций.
"""


def create_exemplar_operation(transfer: dict):  # Создаем экземпляр класса 'Operation'
    transfer_ = classes.Operation(transfer['date'], transfer['description'], transfer['from'],
                                  transfer['to'], transfer['operationAmount']['amount'],
                                  transfer['operationAmount']['currency']['name'])
    return transfer_


"""
Функция служит для создания экземпляров класса 'Operation' с полями, необходимыми 
по условию выполнения задачи, а именно: дата, описание транзакции, отправитель, получатель,
сумма и валюта.
Возвращает экземпляр класса 'Operation'.
"""


def create_exemplar_deposit(deposit: dict):  # Создаем экземпляр класса 'Deposit'
    deposit_ = classes.Deposit(deposit['date'], deposit['description'],
                               deposit['to'], deposit['operationAmount']['amount'],
                               deposit['operationAmount']['currency']['name'])
    return deposit_


"""
Функция служит для создания экземпляров класса 'Deposit' с полями, необходимыми 
по условию выполнения задачи, а именно: дата, описание транзакции, получатель, сумма и валюта.
Возвращает экземпляр класса 'Deposit'.
"""


def reformat_date(date: str):
    new_format = date[8:10] + '.' + date[5:7] + '.' + date[:4]  # Меняем формат даты
    return new_format


"""
Функция служит для изменения формата даты.
Возвращает новый формат даты.
"""


def reformat_sender(count: str):
    count_split = count.split(' ')  # Разбиваем строку по пробелам
    for part in count_split:  # Пробегаемся по списку из разбитыз строк
        if part.isdigit():  # Выбираем строку с номером счета или карты , состоящую из цифр
            new_format = part[:4] + ' ' + part[4:6] + '** **** ' + part[-4:]  # Меняем формат счета или карты
            return ' '.join(count_split[:-1]) + ' ' + new_format
        else:
            continue
    return count  # Если у транзакции статус анонима, то формат менять нету необходимости


"""
Функция служит для изменения формата счета отправителя, маскируя номер счета или карты.
Возвращает новый формат счета отправителя.
"""


def reformat_recipient(count: str):
    count_split = count.split(' ')
    for part in count_split:
        if part.isdigit():
            new_format = '**' + part[-4:]
            return ' '.join(count_split[:-1]) + ' ' + new_format


"""
Функция служит для изменения формата счета получателя, маскируя номер счета или карты.
Возвращает новый формат счета получателя.
"""
