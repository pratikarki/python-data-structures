class Cookie:
  def __init__(self, color):
    self.color = color

  def get_color(self):
    return self.color
  
  def set_color(self, color):
    self.color = color


cookie_1 = Cookie('Red')
print(cookie_1.get_color())

cookie_1.set_color('Pink')
print(cookie_1.get_color())
