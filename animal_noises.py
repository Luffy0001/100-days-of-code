animals = ["dog", "cat", "bird", "fish", "cow", "sheep", "horse", "pig", "goat", "chicken"]

exit = ""
while exit != "yes":
	animal_choose = str(input(("What animal do you want? ")))
	for animal in animals:
		if animal_choose == animal:
			if animal_choose == "dog":
				print("Woof Woof")
			elif animal_choose == "cat":
				print("Meow")
			elif animal_choose == "bird":
				print("Tweet Tweet")
			elif animal_choose == "fish":
				print("Bloop Bloop")
			elif animal_choose == "cow":
				print("Moo")
			elif animal_choose == "sheep":
				print("Baaaa")
			elif animal_choose == "horse":
				print("Neigh")
			elif animal_choose == "pig":
				print("Oink Oink")
			elif animal_choose == "goat":
				print("Maaaa")
			elif animal_choose == "chicken":
				print("Cluck Cluck")
			else:
				print("Animal not in inventory")
	exit = str(input("Do you want to exit? "))
		
	