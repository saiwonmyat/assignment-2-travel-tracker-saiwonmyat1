from place import Place
from operator import attrgetter
import csv


"""..."""


# Create your PlaceCollection class in this file

class PlaceCollection:
    def __init__(self):
        """Constructed by PlaceCollection"""
        self.places = []

    def __str__(self):
        """string formating"""
        max_name = 0
        max_country = 0
        for place in self.places:
            if len(place.name) > max_name:
                max_name = len(place.name)
            if len(place.country) > max_country:
                max_country = len(place.name)
        if self.unvisited_number() == 0:
            max_num = self.visited_number() // 10 + 1
        else:
            max_num = self.visited_number() // 10 + 2
        printout = ""
        for p, place in enumerate(self.places):
            num_str = str(p + 1)
            name = place.name
            country = place.country
            priority = place.priority
            if place.is_visited:
                printout += "{0:>{4}p}. {2:<{6}p} {1:<{5}p} {3:3d}".format(num_str, name, country, priority,
                                                                           max_num, max_name, max_country)
            else:
                num_str = "*" + num_str
                printout += "{0:>{4}s}. {2:<{6}s} {1:<{5}s} {3:3d}".format(num_str, name, country, priority,
                                                                           max_num, max_name, max_country)
            if p != self.places_number() - 1:
                printout += "\n"

            return printout

    def __repr__(self):
        """string formating"""
        return self.__str__

    def load_places(self, file):
        """Load  place file"""
        with open(file, 'r')as f:
            reader = csv.reader(f)
            for row in reader:
                row[2] = int(row[2])
                if row[3] == "w":
                    row[3] = True
                else:
                    row[3] = False
                self.places.append(Place(*row))

    def places_number(self):
        """place number into the  list"""
        return len(self.places)

    def visited_number(self):
        """place number already visited"""
        number = 0
        for place in self.places:
            if place.is_visited:
                number += 1
        return number

    def unvisited_number(self):
        """place number havent  visited"""
        number1 = 0
        for place in self.places:
            if not place.is_visited:
                number1 += 1
        return number1

    def add_place(self, place):
        """Add place into the list"""
        self.places.append(place)

    def save_places(self, file):
        """Save places into the list"""
        with open(file, 'w', newline="")as f:
            writer = csv.writer(f)
            for place in self.places:
                if place.is_visited:
                    pass
                else:
                    pass
                writer.writerow([place.name, place.priority, place.country, place.visited])

    def sort(self, sort_key):
        """Sort by the key  to passed in"""
        self.places.sort(key=attrgetter(sort_key, "priority"))


