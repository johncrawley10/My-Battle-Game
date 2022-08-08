#wizard information
wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150
#elf information
elf = "Elf"
elf_hp = 100
elf_damage = 100
#human information
human = "Human"
human_hp = 150
human_damage = 20
#dragon infomration
dragon = "Dragon"
dragon_hp = 300
dragon_damage = 50
#Orc information
orc = "Orc"
orc_hp = 300
orc_damage = 15

while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    print("4) Orc")
    print("Type 'Exit' if you are a coward")
    user_input = input("Choose your character:").capitalize()
    if user_input == "1" or user_input =="Wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if user_input == "2" or user_input =="Elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if user_input == "3" or user_input =="Human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    if user_input == "4" or user_input =="Orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    if user_input == "Exit":
        print("Coward!")
        exit()
    else: 
        print("Unknown character")

print("You have chosen the character: " + character)
print("Health: " + str(my_hp))
print("Damage: " + str(my_damage))

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now: " + str(dragon_hp))
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at " + character)
    print("The "+ character + "'s hitpoints are now: " + str(my_hp))
    if my_hp <= 0:
        print("The " + character + " has lost the battle")
        break
