from sys import exit
from random import randint

class Scene(object):
	def enter():
		print('If class hasn\'t def enter you write this message')
		exit(0)
		
	value = 'WTF IS OOP ON PYTHON'
	
class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	def play(self):
		currnet_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		while currnet_scene != last_scene:
			next_scene_name = currnet_scene.enter()
			currnet_scene = self.scene_map.next_scene(next_scene_name)
		
		currnet_scene.enter()
		
class Death(Scene):
	def enter(self):
		print('Y die')
		exit(0)
		
class Room_1(Scene):
	def enter(self):
		print(self.value)
		print('this is a room_1. If u want continue write Yes if u want die write no')
		choice = input('> ')
		if choice == 'Yes':
			return 'room_2'
		elif choice == "No":
			return 'death'
		else:
			return 'room_1'
				
class Room_2(Scene):
	def enter(self):
		print('This is a room_2. if u want continue say Yes')
		choice = input('> ')
		if choice == 'Yes':
			return 'finished'
		elif choice == "No":
			return 'death'
		else:
			print('Write Yes or write No')
			choice = input('> ')

class Finish(Scene):
	def enter(self):
		print('Y\'re winner')
		exit(0)
			
class Map(object):
	scenes = {
	'room_1' : Room_1(),
	'room_2' : Room_2(),
	'death' : Death(),
	'finished' : Finish()
	}
	def __init__(self, start_scene):
		self.start_scene = start_scene
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	def opening_scene(self):
		return self.next_scene(self.start_scene)

	
a_map = Map('room_1')
a_game = Engine(a_map)
a_game.play()
	
	
	
	
	
	
	
				
				
				
				
				
				
				