class Set:
    def __init__(s):
        s.d = set()

    def print_set(s):
        print("Set: {", end="")
        for el in s.d:
            print(el, end=" ")
        print("}")

    def add_element(s):
        el = input("Enter the element to be added: ")
        if el in s.d:
            print(f"Element {el} is already in the set.")
        else:
            s.d.add(el)
            print(f"Element {el} added to the set.")

    def remove_element(s):
        el = input("Enter the element to be removed: ")
        if el in s.d:
            s.d.remove(el)
            print(f"Element {el} removed from the set.")
        else:
            print(f"Element {el} not found in the set.")


if __name__ == '__main__':
    s1 = Set()
    s2 = Set()
    while True:
        print("Select an option:")
        print("1. Print set1")
        print("2. Add element to set1")
        print("3. Remove element from set1")
        print("4. Print set2")
        print("5. Add element to set2")
        print("6. Remove element from set2")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        elif choice == 1:
            s1.print_set()
        elif choice == 2:
            s1.add_element()
        elif choice == 3:
            s1.remove_element()
        elif choice == 4:
            s2.print_set()
        elif choice == 5:
            s2.add_element()
        elif choice == 6:
            s2.remove_element()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Try again.")
