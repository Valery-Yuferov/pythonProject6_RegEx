from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

import re
num_pattern_raw = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
num_pattern_new = r'+7(\2)\3-\4-\5 \6 \7'
contacts_list_updated_num = list()
for card in contacts_list:
    contacts_list_updated_num.append(re.sub(num_pattern_raw, num_pattern_new,\
                                        ','.join(card)).split(','))
name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
name_pattern_new = r'\1\3\10\4\6\9\7\8'
contacts_list_updated_name = list()
for card in contacts_list_updated_num:
    contacts_list_updated_name.append(re.sub(name_pattern_raw, name_pattern_new,\
                                        ','.join(card)).split(','))

for i in contacts_list_updated_name:
        for j in contacts_list_updated_name:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                for k in range(2, 7):
                    if i[k] == '':
                        i[k] = j[k]
contacts_list_without_duplicates = list()
for card in contacts_list_updated_name:
    if card not in contacts_list_without_duplicates:
        contacts_list_without_duplicates.append(card)
pprint(contacts_list_without_duplicates)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook_result.csv", "w", newline="") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list_without_duplicates)
