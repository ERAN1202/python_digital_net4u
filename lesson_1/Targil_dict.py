#dictionary

my_dict = {"www.google.com": "8.8.8.8", "www.facebook.com": "4.4.4.4", "www.youtube.com":["1.1.1.1","5.5.5.5"]}
my_dict.update({"www.walla.com": "1.2.3.4"})
print(my_dict)
print("Numbers of entries: " + str(len(my_dict)))
print(my_dict["www.google.com"])
print(my_dict.values())
my_dict["www.google.com"] = "8.8.8.4"
print(my_dict["www.google.com"])
print(my_dict)
