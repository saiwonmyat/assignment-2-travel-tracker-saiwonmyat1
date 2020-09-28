"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place


import csv
from operator import attrgetter,itemgetter

def main(): #Read file
    print("Travel Tracker 1.0 - by <Aung Kaung Myat>")
    reader = open("places.csv","r")
    user_choice = reader.readlines()
    place_data=for_read(user_choice) #formart[4***]
    reader.close()
    print(place_data)
    print("{} places loaded form places.csv".format(len(place_data)))

    while True:

        place_data.sort(key=itemgetter(1))
        place_data.sort(key=attrgetter("*"))


        menu()
        menu_input = str(input(">>> ")).upper()

        if menu_input == "L":
            list_place(place_data)

        elif menu_input == "A":
            newadd_places(place_data)
            place_data.append(newadd_places)

        elif menu_input == "M":
            list_place(place_data)
            marked_place(place_data)

        elif menu_input == "Q":
            written_places(place_data)

        else:
         print ("invalid")

def menu():#Menu 1
    print("Menu: ")
    print ("L - List places")
    print ("A - Add new place")
    print ("M - Mark a place as visited")
    print ("Q - Quit")


def for_read(user_choice):# funtion for read code 2
    place_list =[]

    for a in user_choice:
        place_list.append(a.strip().split(","))

    for v in place_list:
        if v[3] == "n":
            v[3] = "*"
        elif v[3] == "v":
            v[3] = " "
    for pri in place_list:
        pri[2]=int (pri[2])
        ans=sorted(place_list)
    return ans

def list_place(place_data): #functionn for list 3
    for place , p in enumerate(place_data,1):
        print("{} {}. {:40} - {:20} ({})".format(p[3], place, p[0], p[1], p[2]))

    unvisited = 0
    all_places = 0
    for p in place_data:
        all_places = len(place_data)
        count= p.count("*")
        unvisited = unvisited + count
        visit= all_places - unvisited

    if unvisited == 0:
        print("No more places")

    else:
        print(all_places, "places. You still want to visited,", unvisited, "places")
def newadd_places(place_data):
    new_list = []
    loop = True
    while loop:
        try:
            name = input ("Name: ")
            if name == " ":
                print ("Input can not be blank")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid name")

    while loop:
        try:
            country = input("Country: ")
            if country == " ":
                print("Input can not be blank")
            else:
                break
        except ValueError:
            print ("Invalid input; enter a valid number")

    while loop:
        try:
            priority = int(input("Priority: "))
            if priority == " " or priority <=0:
              print("Invalid input: enter a valid number")
            else:
              break
        except ValueError:
            print("Invalid input: enter a valid number")

    new_list.append(name)
    new_list.append(country)
    new_list.append(priority)
    new_list.append("*")
    print(name, "in", country, "(", priority, ")", "added to travel  tracker")
    return new_list
#finction for mark
def marked_place(place_data):
    print("Enter the number of a place to mark as visited")
    while True:
        try:
            place_number = int (input(">>> "))
            count_place = len(place_data)

            if place_number > count_place:
                print("Invalid place number")

            elif place_number <0:
                print("Number must be >= 0")

            else:
                for place in place_data[place_number:place_number+1]:
                    if place[3] == " ":
                        print("No unvisited places", place[0])
                    else:
                        place[3] = " "
                        print(place[0], "by", place[1], "visited")
                break

        except ValueError:
            print("Invalid input; enter a valid number")


def written_places(place_data):
    reader = open("places.csv","w")

    for p in place_data:
        if p[3] == "*":
            p[3] = "u"
        elif p[3] == " ":
            p[3] = "v"

    for a in place_data:
        print(a[0] + ",", a[1], ",", a[2], ",", a[3], file=reader)

    reader.close()
    all_places = len(place_data)

    print(all_places,"places save to places.csv")
    print("Have a nice day :)")
main()