import csv
import json

books_list = []

users_list = []

with open('../data/books.csv', 'r', newline='') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        books_list.append(
            {'title': row['Title'], 'author': row['Author'], 'pages': row['Pages'], 'genre': row['Genre']})
with open('../data/users.json', 'r') as file2:
    users = json.load(file2)
for user in users:
    users_list.append(
        {'name': user['name'], 'gender': user['gender'], 'address': user['address'], 'age': user['age'], 'books': []})

number_of_users = len(users_list)
usr_count = 0
for book in books_list:
    users_list[usr_count]['books'].append(book)
    usr_count = usr_count + 1
    if usr_count >= number_of_users:
        usr_count = 0

with open('result.json', 'w') as result:
    json.dump(users_list, result, indent=4)
