import tkinter as tk

def main():
    #creates empty array
    input_list = []

    root = tk.Tk()
    
    #Function to add user input to the array
    def add_input():
        user_input = input_box.get()
        print("User Input: ", user_input)
        input_list.append(user_input)
        print(("Input list: ", input_list))
        
        input_box.delete(0,tk.END)      #Clears input box

    # create tkinter input box and button
    input_box = tk.Entry(root)
    input_box.pack()

    add_button = tk.Button(root, text="Add", command=add_input)
    add_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()