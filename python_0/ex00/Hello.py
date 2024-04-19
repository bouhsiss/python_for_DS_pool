ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}



def greet(data):
    if (isinstance(data, list)):
        data[1] = "World!"
    elif (isinstance(data, tuple)):
        del data
        data = ("Hello", "Morocco!")
    elif (isinstance(data, set)):
        data.remove("tutu!")
        data.add("Benguerir!")
    elif (isinstance(data, dict)):
        data["Hello"] = "1337!"
    
    return data

ft_list = greet(ft_list)
ft_tuple = greet(ft_tuple)
ft_set = greet(ft_set)
ft_dict = greet(ft_dict)


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

