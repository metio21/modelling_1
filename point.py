import random

class Point:
    def __init__(self, x, y):
        """
        Initialize a Point object.
        :param x: the x position on the axis
        :param y: the y position on the axis
        self invisibly accesses the object getting addressed or changed
        """
        self.x = x # define x attribute via self.x and assign the value x to it
        self.y = y

    def __str__(self):
        """
        Magic method that is called when we try to print an instance
        :return: <x, y>
        makes it readable
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        return self.__str__() #used the same way of printing as str

    def distance_orig(self):
        """
        :return: distance from origin (0,0)
        """
        return (self.x**2 + self.y**2)**0.5 #square root of the sum of x and y squared


    def __gt__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance
    #magic method used for comparisons; in this case to compare the distance between two points
    #allows for comparison based on meaningful criteria

    def __eq__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance
    #magic method to see if distances are equal

if __name__ == "__main__": #this separates the functions that can be exported from the test code below
    # now we need to instantiate it!
    p = Point(1, 2) # p is an instance of 1 and 2
    print(f"p.x={p.x} and p.y={p.y}")
    p.x = 20
    print(f"p.x={p.x} and p.y={p.y}")
    print(p)
    # create a list of 5 random points
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10, 10), # x value
                            random.randint(-10, 10))) # y value
    print("I got these 5 random points:")
    print(points)
    p = Point(3, 4)
    print(p.distance_orig()) # expect 5 as answer
    p2 = Point(1, 1)
    print(f"I am comparing p > p2: {p>p2}") # I expect to have True
    print("the sorted list of points is:")
    points.sort()
    #sorts points in order of distance from origin  
    print(points)