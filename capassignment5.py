# changing a value in a tuple :

x = ("bello", "nelcome", "po")
y = list(x)
y[2] = "ty"
x = tuple(y)

print(x)

# dictonary methods :

#
std =	{
  "tre": "hgf",
  "mnb": "vcx",
  "yui": 43567
}

std.clear()

print(std)

#
std =	{
  "tre": "hgf",
  "mnb": "vcx",
  "yui": 43567
}

std.copy()

print(std)

#
x = ('key1', 'key2', 'key3')
y = 9

thisdict = dict.fromkeys(x, y)


print(thisdict)


#
std =	{
  "tre": "hgf",
  "mnb": "vcx",
  "yui": 43567
}

a=std.get("yui")

print(a)

#
std =	{
  "tre": "hgf",
  "mnb": "vcx",
  "yui": 43567
}

x = std.items()

print(x)

#
std =	{
  "tre": "hgf",
  "mnb": "vcx",
  "yui": 43567
}

x = std.keys()

print(x)

#
std =	{
  "tre": "hgf",
  "mnb": "vcx",
  "yui": 43567
}

std.pop("yui")

print(std)

#
std =	{
  "tre": "hgf",
  "mnb": "vcx",
  "yui": 43567
}

std.popitem()

print(std)

#
# setdefault?

#
std =	{
  "tre": "hgf",
  "mnb": "vcx",
  "yui": 43567
}

std.update({"ewq":"fds"})

print(std)

#
std =	{
  "tre": "hgf",
  "mnb": "vcx",
  "yui": 43567
}

x = std.values()

print(x)



# dict. with no. as key, list & dict. as values :
l1=["adf","vcx","nbv"]
d1={
    "ytr": "iuy",
    "bgt": "mju"
} 
std =	{
  "1": l1,
  "mnb": "vcx",
  "yui": d1
}

print(std)



