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

line_chart = pygal.HorizontalBar()
line_chart.title = 'AUTOS & VEHICLES'
line_chart.add(users_data1[0], views_data1[0])
line_chart.add(users_data1[1], views_data1[1])
line_chart.add(users_data1[2], views_data1[2])
line_chart.add(users_data1[3], views_data1[3])
line_chart.add(users_data1[4], views_data1[4])
line_chart.add(users_data1[5], views_data1[5])
line_chart.add(users_data1[6], views_data1[6])
line_chart.add(users_data1[7], views_data1[7])
line_chart.add(users_data1[8], views_data1[8])
line_chart.add(users_data1[9], views_data1[9])
line_chart.render_to_file('Line_auto.svg')

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

users_data5 = []
subs_data5 = []
views_data5 = []

with open('../Database/film.txt') as csvfile_flim:
    readfile_flim = csv.reader(csvfile_flim, delimiter=',')

    for line in readfile_flim:
        user_data5 = str(line[0])
        sub_data5 = int(line[1])
        view_data5 = int(line[2])
        users_data5.append(user_data5)
        subs_data5.append(sub_data5)
        views_data5.append(view_data5)

# print(users_data5, subs_data5, views_data5)

pie_chart = pygal.Pie()
pie_chart.title = 'FILM'
pie_chart.add(users_data5[0], views_data5[0])
pie_chart.add(users_data5[1], views_data5[1])
pie_chart.add(users_data5[2], views_data5[2])
pie_chart.add(users_data5[3], views_data5[3])
pie_chart.add(users_data5[4], views_data5[4])
pie_chart.add(users_data5[5], views_data5[5])
pie_chart.add(users_data5[6], views_data5[6])
pie_chart.add(users_data5[7], views_data5[7])
pie_chart.add(users_data5[8], views_data5[8])
pie_chart.add(users_data5[9], views_data5[9])
pie_chart.render_to_file('Pie_film.svg')

users_data5 = []
subs_data5 = []
views_data5 = []

with open('../Database/film.txt') as csvfile_flim:
    readfile_flim = csv.reader(csvfile_flim, delimiter=',')

    for line in readfile_flim:
        user_data5 = str(line[0])
        sub_data5 = int(line[1])
        view_data5 = int(line[2])
        users_data5.append(user_data5)
        subs_data5.append(sub_data5)
        views_data5.append(view_data5)

# print(users_data5, subs_data5, views_data5)

pie_chart = pygal.Pie()
pie_chart.title = 'FILM'
pie_chart.add(users_data5[0], views_data5[0])
pie_chart.add(users_data5[1], views_data5[1])
pie_chart.add(users_data5[2], views_data5[2])
pie_chart.add(users_data5[3], views_data5[3])
pie_chart.add(users_data5[4], views_data5[4])
pie_chart.add(users_data5[5], views_data5[5])
pie_chart.add(users_data5[6], views_data5[6])
pie_chart.add(users_data5[7], views_data5[7])
pie_chart.add(users_data5[8], views_data5[8])
pie_chart.add(users_data5[9], views_data5[9])
pie_chart.render_to_file('Pie_film.svg')

users_data6 = []
subs_data6 = []
views_data6 = []

with open('../Database/gaming.txt') as csvfile_gamimg:
    readfile_gamimg = csv.reader(csvfile_gamimg, delimiter=',')

    for line in readfile_gamimg:
        user_data6 = str(line[0])
        sub_data6 = int(line[1])
        view_data6 = int(line[2])
        users_data6.append(user_data6)
        subs_data6.append(sub_data6)
        views_data6.append(view_data6)

# print(users_data6, subs_data6, views_data6)

pie_chart = pygal.Pie()
pie_chart.title = 'GAMIMG'
pie_chart.add(users_data6[0], views_data6[0])
pie_chart.add(users_data6[1], views_data6[1])
pie_chart.add(users_data6[2], views_data6[2])
pie_chart.add(users_data6[3], views_data6[3])
pie_chart.add(users_data6[4], views_data6[4])
pie_chart.add(users_data6[5], views_data6[5])
pie_chart.add(users_data6[6], views_data6[6])
pie_chart.add(users_data6[7], views_data6[7])
pie_chart.add(users_data6[8], views_data6[8])
pie_chart.add(users_data6[9], views_data6[9])
pie_chart.render_to_file('Pie_gamimg.svg')

users_data7 = []
subs_data7 = []
views_data7 = []

with open('../Database/howto.txt') as csvfile_howto:
    readfile_howto = csv.reader(csvfile_howto, delimiter=',')

    for line in readfile_howto:
        user_data7 = str(line[0])
        sub_data7 = int(line[1])
        view_data7 = int(line[2])
        users_data7.append(user_data7)
        subs_data7.append(sub_data7)
        views_data7.append(view_data7)

# print(users_data7, subs_data7, views_data7)

pie_chart = pygal.Pie()
pie_chart.title = 'HOW TO & STYLE'
pie_chart.add(users_data7[0], views_data7[0])
pie_chart.add(users_data7[1], views_data7[1])
pie_chart.add(users_data7[2], views_data7[2])
pie_chart.add(users_data7[3], views_data7[3])
pie_chart.add(users_data7[4], views_data7[4])
pie_chart.add(users_data7[5], views_data7[5])
pie_chart.add(users_data7[6], views_data7[6])
pie_chart.add(users_data7[7], views_data7[7])
pie_chart.add(users_data7[8], views_data7[8])
pie_chart.add(users_data7[9], views_data7[9])
pie_chart.render_to_file('Pie_howto.svg')

users_data8 = []
subs_data8 = []
views_data8 = []

with open('../Database/music.txt') as csvfile_music:
    readfile_music = csv.reader(csvfile_music, delimiter=',')

    for line in readfile_music:
        user_data8 = str(line[0])
        sub_data8 = int(line[1])
        view_data8 = int(line[2])
        users_data8.append(user_data8)
        subs_data8.append(sub_data8)
        views_data8.append(view_data8)

# print(users_data8, subs_data8, views_data8)

pie_chart = pygal.Pie()
pie_chart.title = 'MUSIC'
pie_chart.add(users_data8[0], views_data8[0])
pie_chart.add(users_data8[1], views_data8[1])
pie_chart.add(users_data8[2], views_data8[2])
pie_chart.add(users_data8[3], views_data8[3])
pie_chart.add(users_data8[4], views_data8[4])
pie_chart.add(users_data8[5], views_data8[5])
pie_chart.add(users_data8[6], views_data8[6])
pie_chart.add(users_data8[7], views_data8[7])
pie_chart.add(users_data8[8], views_data8[8])
pie_chart.add(users_data8[9], views_data8[9])
pie_chart.render_to_file('Pie_music.svg')

users_data9 = []
subs_data9 = []
views_data9 = []

with open('../Database/news.txt') as csvfile_news:
    readfile_news = csv.reader(csvfile_news, delimiter=',')

    for line in readfile_news:
        user_data9 = str(line[0])
        sub_data9 = int(line[1])
        view_data9 = int(line[2])
        users_data9.append(user_data9)
        subs_data9.append(sub_data9)
        views_data9.append(view_data9)

# print(users_data9, subs_data9, views_data9)

pie_chart = pygal.Pie()
pie_chart.title = 'NEWS'
pie_chart.add(users_data9[0], views_data9[0])
pie_chart.add(users_data9[1], views_data9[1])
pie_chart.add(users_data9[2], views_data9[2])
pie_chart.add(users_data9[3], views_data9[3])
pie_chart.add(users_data9[4], views_data9[4])
pie_chart.add(users_data9[5], views_data9[5])
pie_chart.add(users_data9[6], views_data9[6])
pie_chart.add(users_data9[7], views_data9[7])
pie_chart.add(users_data9[8], views_data9[8])
pie_chart.add(users_data9[9], views_data9[9])
pie_chart.render_to_file('Pie_news.svg')

users_data10 = []
subs_data10 = []
views_data10 = []

with open('../Database/Travel.txt') as csvfile_Travel:
    readfile_Travel = csv.reader(csvfile_Travel, delimiter=',')

    for line in readfile_Travel:
        user_data10 = str(line[0])
        sub_data10 = int(line[1])
        view_data10 = int(line[2])
        users_data10.append(user_data10)
        subs_data10.append(sub_data10)
        views_data10.append(view_data10)

# print(users_data10, subs_data10, views_data10)

pie_chart = pygal.Pie()
pie_chart.title = 'TRAVEL'
pie_chart.add(users_data10[0], views_data10[0])
pie_chart.add(users_data10[1], views_data10[1])
pie_chart.add(users_data10[2], views_data10[2])
pie_chart.add(users_data10[3], views_data10[3])
pie_chart.add(users_data10[4], views_data10[4])
pie_chart.add(users_data10[5], views_data10[5])
pie_chart.add(users_data10[6], views_data10[6])
pie_chart.add(users_data10[7], views_data10[7])
pie_chart.add(users_data10[8], views_data10[8])
pie_chart.add(users_data10[9], views_data10[9])
pie_chart.render_to_file('Pie_travel.svg')

users_data11 = []
subs_data11 = []
views_data11 = []

with open('../Database/nonprofit.txt') as csvfile_nonprofit:
    readfile_nonprofit = csv.reader(csvfile_nonprofit, delimiter=',')

    for line in readfile_nonprofit:
        user_data11 = str(line[0])
        sub_data11 = int(line[1])
        view_data11 = int(line[2])
        users_data11.append(user_data11)
        subs_data11.append(sub_data11)
        views_data11.append(view_data11)

# print(users_data11, subs_data11, views_data11)

pie_chart = pygal.Pie()
pie_chart.title = 'NONPROFIT'
pie_chart.add(users_data11[0], views_data11[0])
pie_chart.add(users_data11[1], views_data11[1])
pie_chart.add(users_data11[2], views_data11[2])
pie_chart.add(users_data11[3], views_data11[3])
pie_chart.add(users_data11[4], views_data11[4])
pie_chart.add(users_data11[5], views_data11[5])
pie_chart.add(users_data11[6], views_data11[6])
pie_chart.add(users_data11[7], views_data11[7])
pie_chart.add(users_data11[8], views_data11[8])
pie_chart.add(users_data11[9], views_data11[9])
pie_chart.render_to_file('Pie_nonprofit.svg')

users_data12 = []
subs_data12 = []
views_data12 = []

with open('../Database/people.txt') as csvfile_people:
    readfile_people = csv.reader(csvfile_people, delimiter=',')

    for line in readfile_people:
        user_data12 = str(line[0])
        sub_data12 = int(line[1])
        view_data12 = int(line[2])
        users_data12.append(user_data12)
        subs_data12.append(sub_data12)
        views_data12.append(view_data12)

# print(users_data12, subs_data12, views_data12)

pie_chart = pygal.Pie()
pie_chart.title = 'PEOPLE'
pie_chart.add(users_data12[0], views_data12[0])
pie_chart.add(users_data12[1], views_data12[1])
pie_chart.add(users_data12[2], views_data12[2])
pie_chart.add(users_data12[3], views_data12[3])
pie_chart.add(users_data12[4], views_data12[4])
pie_chart.add(users_data12[5], views_data12[5])
pie_chart.add(users_data12[6], views_data12[6])
pie_chart.add(users_data12[7], views_data12[7])
pie_chart.add(users_data12[8], views_data12[8])
pie_chart.add(users_data12[9], views_data12[9])
pie_chart.render_to_file('Pie_people.svg')

users_data13 = []
subs_data13 = []
views_data13 = []

with open('../Database/pets.txt') as csvfile_pet:
    readfile_pet = csv.reader(csvfile_pet, delimiter=',')

    for line in readfile_pet:
        user_data13 = str(line[0])
        sub_data13 = int(line[1])
        view_data13 = int(line[2])
        users_data13.append(user_data13)
        subs_data13.append(sub_data13)
        views_data13.append(view_data13)

# print(users_data13, subs_data13, views_data13)

pie_chart = pygal.Pie()
pie_chart.title = 'PETS'
pie_chart.add(users_data13[0], views_data13[0])
pie_chart.add(users_data13[1], views_data13[1])
pie_chart.add(users_data13[2], views_data13[2])
pie_chart.add(users_data13[3], views_data13[3])
pie_chart.add(users_data13[4], views_data13[4])
pie_chart.add(users_data13[5], views_data13[5])
pie_chart.add(users_data13[6], views_data13[6])
pie_chart.add(users_data13[7], views_data13[7])
pie_chart.add(users_data13[8], views_data13[8])
pie_chart.add(users_data13[9], views_data13[9])
pie_chart.render_to_file('Pie_pet.svg')

users_data14 = []
subs_data14 = []
views_data14 = []

with open('../Database/Science-Tecgnology.txt') as csvfile_sci:
    readfile_sci = csv.reader(csvfile_sci, delimiter=',')

    for line in readfile_sci:
        user_data14 = str(line[0])
        sub_data14 = int(line[1])
        view_data14 = int(line[2])
        users_data14.append(user_data14)
        subs_data14.append(sub_data14)
        views_data14.append(view_data14)

# print(users_data14, subs_data14, views_data14)

pie_chart = pygal.Pie()
pie_chart.title = 'SCIENCE & TECGNOLOGY'
pie_chart.add(users_data14[0], views_data14[0])
pie_chart.add(users_data14[1], views_data14[1])
pie_chart.add(users_data14[2], views_data14[2])
pie_chart.add(users_data14[3], views_data14[3])
pie_chart.add(users_data14[4], views_data14[4])
pie_chart.add(users_data14[5], views_data14[5])
pie_chart.add(users_data14[6], views_data14[6])
pie_chart.add(users_data14[7], views_data14[7])
pie_chart.add(users_data14[8], views_data14[8])
pie_chart.add(users_data14[9], views_data14[9])
pie_chart.render_to_file('Pie_sci.svg')

users_data15 = []
subs_data15 = []
views_data15 = []

with open('../Database/Shows.txt') as csvfile_show:
    readfile_show = csv.reader(csvfile_show, delimiter=',')

    for line in readfile_show:
        user_data15 = str(line[0])
        sub_data15 = int(line[1])
        view_data15 = int(line[2])
        users_data15.append(user_data15)
        subs_data15.append(sub_data15)
        views_data15.append(view_data15)

# print(users_data15, subs_data15, views_data15)

pie_chart = pygal.Pie()
pie_chart.title = 'SHOWS'
pie_chart.add(users_data15[0], views_data15[0])
pie_chart.add(users_data15[1], views_data15[1])
pie_chart.add(users_data15[2], views_data15[2])
pie_chart.add(users_data15[3], views_data15[3])
pie_chart.add(users_data15[4], views_data15[4])
pie_chart.add(users_data15[5], views_data15[5])
pie_chart.add(users_data15[6], views_data15[6])
pie_chart.add(users_data15[7], views_data15[7])
pie_chart.add(users_data15[8], views_data15[8])
pie_chart.add(users_data15[9], views_data15[9])
pie_chart.render_to_file('Pie_show.svg')

users_data16 = []
subs_data16 = []
views_data16 = []

with open('../Database/Sports.txt') as csvfile_sport:
    readfile_sport = csv.reader(csvfile_sport, delimiter=',')

    for line in readfile_sport:
        user_data16 = str(line[0])
        sub_data16 = int(line[1])
        view_data16 = int(line[2])
        users_data16.append(user_data16)
        subs_data16.append(sub_data16)
        views_data16.append(view_data16)

# print(users_data16, subs_data16, views_data16)

pie_chart = pygal.Pie()
pie_chart.title = 'SPORTS'
pie_chart.add(users_data16[0], views_data16[0])
pie_chart.add(users_data16[1], views_data16[1])
pie_chart.add(users_data16[2], views_data16[2])
pie_chart.add(users_data16[3], views_data16[3])
pie_chart.add(users_data16[4], views_data16[4])
pie_chart.add(users_data16[5], views_data16[5])
pie_chart.add(users_data16[6], views_data16[6])
pie_chart.add(users_data16[7], views_data16[7])
pie_chart.add(users_data16[8], views_data16[8])
pie_chart.add(users_data16[9], views_data16[9])
pie_chart.render_to_file('Pie_sport.svg')