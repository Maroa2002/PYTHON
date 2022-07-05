try:
    file = open("file.txt")
    dictionary = {"Key": "Value"}
    print(dictionary["Key"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
