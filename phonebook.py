import re
import csv

source_file = 'phonebook_raw.csv'
phone_pattern_1 = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
phone_pattern_2 = r'+7(\3)\6-\8-\10 \12\13'


def data_input():
    with open(source_file, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)
    return contacts_list


def get_new_contact_list(contacts_list):
    new_contacts_list = list()
    for contact in contacts_list:
        new_contact = list()
        full_name_str = ",".join(contact[:3])
        result = re.findall(r'(\w+)', full_name_str)
        while len(result) < 3:
            result.append('')
        new_contact += result
        new_contact.append(contact[3])
        new_contact.append(contact[4])
        phone_pattern = re.compile(phone_pattern_1)
        changed_phone = phone_pattern.sub(phone_pattern_2, contact[5])
        new_contact.append(changed_phone)
        new_contact.append(contact[6])
        new_contacts_list.append(new_contact)
    return new_contacts_list


def delete_duplicates(new_contacts_list):
    phone_book = dict()
    for contact in new_contacts_list:
        if contact[0] in phone_book:
            contact_value = phone_book[contact[0]]
            for i in range(len(contact_value)):
                if contact[i]:
                    contact_value[i] = contact[i]
        else:
            phone_book[contact[0]] = contact
    return list(phone_book.values())


def write_data(new_contacts_list):
    with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)


def start():
    new_contacts_list = data_input()
    new_parsed_list = get_new_contact_list(new_contacts_list)
    contact_book_values = delete_duplicates(new_parsed_list)
    write_data(contact_book_values)


if __name__ == '__main__':
    start()
