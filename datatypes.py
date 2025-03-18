#data types specify the type of data that can be stored inside a variable
num = 24 #integer
print(num)

#Numeric: int, float, complex (Holds numeric values)
#int - holds signed integers of non-limited length
#float - holds floating decimal points and it's accurate up to 15 decimal places
# use the type() function to know which class a variable or a value belongs to.
num1 = 55
num2 = 5.3
print(num1)
print(num2)
print(type(num1))


#String: str(Holds sequence of characters)
#(sequence of characters represented by either single or double quotes. For example,)
sites_name = 'power learn project'
print(sites_name)

#sequence: list, tuple ,range(Holds collection of items)
#(A list is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ].)
languages = ['python', 'dart', 'web', 23]
print(languages)

#Access list items
#(To access items from a list, we use the index number (0, 1, 2 ...))
print(languages[1])
print(languages[0])
print(languages[2])
print(languages[3])

#Tuple data type
#(A tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.)
products = ('xbox', 499.99, 'Habibi', 23)
print(products)

#Access tuple items
#(Similar to lists, we use the index number to access tuple items in Python.)
print(products[2])

#mapping: dict(Holds data in key-value pair form)
#(ordered collection of items. It stores elements in key/value pairs.)
capital_city = {"Kenya": "Nairobi", "Nigeria": "Lagos"}
print(capital_city)

#boolean: bool(Holds either True or False)
#set: set(Holds collection of unique items)
#(Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }.)
student_ids = {112, 114, 117, 113}
print(student_ids)