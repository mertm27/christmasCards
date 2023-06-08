import os

template_file = 'template.txt'
names_file = 'names.txt'
output_directory = 'christmasCards'
with open(template_file, 'r') as file:
    template = file.read()
with open(names_file, 'r') as file:
    names = file.read().splitlines()
os.makedirs(output_directory, exist_ok=True)
for name in names:
    card_message = template.replace("NAME", name)
    output_file = os.path.join(output_directory, f"{name}_card.txt")

    with open(output_file, 'w') as file:
        file.write(card_message)
print(f"{len(names)} cards generated and saved in the {output_directory} directory.")