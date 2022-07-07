# Icons

boat_icon = "\U000026F5"
water_icon = "\U000026AA"
octopus_icon = "\U0001F419"
shoot_boat = "\U0000274C"
shoot_water = "\U0001F300"


# Boats

boat_0 = boat_icon + boat_icon + boat_icon + boat_icon 
boat_1 = boat_icon + boat_icon + boat_icon + boat_icon 
boat_2 = boat_icon + boat_icon + boat_icon + boat_icon 
boat_3 = boat_icon + boat_icon + boat_icon + boat_icon 
boat_4 = boat_icon + boat_icon + boat_icon 
boat_5 = boat_icon + boat_icon + boat_icon 
boat_6 = boat_icon + boat_icon + boat_icon 
boat_7 = boat_icon + boat_icon  
boat_8 = boat_icon + boat_icon  
boat_9 = boat_icon 

available_boats_list = [boat_9, boat_8, boat_7, boat_6, boat_5, boat_4, boat_3, boat_2, boat_1, boat_0]
available_boats_list_user = [boat_9, boat_8, boat_7, boat_6, boat_5, boat_4, boat_3, boat_2, boat_1, boat_0]
available_boats_list_machine = [boat_0, boat_1, boat_2, boat_3, boat_4, boat_5, boat_6, boat_7, boat_8, boat_9]

boat_position_list_user = []
boat_position_list_machine = []

total_boats = len(available_boats_list)


rows = 10
columns = 10
water = " "

starter_shoots = 10
boat_number = 10
chosen_lenght = 0


