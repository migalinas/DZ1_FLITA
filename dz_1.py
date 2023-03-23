class Set:
    def __init__(s):
        s.d = set()

    def input_set(s):
        n = int(input("Enter the number of elements in the set: "))
        print("Enter the elements of the set:")
        for i in range(n):
            el = input()
            s.d.add(el)

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
    s = Set()
    s1 = Set()
    while True:
        print("Select an option:")
        print("1. Input set")
        print("2. Print set")
        print("3. Add element to set")
        print("4. Remove element from set")
        print("5. Input set1")
        print("6. Print set1")
        print("7. Add element to set1")
        print("8. Remove element from set1")
        print("9. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            s.input_set()
        elif choice == 2:
            s.print_set()
        elif choice == 3:
            s.add_element()
        elif choice == 4:
            s.remove_element()
        elif choice == 5:
            s1.input_set()
        elif choice == 6:
            s1.print_set()
        elif choice == 7:
            s1.add_element()
        elif choice == 8:
            s1.remove_element()
        elif choice == 9:
            break
        else:
            print("Invalid choice. Try again.")
