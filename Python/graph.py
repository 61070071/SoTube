import csv
import pygal

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
pie_chart.render_to_file('bartest.svg')