name = input("Type your name: ")
print("Welcome dearest", name, "to this dark and riveting adventure!")

answer = input("You are on a mysterious island. After a shipwreck, you find yourself washed ashore. The sun is setting, and you need to find shelter. To your left, there is a dense forest. To your right, there is a rocky path leading up to an ancient temple. Do you want to go left or right? ").lower()

if answer == "left":
    answer = input("You enter the forest to your left. It's dark and dense. You hear a noise to your left. Do you want to go left or right? ").lower()

    if answer == "left":
        print("You find an injured animal. You help it, and it leads you to a safe spot with fruit trees. Congratulations! You've found a safe place to stay. ")
    elif answer == "right":
        print("You walk deeper into the forest, finding a small stream. As night falls, you feel vulnerable. You survive the night but feel exposed. ")
    else:
        print('Not a valid option. You get eaten by a wild, but extremely beautiful, white tigre.')

elif answer == "right":
    answer = input("You climb the rocky path to the ancient temple. Inside, you see strange carvings. Do you want to go left or right? ")
    
    if answer == "left":
        print("Examine the Carvings. You trigger a hidden door, revealing a secret chamber with supplies.You've found valuable resources for survival! ")
    elif answer == "right":
        answer = input("Search for a Hidden Entrance. You find a hidden entrance leading to an underground chamber with tools. You've gained valuable tools for your adventure. Do you want to use the tools? (Yes/No) ")
    
        if answer == "yes":
            print("You decide to use the ancient tools, but unknowingly, they are cursed. As you work, a series of bizarre and dangerous events unfold, ultimately leading to a fatal accident. GAME OVER: The ancient curse claims another victim. ")
        elif answer == "no":
            print("You decide not to risk it and leave the tools alone. Without the tools, you struggle to survive the cold night and eventually freeze to death. GAME OVER: The harsh conditions of the island prove too much. ")

    else:
        print('Not a valid option. You get eaten by a wild, but extremely beautiful and sophisticated tiger.') 

else:
    print('Not a valid option. You get stung by angry bees.')

print("Thank you for playing", name, "Remember, if at first you don't succeed, try, try again. Or, you know, maybe just avoid cursed islands altogether. They're bad news. Seriously." )