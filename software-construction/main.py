from stack import Stack
from queue import Queue
from linkedlist import SinglyLinkedList

def visualize_stack(stack):
    print("\nStack Visualization (top to bottom):")
    for item in reversed(stack._items):
        print(f"| {item} |")
    print(" -----")

def visualize_queue(queue):
    print("\nQueue Visualization (front to rear):")
    queue_list = list(queue._items)
    print(" <- ".join(str(i) for i in queue_list))

def visualize_linkedlist(linkedlist):
    print("\nSingly Linked List Visualization:")
    print(str(linkedlist))

def main():
    print("Welcome to MIVA Open University Data Structures Demo!")
    stack = Stack()
    queue = Queue()
    linkedlist = SinglyLinkedList()

    while True:
        print("\nChoose a data structure to work on:")
        print("1. Stack")
        print("2. Queue")
        print("3. Singly Linked List")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            print("\n-- Stack Operations --")
            print("a. Push item")
            print("b. Pop item")
            print("c. Peek top")
            print("d. Visualize stack")
            option = input("Choose operation (a-d): ").strip().lower()
            if option == 'a':
                item = input("Enter item to push: ")
                stack.push(item)
                print(f"Pushed '{item}' to stack.")
            elif option == 'b':
                try:
                    popped = stack.pop()
                    print(f"Popped '{popped}' from stack.")
                except IndexError as e:
                    print(e)
            elif option == 'c':
                top = stack.peek()
                print(f"Top of stack is: {top}")
            elif option == 'd':
                visualize_stack(stack)
            else:
                print("Invalid option.")

        elif choice == '2':
            print("\n-- Queue Operations --")
            print("a. Enqueue item")
            print("b. Dequeue item")
            print("c. Peek front")
            print("d. Visualize queue")
            option = input("Choose operation (a-d): ").strip().lower()
            if option == 'a':
                item = input("Enter item to enqueue: ")
                queue.enqueue(item)
                print(f"Enqueued '{item}' to queue.")
            elif option == 'b':
                try:
                    dequeued = queue.dequeue()
                    print(f"Dequeued '{dequeued}' from queue.")
                except IndexError as e:
                    print(e)
            elif option == 'c':
                front = queue.peek()
                print(f"Front of queue is: {front}")
            elif option == 'd':
                visualize_queue(queue)
            else:
                print("Invalid option.")

        elif choice == '3':
            print("\n-- Singly Linked List Operations --")
            print("a. Append item")
            print("b. Prepend item")
            print("c. Delete item")
            print("d. Find item")
            print("e. Visualize list")
            option = input("Choose operation (a-e): ").strip().lower()
            if option == 'a':
                item = input("Enter item to append: ")
                linkedlist.append(item)
                print(f"Appended '{item}' to linked list.")
            elif option == 'b':
                item = input("Enter item to prepend: ")
                linkedlist.prepend(item)
                print(f"Prepended '{item}' to linked list.")
            elif option == 'c':
                item = input("Enter item to delete: ")
                deleted = linkedlist.delete_with_value(item)
                if deleted:
                    print(f"Deleted '{item}' from linked list.")
                else:
                    print(f"Item '{item}' not found.")
            elif option == 'd':
                item = input("Enter item to find: ")
                found = linkedlist.find(item)
                print(f"Item '{item}' found: {found}")
            elif option == 'e':
                visualize_linkedlist(linkedlist)
            else:
                print("Invalid option.")

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice, please select 1-4.")

if __name__ == "__main__":
    main()
