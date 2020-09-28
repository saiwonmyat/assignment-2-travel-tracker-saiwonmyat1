"""..."""

# Create your Place class in this file



class Place:
    def __init__(self, name="",  country="", priority=0, is_visited=False):
        """Create a visit class"""
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        """Determine visit"""
        if self.is_visited:
            visit = "v"
        else:
            visit = "u"
        return "{} {} ({}) {}".format(self.name, self.country, self.priority, visit)

    def unvisit(self):
        """Make unvisited if the visit is not visit"""
        self.is_visited  = False

    def visit(self):
        """Make vsiit to vistied when visit is visited"""
        self.is_visited = True

    pass
