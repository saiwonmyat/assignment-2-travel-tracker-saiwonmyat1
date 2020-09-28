"""
Name: Aung Kaung Myat
Date: 26.9.2020
Brief Project Description:
GitHub URL:
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from place import Place
from placecollection import PlaceCollection

WELCOME = "visited places"
DICTIONARY = dict({"visited": "is_visited", "Name": "name", "Country": "country", "Priority": "priority"})
DATA = "places.csv"
button_color = [1.8, 1.8, 1, 1]


class TravelTrackerApp(App):
    """..."""
    def __init__(self, **kwargs):
        """Creat main app"""
        super().__init__(**kwargs)
        self.text_att = DICTIONARY
        self.sort_method = list(self.text_att.keys())
        self.sort_current = self.sort_method[0]
        self.places = PlaceCollection()
        self.places.load_places(DATA)
        self.information = WELCOME
        Window.size = (1000, 750)

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Places to Visit 2.0"
        self.source = Builder.load_file("app.kv")
        self.button_creat()

        return self.source

    def rank(self, text):
        """sort places"""
        attr = self.text_att[text]
        self.places.sort(attr)
        self.button_creat()

    def button_creat(self):
        """Clear all buttons"""
        self.source.ids.place_button.clear_widgets()
        for i, place in enumerate(self.places.places):
            temp_button = Button(id=str(i))
            temp_button.bind(on_release=self.place_button)
            name = place.name
            country = place.country
            priority = place.priority

            if place.is_visited:
                visited = " (visited)"
                temp_button.background_color = [0.5, 0.5, 1, 1]
            else:
                visited = ""
                temp_button.background_color = button_color
            text = " ''{}'' by {} ({}) {}".format(name, priority, country, visited)
            temp_button.text = text
            self.source.ids.place_button.add_widget(temp_button)

    def add_button(self):
        """Add place button"""
        name = self.source.ids.name.text
        country = self.source.ids.country.text
        priority = self.source.ids.priority.text

        if (name == "") | (country == "") | (priority == ""):
            self.information = "All fields must be completed"
            self.bottom_inf()
        else:
            try:
                priority = int(priority)
                if priority < 1:
                    # if the priority is < 1
                    self.information = "priority must be >=0"
                    self.bottom_inf()
                else:
                    place = Place(name, priority, country)
                    self.places.add_place(place)
                    self.all_inf()
            except ValueError:
                self.information = "Please enter a valid number"
                self.bottom_inf()

    def clear_button(self):
        """Clear button"""
        self.source.ids.name.text = ""
        self.source.ids.country.text = ""
        self.source.ids.priority.text = ""

    def place_button(self, instance):
        """Creat place button"""
        i = int(instance.id)
        place = self.places.places[i]
        if place.is_visited:
            place.unvisited()
            self.information = "You can visit {}".format(place.name)
        else:
            place.visit()
            self.information = "You have visited {}".format(place.name)
        self.all_inf()

    def top_inf(self):
        """Display the information on the top"""
        self.source.ids.top_message.text = "To visit: {}  visited: {}".format(self.places.unvisited_number(),
                                                                              self.places.visited_number())

    def bottom_inf(self):
        """Display the information of bottom"""
        self.source.ids.bottom_message.text = self.information

    def all_inf(self):
        """Display all information"""
        self.button_creat()
        self.top_inf()
        self.bottom_inf()

    def run_exit(self):
        self.places.save_places(DATA)


if __name__ == '__main__':
    TravelTrackerApp().run()
