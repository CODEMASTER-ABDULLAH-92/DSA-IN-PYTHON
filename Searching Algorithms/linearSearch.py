# -------------------------
# Methode 1
# -------------------------

# my_list = [23,54,44,32,65]
# def linearSearch(target):
#     for i in my_list:
#         if(i == target):
#             print(f"Elment is present on {i}")
#             return
#     print("Element is not present")

# linearSearch(32)


# for index, value in enumerate(my_list):
#     print(index, value)

# -------------------------
# Methode 2
# -------------------------


my_list = [23,54,44,32,65]
def linearSearch(target):
    for idx, value in enumerate(my_list):
        if(value == target):
            print(f"Elment is present on {idx}")
            return
    print("Element is not present")

linearSearch(32)


# -------------------------
# Methode 3
# -------------------------


my_list = [23,54,44,32,65]
def linearSearch(target):
    for i in range(len(my_list)):
        if(target == my_list[i]):  
            print(i, my_list[i])
            return
    print("Element is not present")
    
linearSearch(32)
