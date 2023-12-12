def calculate_distance(gamt):
	
	distance = gamt * 10
	if gamt == 40:
		return "Your tank is full and your car can go " + str(distance) + "km"
	if gamt >= 25 and gamt < 39:
		return "Your tank is 3/4 full and your car can go " + str(distance) + "km"
	if gamt >= 15 and gamt < 25:
		return "Your tank is 2/4 full and your car can go " + str(distance) + "km"
	if gamt >= 5 and gamt < 15:
		return "Your tank is 1/4 full and your car can go " + str(distance) + "km"
	else:
		return "Your tank is empty and your car can go " + str(distance) + "km"
	
gamt = int(input("How much gas do you have left (In litres): "))
		
print(calculate_distance(gamt))