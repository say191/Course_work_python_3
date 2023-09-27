import json  # Импортируем библиотеку json для работы с json файлом

from funcs import funcs  # Импортируем все необходимые функции

with open(funcs.get_patch(), 'r') as file:  # Открываем файл 'operations.json'
    data = json.load(file)  # Считываем данные с файла 'operations.json'

executed_data = funcs.executed_data(data)  # Отсеиваем незавершенные транзакции с помощью функции

sorted_executed_data = funcs.sorted_data_for_date(executed_data)  # Сортируем транзакции по датам

last_transfers = []  # Создаем пустой спиок, куда будут помещаться экземпляры поледних транзаций (классов).

while len(last_transfers) < 5:  # Цикл while будет работать 5 раз, т к нам нужны пять последних транзакций
    if 'from' in sorted_executed_data[len(last_transfers)].keys():
        # Проверяем какой класс нам использовать. Если в словаре есть ключ 'from', то создаем экземпляр класа
        # 'Operation'
        exemplar = funcs.create_exemplar_operation(sorted_executed_data[len(last_transfers)])
        # Создаем экземпляр класса 'Operation'

        exemplar.date = funcs.reformat_date(exemplar.date)  # Меняем формат даты транзакции внутри экземпляра класса
        exemplar.sender = funcs.reformat_sender(exemplar.sender)  # Меняем формат счета отправителя внутри экземпляра
        exemplar.recipient = funcs.reformat_recipient(exemplar.recipient)  # Меняем формат счета получателя

        last_transfers.append(exemplar)  # Добавляем экземпляр класса в список

    else:
        exemplar = funcs.create_exemplar_deposit(sorted_executed_data[len(last_transfers)])
        # Если в словаре нету ключа 'from', то создаем экземпляр класса 'Deposit'
        exemplar.date = funcs.reformat_date(exemplar.date)  # Меняем формат даты
        exemplar.recipient = funcs.reformat_recipient(exemplar.recipient)  # Меняем формат счета получателя

        last_transfers.append(exemplar)  # Добавляем экземпляр класса в список

for i in last_transfers:
    print(f"{i}\n")  # Выводим на экран необходимую информации об транзакции разделяя их пустой строчкой
