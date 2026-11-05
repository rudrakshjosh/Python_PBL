#=============================================================================================================
# This module contains the rooms categories and the allocation and addition of rooms to the management system
#=============================================================================================================
class Room:
	def __init__(self,a,b,c):
		self.room_id=(a,b)
		self.capacity=c		
class Standard_Room(Room):
	def __init__(self,a,b,c):
		super().__init__(a,b,c=2)
	def calculate_rent(self):
		return 8000
class Deluxe_Room(Room):
	def __init__(self,a,b,c):
		super().__init__(a,b,c=1)
	def calculate_rent(self):
		return 12000	
class Shared_Dormitory(Room):
	def __init__(self,a,b,c):
		super().__init__(a,b,c=6)
	def calculate_rent(self):
		return 5000
class Management(Room):
	def __init__(self):
		self.rooms={}
		self.booked_rooms=[]
	def add_room(self,room):
		self.rooms.add(room)
	def book_room(self,room_id):
		if room_id in self.rooms:
			self.booked_rooms.append(room_id)
			del self.rooms[room_id]
			return True
		else:
			return False
	def cancel_booking(self,room_id):
		if room_id in self.booked_rooms:
			self.booked_rooms.remove(room_id)
			return True
		else:
			return False
	def calculate_total_rent(self):
		total_rent=0
		for room in self.booked_rooms:
			total_rent+=room.calculate_rent()
		return total_rent
#====================================================
#module 2
#====================================================