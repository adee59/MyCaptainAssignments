# methods of strings :

#

n = "python Is FUN!"

x = n.capitalize()

print (x)

#

a = "This Is Case Fold!!"

x = a.casefold()

print(x)

#

n = "this is center"

x = n.center(20)

print(x)

#

n = "this is count, it'll count counts!"

x = n.count("count")

print(x)

#

a = "My name is StalË"

x = a.encode()

print(x)

#

n = "this is @endswith!"

x = n.endswith("!")

print(x)

#

n = "E\tx\tp\ta\tn\td\ti\tt"

x =  n.expandtabs(3)

print(x)


#

n = "tell us what you need to find!!"

x = n.find("to")

print(x)


#

a = "For only {price:.1f} dollars!"
print(a.format(price = 49))

#format_map() not opening

#

txt = "I'm using index!"

x = txt.index("index")

print(x)

#

txt = "Company12"

x = txt.isalnum()

print(x)

#

txt = "CompanyX"

x = txt.isalpha()

print(x)


#

txt = "Company123"

x = txt.isascii()

print(x)

#

txt = "\u0033"

x = txt.isdecimal()

print(x)

#

txt = "5647830"

x = txt.isdigit()

print(x)

#

txt = "Demo_09"

x = txt.isidentifier()

print(x)

#

txt = "hello bro!!"

x = txt.islower()

print(x)

#

txt = "4736289"

x = txt.isnumeric()

print(x)

#

txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)

#

txt = "   "

x = txt.isspace()

print(x)

#

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)

#

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

#

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

#

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

#

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

#

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

#

txt = "Hello Sam!"

mytable = txt.maketrans("S", "P")

print(txt.translate(mytable))

#

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

#

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

#

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

#

txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

#

txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

#

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

#

txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

#

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

#

txt = "Bello, nelcome po ty morld."

x = txt.startswith("Bello")

print(x)

#

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

#

txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

#

txt = "Welcome to my world"

x = txt.title()

print(x)

#
# 83,80 are ascii values
mydict = {83:  80}

txt = "Hello Sam!"

print(txt.translate(mydict))

#

txt = "Hello my friends"

x = txt.upper()

print(x)

#

txt = "50"

x = txt.zfill(20)

print(x)



