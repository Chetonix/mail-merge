with open("./Input/names.txt", "r") as data:
    names_list = data.readlines()

print(names_list)

for name in names_list:
    stripped_name = name.strip()
    print(stripped_name)
    with open("./Input/example_output.txt", "r") as letter_contents:
        contents = letter_contents.read()
    output = contents.replace("[name]", stripped_name)
    with open(f"./Output/{stripped_name}.txt", "w") as letter:
        letter.write(output)