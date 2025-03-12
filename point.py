import random
class Point:
    def __init__(self,x,y): #a function in a class, is a method: link to the object
        #self can be anything
        """
        Initialize point object
        :param x: x axis
        :param y: y axis
        """
        self.x = x # define x attribute via self.x and assign value x to it
        self.y = y # define x attribute via self.x and assign value x to it
    def __str__(self):
        """

        :param self:
        :return:
        """
        return f"p({self.x}, {self.y})"
    def __repr__(self):
        return self.__str__() # use the same awy of printing as str

    def distance_orig(self):
        return (self.x**2 + self.y**2)**0.5 # square root of the sum of x square + y squared

    def __gt__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance
    def




#now we instantiate it! // this means creating a particular version of a said object
p = Point(1,2)
p2 = Point(2,3 )
p4 = Point(4.4, -55)

#now we need to instantiate it!
p = Point(1,2) # p is an instance of 1 and 2

print(f"p.x = {p.x} and p.y = {p.y}") # .x retrives the x point/coordinate
print(f"p4.x = {p4.x} and p4.y = {p4.y}")
p.x = 20
print(f"p.x={p.x} and {p.y}")
#create a list of 5 rnadom points
points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10), # x value
                        random.randint(-10,10))) # y value
print("I go these 5 random points:")
p = Points(3,4)
print(p.distance_orig())
p2 = Point(1,2)
print(f"I am comparing p > p2: {p>p2}")
print("the sorted list of points is:")
points.sort()
print(points)

