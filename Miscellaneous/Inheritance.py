class animal:

  def __init__(self, name):
    self.x = 0
    self.name = name

  def party(self):
    print('Partying here:', self.name)
    self.x = (self.x) + 1
    print("So far:", self.x)


class subClass(animal):

  def __init__(self, name):
    super().__init__(name)
    self.points = 0

  def point(self):
    self.points = self.points + 7
    self.party()
    print(self.name, self.points)


s = animal('Jeff')

print(s.party())

j = subClass('Jack')
j.party()
j.point()
