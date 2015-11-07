######################  Class_Practise   #####################
class Things:
	pass

class Inanimate(Things):
	pass
	
class Animate(Things):
	pass
	
class Sidewalks(Inanimate):
	pass
	
class Aniamals(Animate):
	def breathe(self):
		print ("breathing")
	def move(self):
		print ("moving")
	def eat_food(self):
		print ("eating food")
	
class Mammals(Aniamals):
	def feed_young_with_milk(self):
		print ("feeding young")
		
class Giraffes(Mammals):
	def __init__(self,spots):
		self.giraffe_spots = spots
	def find_food(self):
		self.move()
		print ("I've found food!")
		self.eat_food()
	def eat_leaves_from_trees(self):
		self.eat_food()
	def dance_a_jig(self):
		self.move()
		self.move()
		self.move()

ozward = Giraffes(100)
gertrude = Giraffes(150)
print ozward.giraffe_spots
print gertrude.giraffe_spots
		
reginald = Giraffes(888)
reginald.move()
reginald.breathe()
reginald.feed_young_with_milk()
reginald.find_food()
reginald.dance_a_jig()

harold = Giraffes(99)
harold.move()


#######################  Turtle_Move   ###########################
import turtle
avery = turtle.Pen()
kate = turtle.Pen()

avery.forward(50)
avery.right(90)
avery.forward(20)

kate.left(90)
kate.forward(100)

jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)


####################   键盘输入值   ########################
year = input('Year of birth: ')
if not bool(year.rstrip())  #用户没有输入时执行
	print("you need to enter a value for your year of birth")

#键盘输入值的另一种方法
import sys
print (sys.stdin.readline())