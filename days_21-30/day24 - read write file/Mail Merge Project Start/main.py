# create name list
with open("Input/Names/invited_names.txt", 'r') as names_file:
    names = [name.strip() for name in names_file.readlines()]

# prepare list template
with open("Input/Letters/starting_letter.txt", 'r') as letter_file:
    letter_contents = letter_file.read()

# write personalized lists and safe in Output directory
for name in names:
    new_letter_contents = letter_contents.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}", 'w') as new_letter_file:
        new_letter_file.write(new_letter_contents)
