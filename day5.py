# participants = ("ram", "hari", "sita")

# participants.append("amin")

# print(type(participants))
# order status -> received/ 
# packed/ in-transit/ 
# reached-destination/ delivered

# ORDER_STATUS_CHOICES = (
#     "received",
#     "packed",
#     "etc"
# )

# capital letters are used in constant variables
# small letters are used in dynamic variables

# set data structure
# set is the collection of well defined objects
# example is , set of the students of class 8
# example 2: ram_hobbies = {"singing", "dancing", "fishing", "cycling"}

# ram_hobbies = {"singing", "dancing", "fishing", "cycling"}
# hari_hobbies = {"dancing", "biking", "swimming", "singing"}

# print(ram_hobbies)
# print(hari_hobbies)


# stores only unique items or data
#disadvantage of set: 
# not follows the order that user has put the data
# symbol used for intersection is & ampersand
# word used for intersection is common

# common = ram_hobbies & hari_hobbies
# common = ram_hobbies.intersection(hari_hobbies)

# print (common)

# # union is pipe symbol and union
# union = ram_hobbies | hari_hobbies
# union = ram_hobbies.union(hari_hobbies)
# print (union)



# ram_hobbies = {"singing", "dancing", "fishing", "cycling"}
# hari_hobbies = {"dancing", "biking", "swimming", "singing"}

# #only wala set

# ram_only = ram_hobbies.difference(hari_hobbies)

# hari_only = hari_hobbies.difference(ram_hobbies)
# hari_only = hari_hobbies - ram_hobbies
# print(ram_only)
# print(hari_only)

# class_8 = {"vedetar", "tinjure", "pokhara"}
# class_9 = {"shree antu", "damauli", "abc", "pokhara"}
# class_10 = {"Chitwan", "rara", "api", "pokhara"}
# common = class_8 & class_9 & class_10
# print(common)

####################

# DICTIONARY
# data is stored in key value pairs
# data has its respective value

# oxford_dict = {
#     "abc" : "this is abc meaning",
#     "bcd" : "this is binary coded decimals",
#     "oct" : "this is short octal number system"
# }

# print (oxford_dict["abc"])
# user_input = input("Keyword : ")

# if user_input in oxford_dict.keys():
#     print (user_input)
# elif ():
#     print("sorry the key is not found")

# print ("the program completed successfully")


# products = [
#     {
#         "name": "Mobile Phone",
#         "price": 34000,
#         "ram": 12,
#         "rom": 256,
#         "battery_capacity": "10000 mAh"
#     }
# ]


# how to use dictionary in cache
# if  some data is committed in 10 seconds, 
# and again another user commits the same data , what will be the time taken?
# if same operation is asked to be done to the server, the output is stored in some location, that is fetched when same operation is done

# cache = {
#     "qn1": 29,
#     "qn2": 50,
#     "qn3": 90
# }


# while True:
#     user_input = input("which question? : ")
#     print (" starting calculation")
#     answer = cache[user_input] 
#     # answer = 90

#     print(answer)

# dict_ex = {
#     1: "one",
#     2: "two",
#     3: "three"
# }

#example to store user details

# ex = {
#     "name": {
#         "first_name": "amin",
#         "last_name": "nepali"
#     },
#     "address": {
#         "temporary": "biratchowk",
#         "permanent": "dangihat",
#         "state": "koshi"
#     },
#     "education": [
#         {
#             "level": "SEE",
#             "core_subject": ["math", "science"],
#             "institution": {
#                 "name": "XYZ School",
#                 "board": "NEB"
#             }
#         }
#     ]

# }

# print(ex["education"])


#mutable : changable : lists, arrays, dictionaries
#immutable : unchangable :::: tuples

dict_ex = {
    1: "one",
    2: "two",
    3: "three"
}

dict_ex.pop(1)
dict_ex.popitem(2)



