# repeated / reusable

# function is doing a particular task
# used to define a task
# reusable
# assign a number or lines of codes to a certain variable

# एुउटा काम हो


# def send_mail():
#     print("check if user email is verified")
#     print("sending mail to ram")
#     print("prepair mail message")
#     print("mail sending")
#     print("mail sent")

# send_mail() # this is function call

# send_mail()


# name = "amin"

# def send_mail(name, status):
#     print(f"the mail is send by {name}, the order status is '{status}'")


# value we pass/ send to the function are called arguments
# arguments based on position are called positional arguments
# same for keyword arguments that keywords are used
# send_mail("hari")


# send_mail("reeta", "on the way")
# send_mail( status = "on the way", name = "reeta")

# --------------------

# def send_mail(  greeting, status, name="amin"):
#     print(f"{greeting}, {name}")
#     print(f"Your order status is ' {status} '")


# send_mail(
#     status="on the way",
#     greeting="good evening"
#     # name="asmita"
#     ) 




# def send_mail(  greeting, status, name="amin"):
#     print(f"{greeting}, {name}")
#     print(f"Your order status is ' {status} '")
#     return("your task has started")


# response = send_mail(
#     status="on the way",
#     greeting="good evening",
#     name="asmita"
# )

# print(response)

# def add(a,b):
#     result = a + b
#     # print ( result)
#     return result


# add_result = add(5,6)

# x = add_result * 5
# print (x)


# now it should return both addition and subtraction

def add_sub(a,b):
    add = a+b
    sub = a-b
    return add, sub

a, s = add_sub (5, 6)


# print (result)
print (a, s )
