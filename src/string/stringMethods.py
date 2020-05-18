string = "Hello World"

# HelloWorld
print("isalpha() -", string.isalpha())  # False

# hello world
print("islower() -", string.islower())  # False

# HELLO WORLD
print("isupper() -", string.isupper())  # False

# 123
print("isdigit() -", string.isdigit())  # False

# 123
print("isnumeric() -", string.isnumeric())  # False

# Hello
print("startswith(str) -", string.startswith("Hello"))  # True

# World
print("endswith(str) -", string.endswith("World"))  # False

# Hello World
print("lower() -", string.lower())  # hello world

# Hello World
print("upper() -", string.upper())  # HELLO WORLD

# hello world
print("title() -", string.title())  # Hello World

# hello World
print("capitalize() -", string.capitalize())  # Hello world

# "  Hello World"
print("lstrip() -", string.lstrip())  # Hello World

# "Hello World  "
print("rstrip() -", string.rstrip())  # Hello World

# "  Hello World  "
print("strip() -", string.strip())  # Hello World

# Hello World
print("ljust(width) -", string.ljust(13))  # "Hello World  "

# Hello World
print("rjust(width) -", string.rjust(13))  # "  Hello World"

# Hello World
print("center(width) -", string.center(15))  # "  Hello World  "

# Hello World
print("find(str) -", string.find("W"))  # 6

# Hello World
print("find(str, start) -", string.find("o", 5))  # 7

# Hello World
print("find(str, start, end) -", string.find("o", 0, 5))  # 4

# Hello World
print("replace(old, new) -", string.replace(" ", "_"))  # Hello_World

# Hello World
print("replace(old, new, num) -", string.replace("", "_", 5))  # _H_e_l_l_o World

# Hello, World
print("split() -", string.split())  # ['Hello', 'World']

# Hello World
print("split(delimeter) -", string.split("o"))  # ['Hell', ' W', 'rld']

# Hello World
print("split(delimeter, num) -", string.split("l", 1))  # ['He', 'lo World']

# Hello World
print("join(strs) -", ",".join(string))  # H,e,l,l,o, ,W,o,r,l,d
