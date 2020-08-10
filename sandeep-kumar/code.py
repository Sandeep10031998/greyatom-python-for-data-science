# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class=class_1+class_2
print(new_class)

# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)



# Create the Dictionary
courses={('Math'):65,('English'):70,('History'):80,('French'):70,('Science'):60}
print(courses)
# Slice the dict and stores  the all subjects marks in variable
values=courses.values()
# Store the all the subject in one variable `Total`
total=sum(values)
# Print the total
print(total,'out of 100')
# Insert percentage formula
percentage=(total*100)/500
# Print the percentage
print(percentage)



# Create the Dictionary
mathematics={('Geoffrey Hinton'):78,('Andrew Ng'):95,('Sebastian Raschka'):65,('Yoshua Bengio'):50,('Hilary Mason'):70,('Corinna Cortes'):66,('Peter Warden'):75}
print(mathematics)
topper=max(mathematics,key=mathematics.get)
print(topper)



# Given string
topper="Andrew Ng"



# Create variable first_name 
first_name="Andrew"

# Create variable Last_name and store last two element in the list
Last_name="Ng"
# Concatenate the string
full_name=('Ng'+' '+'Andrew')

# print the full_name
print(full_name)
# print the name in upper case
certificate_name=full_name.upper()
print(certificate_name)

# Code ends here


