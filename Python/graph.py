import csv
import pygal

users_data1 = []
subs_data1 = []
views_data1 = []


with open('../Database/auto.txt') as csvfile_auto:
    readfile_auto = csv.reader(csvfile_auto, delimiter=',')

    for line in readfile_auto:
        user_data1 = str(line[0])
        sub_data1 = int(line[1])
        view_data1 = int(line[2])
        users_data1.append(user_data1)
        subs_data1.append(sub_data1)
        views_data1.append(view_data1)

# print(users_data1, subs_data1, views_data1)

pie_chart = pygal.Pie()
pie_chart.title = 'AUTOS & VEHICLES'
pie_chart.add(users_data1[0], views_data1[0])
pie_chart.add(users_data1[1], views_data1[1])
pie_chart.add(users_data1[2], views_data1[2])
pie_chart.add(users_data1[3], views_data1[3])
pie_chart.add(users_data1[4], views_data1[4])
pie_chart.add(users_data1[5], views_data1[5])
pie_chart.add(users_data1[6], views_data1[6])
pie_chart.add(users_data1[7], views_data1[7])
pie_chart.add(users_data1[8], views_data1[8])
pie_chart.add(users_data1[9], views_data1[9])
pie_chart.render_to_file('Pie_auto.svg')

users_data2 = []
subs_data2 = []
views_data2 = []

with open('../Database/COMEDY.txt') as csvfile_com:
    readfile_com = csv.reader(csvfile_com, delimiter=',')

    for line1 in readfile_com:
        user_data2 = str(line1[0])
        sub_data2 = int(line1[1])
        view_data2 = int(line1[2])
        users_data2.append(user_data2)
        subs_data2.append(sub_data2)
        views_data2.append(view_data2)

# print(users_data2, subs_data2, views_data2)

pie_chart = pygal.Pie()
pie_chart.title = 'COMEDY'
pie_chart.add(users_data2[0], views_data2[0])
pie_chart.add(users_data2[1], views_data2[1])
pie_chart.add(users_data2[2], views_data2[2])
pie_chart.add(users_data2[3], views_data2[3])
pie_chart.add(users_data2[4], views_data2[4])
pie_chart.add(users_data2[5], views_data2[5])
pie_chart.add(users_data2[6], views_data2[6])
pie_chart.add(users_data2[7], views_data2[7])
pie_chart.add(users_data2[8], views_data2[8])
pie_chart.add(users_data2[9], views_data2[9])
pie_chart.render_to_file('Pie_com.svg')

users_data2 = []
subs_data2 = []
views_data2 = []

with open('../Database/COMEDY.txt') as csvfile_com:
    readfile_com = csv.reader(csvfile_com, delimiter=',')

    for line in readfile_com:
        user_data2 = str(line[0])
        sub_data2 = int(line[1])
        view_data2 = int(line[2])
        users_data2.append(user_data2)
        subs_data2.append(sub_data2)
        views_data2.append(view_data2)

# print(users_data2, subs_data2, views_data2)

pie_chart = pygal.Pie()
pie_chart.title = 'COMEDY'
pie_chart.add(users_data2[0], views_data2[0])
pie_chart.add(users_data2[1], views_data2[1])
pie_chart.add(users_data2[2], views_data2[2])
pie_chart.add(users_data2[3], views_data2[3])
pie_chart.add(users_data2[4], views_data2[4])
pie_chart.add(users_data2[5], views_data2[5])
pie_chart.add(users_data2[6], views_data2[6])
pie_chart.add(users_data2[7], views_data2[7])
pie_chart.add(users_data2[8], views_data2[8])
pie_chart.add(users_data2[9], views_data2[9])
pie_chart.render_to_file('Pie_com.svg')

users_data3 = []
subs_data3 = []
views_data3 = []

with open('../Database/EDUCATION.txt') as csvfile_edu:
    readfile_edu = csv.reader(csvfile_edu, delimiter=',')

    for line in readfile_edu:
        user_data3 = str(line[0])
        sub_data3 = int(line[1])
        view_data3 = int(line[2])
        users_data3.append(user_data3)
        subs_data3.append(sub_data3)
        views_data3.append(view_data3)

# print(users_data3, subs_data3, views_data3)

pie_chart = pygal.Pie()
pie_chart.title = 'EDUCATION'
pie_chart.add(users_data3[0], views_data3[0])
pie_chart.add(users_data3[1], views_data3[1])
pie_chart.add(users_data3[2], views_data3[2])
pie_chart.add(users_data3[3], views_data3[3])
pie_chart.add(users_data3[4], views_data3[4])
pie_chart.add(users_data3[5], views_data3[5])
pie_chart.add(users_data3[6], views_data3[6])
pie_chart.add(users_data3[7], views_data3[7])
pie_chart.add(users_data3[8], views_data3[8])
pie_chart.add(users_data3[9], views_data3[9])
pie_chart.render_to_file('Pie_edu.svg')

users_data4 = []
subs_data4 = []
views_data4 = []

with open('../Database/ENTERTAINMENT.txt') as csvfile_entertain:
    readfile_entertain = csv.reader(csvfile_entertain, delimiter=',')

    for line in readfile_entertain:
        user_data4 = str(line[0])
        sub_data4 = int(line[1])
        view_data4 = int(line[2])
        users_data4.append(user_data4)
        subs_data4.append(sub_data4)
        views_data4.append(view_data4)

# print(users_data4, subs_data4, views_data4)

pie_chart = pygal.Pie()
pie_chart.title = 'ENTERTAINMENT'
pie_chart.add(users_data4[0], views_data4[0])
pie_chart.add(users_data4[1], views_data4[1])
pie_chart.add(users_data4[2], views_data4[2])
pie_chart.add(users_data4[3], views_data4[3])
pie_chart.add(users_data4[4], views_data4[4])
pie_chart.add(users_data4[5], views_data4[5])
pie_chart.add(users_data4[6], views_data4[6])
pie_chart.add(users_data4[7], views_data4[7])
pie_chart.add(users_data4[8], views_data4[8])
pie_chart.add(users_data4[9], views_data4[9])
pie_chart.render_to_file('Pie_entertain.svg')