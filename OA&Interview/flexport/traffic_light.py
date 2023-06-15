class Light:
  def __init__(self,x,y,is_green=True):
    self.x = x
    self.y = y
    self.is_green = is_green
    
class Road:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  @property
  def is_vertical(self):
    return self.y == None

class Car:
  def __init__(self,x,y,direction): # 0 => increasing y, 1 => increasing x, 2 => decreasing y, 3 => decreasing x
    self.x = x
    self.y = y
    self.direction = direction

class Map:
  def __init__(self,roads,limits_min,limits_max):
    self.lights = []
    for r1 in roads:
      for r2 in roads:
        if r1.is_vertical and not r2.is_vertical:
          self.lights.append(Light(r1.x,r2.y))
    self.roads = roads
    self.city_limits_min = limits_min
    self.city_limits_max = limits_max
  
  def simulation(self,car):
    total_time = 0
    while self.city_limits_min[0] <= car.x <= self.city_limits_max[0] and self.city_limits_min[1] <= car.y < self.city_limits_max[1]:
      total_time += 1
      if not any((light.x, light.y) == (car.x, car.y) and not light.is_green for light in self.lights):
        if car.direction == 0: car.y += 1
        if car.direction == 1: car.x += 1
        if car.direction == 2: car.y -= 1
        if car.direction == 3: car.x -= 1
      for light in self.lights:
        light.is_green = not light.is_green
    return total_time

J = Road(1, None)
A = Road(None, 1)
B = Road(None, 2)

m = Map([J, A, B], (0, 0), (2, 3))
assert m.simulation(Car(1, 0, 0)) == 5