# Dictionaries: We use it to store information that comes as key value pairs.
#               It's same as object in JavaScript.
person = {
    "name": "Daeh Rhetica",
    "age": 17,
    "is_verified": True
}
print(person["name"]) # This is how to access a specific key in the dictionary.
# If we don't use get, it would display error because there ain't that key in the dictionary.
print(person.get("birthdate"))
# Instead let it display 'None', we can supply the default value.
# But only when there's ain't that key, if the key is there, it will not supply.
print(person.get("birthdate", "Mar 30 2007"))
# We can also update the value or add a new key.
person["birthdate"] = "Mar 30 2007"
person["name"] = "Dha Reca"
print(f"Name: {person["name"]}\nBirthdate: {person["birthdate"]}")