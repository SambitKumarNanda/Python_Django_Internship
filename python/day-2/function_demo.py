def message(name, age, university):
    return f"my name is {name}, age {age} , I'm studying at {university}"


data = {
    "name": "Sambit",
    "age": 21,
    "university": "Silicon"
}

# Similar to spread operator in Js
print(message(**data))
