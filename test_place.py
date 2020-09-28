"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)

    print(default_place)
    assert default_place.name == "Malagar"
    assert default_place.country == "Spain"
    assert default_place.priority == 1
    assert default_place.is_visited

    # TODO: Write tests to show this initialisation works
    default_place.visit()
    assert default_place.is_visited
    default_place.unvisited()
    assert not default_place.is_visited


    # TODO: Add more tests, as appropriate, for each method


run_tests()
