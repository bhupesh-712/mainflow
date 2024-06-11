def manage_list():
    my_list = []
    while True:
        print("\nCurrent List:", my_list)
        print("1. Add an element")
        print("2. Remove an element")
        print("3. Modify an element")
        print("4. Exit list management")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            element = input("Enter the element to add: ")
            my_list.append(element)
        elif choice == '2':
            element = input("Enter the element to remove: ")
            if element in my_list:
                my_list.remove(element)
            else:
                print("Element not found in the list.")
        elif choice == '3':
            index = int(input("Enter the index of the element to modify: "))
            if 0 <= index < len(my_list):
                new_value = input("Enter the new value: ")
                my_list[index] = new_value
            else:
                print("Invalid index.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def manage_dict():
    my_dict = {}
    while True:
        print("\nCurrent Dictionary:", my_dict)
        print("1. Add a key-value pair")
        print("2. Remove a key-value pair")
        print("3. Modify a value")
        print("4. Exit dictionary management")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            my_dict[key] = value
        elif choice == '2':
            key = input("Enter the key to remove: ")
            if key in my_dict:
                del my_dict[key]
            else:
                print("Key not found in the dictionary.")
        elif choice == '3':
            key = input("Enter the key to modify: ")
            if key in my_dict:
                new_value = input("Enter the new value: ")
                my_dict[key] = new_value
            else:
                print("Key not found in the dictionary.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def manage_set():
    my_set = set()
    while True:
        print("\nCurrent Set:", my_set)
        print("1. Add an element")
        print("2. Remove an element")
        print("3. Exit set management")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            element = input("Enter the element to add: ")
            my_set.add(element)
        elif choice == '2':
            element = input("Enter the element to remove: ")
            if element in my_set:
                my_set.remove(element)
            else:
                print("Element not found in the set.")
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

def main():
    while True:
        print("\nChoose the data structure to manage:")
        print("1. List")
        print("2. Dictionary")
        print("3. Set")
        print("4. Exit program")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            manage_list()
        elif choice == '2':
            manage_dict()
        elif choice == '3':
            manage_set()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
