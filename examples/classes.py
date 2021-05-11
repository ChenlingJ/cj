class Bicycle:
    def __init__(self, owner):  # __init__ and __new__ methods are constructors
        # A "constructor" is a method defining the code that should run to set up a new instance of a class.
        # In Python, define the `__init__` (or `__new__`, rarely) method to customize what happens when
        #     an instance is created.
        # Constructors are responsible for assigning data to new instances of an object.
        # `self` is a newly-allocated, uninitialized instance of `Bicycle`.
        self.owner = owner
        # `owner` is an "attribute", stored on instances of `Bicycle`.

        self.current_gear = 1  # Every instance of `Bicycle` starts out in 1st gear.

    def __str__(self):
        # The magic method `__str__` defines how the `str` function behaves with instances of `Bicycle`.
        # Instead of printing "<__main__.Bicycle object at SOMEADDRESS>" it will be "A bicycle owned by NAME."
        return "A bicycle owned by {}.".format(self.owner)

    def _current_gear_str(self):
        if self.current_gear % 10 == 1 and self.current_gear != 11:
            suffix = "st"
        elif self.current_gear % 10 == 2 and self.current_gear != 12:
            suffix = "nd"
        elif self.current_gear % 10 == 3 and self.current_gear != 13:
            suffix = "rd"
        else:
            suffix = "th"
        return "{}{}".format(self.current_gear, suffix)

    def move_forward(self):
        print("{} is bicycling forward in {} gear!".format(self.owner, self._current_gear_str()))

    def move(self, direction):
        print("{} is bicycling {} in {} gear!".format(self.owner, direction, self._current_gear_str()))

    def change_gears(self, new_gear):
        # `new_gear` is a parameter of the `change_gears` method.
        # `owner` and `current_gear` are attributes of `self`, an instance of `Bicycle`.
        print("{} is switching gears from {} to {}.".format(self.owner, self.current_gear, new_gear))
        self.current_gear = new_gear

    def compare_gears(self, other_bike):
        # The `other_bike` parameter is a (different?) instance of the `Bicycle` class.
        if self.current_gear < other_bike.current_gear:
            comparison = "a lower gear than"
        elif self.current_gear > other_bike.current_gear:
            comparison = "a higher gear than"
        else:
            comparison = "the same gear as"
        print("{}'s bike is in {} {}'s bike.".format(self.owner, comparison, other_bike.owner))


class FooClass:
    pass


if __name__ == "__main__":
    mikes_bike = Bicycle("Mike")  # Call the constructor of `Bicycle`.
    # `Bicycle` is a "class".
    # `mikes_bike` is an "object".
    # `mikes_bike` is an "instance of Bicycle".
    print(mikes_bike)  # Print the value of `str(mikes_bike)`.
    mikes_bike.move_forward()
    # `b.move_forward` is a "method" of `mikes_bike`, from the Bicycle class.
    # `self` is `mikes_bike`.
    mikes_bike.move("backward")
    # `"backward"` is an "argument" to the `move` method.
    # Arguments are sometimes known as parameters.
    # Inside the `move` method, `self` refers to `mikes_bike`.

    chenlings_bike = Bicycle("Chenling")
    # `chenlings_bike` is an instance of `Bicycle`.
    print(chenlings_bike)
    chenlings_bike.compare_gears(mikes_bike)
    chenlings_bike.move("upward")
    chenlings_bike.change_gears(9)
    chenlings_bike.move("sideways")
    chenlings_bike.compare_gears(mikes_bike)
    mikes_bike.compare_gears(chenlings_bike)
    mikes_bike.compare_gears(mikes_bike)
    # `self` will refer to `chenlings_bike`.

    foo = FooClass()  # `foo` is an instance of `FooClass`.
    foo.owner = "Not a real bike"
    foo.current_gear = 2
    mikes_bike.compare_gears(foo)

    mikes_bike.current_gear = 3
    mikes_bike.move("everywhere")
