print ("Please input the amount of fruits you have collected (in kilograms): ")
print ("---------------------------------------------------------------------")
orange_quantity_kg = input("Orange: ")
strawberry_quantity_kg = input("Strawberry: ")
cherry_quantity_kg = input("Cherry: ")
apricot_quantity_kg = input("Apricot: ")

orange_jars = int((int(orange_quantity_kg) * 1000) / 500)
strawberry_jars = int((int(strawberry_quantity_kg) * 1000) / 750)
cherry_jars = int((int(cherry_quantity_kg) * 1000) / 1000)
apricot_jars = int((int(apricot_quantity_kg) * 1000) / 600)

total_jars = orange_jars + strawberry_jars + cherry_jars + apricot_jars
revenue = total_jars * 20
print ("---------------------------------------------------------------------")
print ("Orange jars: " + str(orange_jars))
print ("Strawberry jars: " + str(strawberry_jars))
print ("Cherry jars: " + str(cherry_jars))
print ("Apricot jars: " + str(apricot_jars))
print ("---------------------------------------------------------------------")
print ("Total jars: " + str(total_jars))
print ("Revenue: " + str(revenue) + " AED")
