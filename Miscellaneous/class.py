class animal:

  def __init__(self):
    self.x = 0

  def setting_value(self):
    self.x = (self.x) + 1
    print("So far:", self.x)


an = animal()

i = 0
for i in range(3):
  an.setting_value()

