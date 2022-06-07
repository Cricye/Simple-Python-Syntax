class Students():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print(self):
        print(self.name, self.score)

s1 = Students('Curry', 90)
s1.print()



class Students():
    count = 1
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Students.count += 1

    def print(self):
        print(self.name, self.score)

print(Students.count)
s1 = Students('Curry', 93)
s1.print()
print(Students.count)
s2 = Students('James', 92)
s2.print()