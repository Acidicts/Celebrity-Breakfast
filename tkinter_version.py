import tkinter as tk
import random
from tkinter import scrolledtext

# Create the main window
root = tk.Tk()
root.title("Celebrity Recipe Generator")
root.geometry("500x500")


labels = []
buttons = []

celebrities = []
with open("celebrities.txt", "r") as file:
    for line in file:
        celebrities.append(line)

# Basic Functions


def make_button(master, text, command):
    button = tk.Button(master=master, text=text, command=command)
    button.pack()
    buttons.append(button)


def make_label(master, text):
    label = tk.Label(master=master, text=text)
    label.pack()
    labels.append(label)


def clear_screen():
    global buttons, labels
    for i in range(len(buttons)):
        buttons.remove(buttons[i])
    for i in range(len(labels)):
        labels.remove(labels[i])


def get_input(choice, entry):
    entry.destroy()
    clear_screen()
    if int(choice) <= 0:
        make_label(root, "Please enter a number greater than 0")
        make_button(root, "Try Again", lambda: clear_screen())
    else:
        recipe = []
        for item in range(int(choice)):
            if not celebrities:  # Check if the list is empty
                make_label(root, "No more celebrities left.")
                break
            option = random.choice(celebrities)
            recipe.append(option)
            celebrities.remove(option)
        clear_screen()

        st = scrolledtext.ScrolledText(root, width=50, height=10)

        for item in recipe:
            st.insert(tk.END, item)

        st.pack()

        for celeb in recipe:
            st.insert(tk.END, celeb)

        make_button(root, "Try Again", lambda: main())


def main():
    make_label(root, "How many Ingredients do you want to use? \n")
    entry = (tk.Entry(root, width=10, borderwidth=5))
    entry.pack()
    make_button(root, "Submit", lambda: get_input(entry.get(), entry))

    root.mainloop()


if __name__ == "__main__":
    main()
