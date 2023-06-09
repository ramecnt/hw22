# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def get_users_list():
    # Чтение данных из строки
    def _read(str):
        return [i.split(";") for i in str.split('\n')]

    def _sort(data):
        return sorted(data, key=lambda x: int(x[1]))

    def _filter(data):
        return [i for i in data if int(i[1]) > 10]

    data = _read(csv)
    data = _sort(data)
    return _filter(data)


if __name__ == '__main__':
    print(get_users_list())
