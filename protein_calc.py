
print("Hi, there!")
weight = input("So, you're trying to figure out how much protein you should consume to gain muscle mass? Input your weight here:\n")

try:
	rec_protein_intake = float(weight) * .65
except ValueError:
	print("Oops, that doesnt look like a valid weight")
else:	
	print(f"Eat {rec_protein_intake} grams of protein daily to gain muscle mass.")