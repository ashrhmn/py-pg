from pickle import TRUE
import numpy as np

from func import addition

arr = np.zeros(4)
print(arr)

# dic = {
#     "a": 1,
#     "b": 2
# }

# # print(dic)

# users = {
#     "ashrhmn": {
#         "name": "Ashik Rahman",
#         "age": 20,
#         "website": "ashrhmn.com"
#     },
#     "hasanJahidul": {
#         "name": "Jahidul Hasan Joy",
#         "age": 24,
#         "website": "hasanjahidul.com"
#     }
# }

# # print(users.items())

# for key, value in users.items():
#     print(key, " : ")
#     for key2, value2 in value.items():
#         print(key2.capitalize(), value2)


# words = []

# while TRUE:
#     inp = input("Word : ")
#     if inp == "exit":
#         break
#     words.append(inp)

# query = input("Search for : ")

# if query in words:
#     print(query, " found")
# else:
#     print(query, " not found")


print(addition(1, 2))
