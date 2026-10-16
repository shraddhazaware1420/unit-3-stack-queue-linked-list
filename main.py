"""
Name: Zaware Shraddha Sandip
Roll No.: 67 | Division: B | Batch: C
Unit III Case Study: Stack and Queue Using Linked Lists
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    """Stack follows Last In, First Out (LIFO)."""

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        value = self.top.data
        self.top = self.top.next
        return value

    def display(self):
        values = []
        current = self.top
        while current is not None:
            values.append(str(current.data))
            current = current.next
        return values


class LinkedQueue:
    """Queue follows First In, First Out (FIFO)."""

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def display(self):
        values = []
        current = self.front
        while current is not None:
            values.append(str(current.data))
            current = current.next
        return values


def main():
    stack = LinkedStack()
    queue = LinkedQueue()

    while True:
        print("\n=== Linked List Stack and Queue ===")
        print("1. Push onto stack")
        print("2. Pop from stack")
        print("3. Display stack")
        print("4. Add to queue (enqueue)")
        print("5. Remove from queue (dequeue)")
        print("6. Display queue")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            value = input("Enter a value to push: ").strip()
            if value:
                stack.push(value)
                print(f"{value} pushed onto the stack.")
            else:
                print("Value cannot be empty.")
        elif choice == "2":
            value = stack.pop()
            print(f"Popped value: {value}" if value is not None
                  else "Stack is empty.")
        elif choice == "3":
            values = stack.display()
            print("Top -> " + " -> ".join(values) if values
                  else "Stack is empty.")
        elif choice == "4":
            value = input("Enter a value to enqueue: ").strip()
            if value:
                queue.enqueue(value)
                print(f"{value} added to the queue.")
            else:
                print("Value cannot be empty.")
        elif choice == "5":
            value = queue.dequeue()
            print(f"Dequeued value: {value}" if value is not None
                  else "Queue is empty.")
        elif choice == "6":
            values = queue.display()
            print("Front -> " + " -> ".join(values) if values
                  else "Queue is empty.")
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Choose a listed option.")


if __name__ == "__main__":
    main()