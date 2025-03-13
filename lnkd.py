if __name__ == "__main__":
    ll = LinkedList()
    
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()   # Output: 10 -> 20 -> 30 -> None

    ll.prepend(5)
    ll.display()   # Output: 5 -> 10 -> 20 -> 30 -> None

    ll.delete(20)
    ll.display()   # Output: 5 -> 10 -> 30 -> None
