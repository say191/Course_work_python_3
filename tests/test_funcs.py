from funcs import funcs


def test_get_patch():
    assert funcs.get_patch() == "/Users/neymar/Desktop/operations.json"


def test_executed_data():
    assert (funcs.executed_data(
        [{'id': 1, 'state': 'bla'},
         {'id': 2, 'state': 'EXECUTED'}]) ==
            [{'id': 2, 'state': 'EXECUTED'}])


def test_sorted_data_for_date():
    assert (funcs.sorted_data_for_date(
        [{'id': 1, 'date': '2019-05-17T01:50:00.166954'},
         {'id': 2, 'date': '2018-06-16T22:17:01.825020'},
         {'id': 3, 'date': '2019-02-14T17:38:09.910336'}]) ==
            [{'id': 1, 'date': '2019-05-17T01:50:00.166954'},
             {'id': 3, 'date': '2019-02-14T17:38:09.910336'},
             {'id': 2, 'date': '2018-06-16T22:17:01.825020'}])


def test_reformat_date():
    assert funcs.reformat_date('2019-05-17T01:50:00.166954') == '17.05.2019'


def test_reformat_sender():
    assert funcs.reformat_sender('Счет 18125798580985711166') == 'Счет 1812 57** **** 1166'


def test_reformat_recipient():
    assert funcs.reformat_recipient('Счет 98841213648056852372') == 'Счет **2372'
