class Point:
    def draw(self):
        print("drawing...")
    def move(self):
        print("Moving...")

point1 = Point()
point1.move()
point1.draw()

point1.x = 10
point1.y = 12
print(point1.y)
#print(point1.move())