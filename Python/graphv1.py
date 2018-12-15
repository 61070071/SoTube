import csv

users_data1 = []
subs_data1 = []
views_data1 = []

with open('../Database/auto.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        user_data1 = str(line[0])
        sub_data1 = int(line[1])
        view_data1 = int(line[2])
        users_data1.append(user_data1)
        subs_data1.append(sub_data1)
        views_data1.append(view_data1)

print(users_data1, subs_data1)
