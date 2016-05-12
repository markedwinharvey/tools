#!/usr/bin/env python
'''
Standard Queue (FIFO) implemented as python object, using a dictionary/hash to track 
element order. Instantiation takes name as only argument. New data is added to self.data 
dictionary through 'push' function. Items are removed through 'pull' function; hash
is automatically updated. 
'''
class queue(object):

	def __init__(self,name):						#initialize empty queue
		self.name=name
		self.data = {}
		self.last_el = -1
		self.first_el=0
		
	def push(self,data):							#add new data
		self.last_el+=1
		self.data[self.last_el]=data
		
	def pull(self):
		if self.data:
			pulled_el = self.data[self.first_el]	#remove and return first element
			del self.data[self.first_el]
			self.first_el+=1
			return pulled_el
		return 'Queue is empty'
	
	def peek(self):									#return top of queue
		if self.data:
			return self.data[first_el]
		return 'Queue is empty'			
	
	def is_empty(self):								#check if queue is empty
		if self.data:
			return False
		return True			

def main():
	pass
if __name__ == '__main__':
	main()