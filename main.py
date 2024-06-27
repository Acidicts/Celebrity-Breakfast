import random

celebrities = []
with open("celebrities.txt", "r") as file:
    for line in file:
        celebrities.append(line.strip())

def main():
    choice = input("How many Ingredients do you want to use? \n")

    if int(choice) <= 0:
        print("Please enter a number greater than 0")
        main()

    recipe = []

    for item in range(int(choice)):
        if not celebrities:  # Check if the list is empty
            print("No more celebrities left.")
            break
        option = random.choice(celebrities)
        print(option)
        recipe.append(option)
        celebrities.remove(option)

    print("\n\n\n\n\n\n\n")
    temp= ""
    for item in recipe:
        temp = temp + item + ", "
    print("Your recipe is: " + temp[:-2])




if __name__ == '__main__':
    main()
