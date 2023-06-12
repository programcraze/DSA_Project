import random
import time
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.down = None

class SkipList:
    def __init__(self):
        self.levels = [Node(float('-inf'))]  # Initialize the bottom level with a sentinel node
        self.count=0 # to count the no of comparisons 
    def insert(self, value):
        start=time.perf_counter()
        # Insert the node in level 1 (always) so that a linked list can be created at the bottom level
        node = Node(value)
        current = self.levels[0]
        while current.next is not None and current.next.value < value:
            current = current.next
        node.next = current.next
        current.next = node

        # Randomly insert the node in higher levels
        level = 1
        while random.random() < 0.5: 
            # Check if level exists, otherwise create a new level
            if level == len(self.levels): # if the value is same then it means that the level is not created
                new_level = Node(float('-inf')) # creation of new node and initialize it with sentinel node
                new_level.down = self.levels[level - 1] # to point to the level below  
                self.levels.append(new_level) # to append the new level into the list levels

            # Move up to the next level
            current = self.levels[level] # moving to the currently pointed level 
            while current.next is not None and current.next.value < value: 
                current = current.next
            node = Node(value) # inserting the value in the layer 
            node.next = current.next
            current.next = node
            node.down = self.levels[level - 1] # to point to below layers

            level += 1
        end=time.perf_counter()
        exp=end-start
        print("Insert :")
        print("Execution time :",exp,"in seconds")
        print("Execution time :",exp*1000,"in milli seconds")
    def search(self, value):
        start=time.perf_counter()
        current = self.levels[-1]  # Start at the top level
        while current is not None:
            if current.next is None or current.next.value > value:

                # Move to the level below
                current = current.down if current.down is not None else None
                self.count+=1
            elif current.next.value == value:
                # Found the value
                print("The no of comparisons is :",self.count)
                print("True")
                break
            else:
                # Move to the next node in the current level
                current = current.next
        self.count=0
        print("False")
        end=time.perf_counter()
        exp=end-start
        print("Search :")
        print("Execution time :",exp,"in seconds")
        print("Execution time :",exp*1000,"in milli seconds")

    def delete(self, value):
        start=time.perf_counter()
        current = self.levels[-1]  # Start at the top level
        while current is not None:
            if current.next is None or current.next.value > value:
                # Move to the level below
                current = current.down if current.down is not None else None
            elif current.next.value == value:
                # Found the node to delete
                current.next = current.next.next
                current = current.down if current.down is not None else None
            else:
                # Move to the next node in the current level
                current = current.next
        end=time.perf_counter()
        exp=end-start
        print("delete :")
        print("Execution time :",exp,"in seconds")
        print("Execution time :",exp*1000,"in milli seconds")

    def display(self):
        start=time.perf_counter()
        for level in reversed(self.levels):
            current = level.next
            while current is not None:
                print(current.value,end=" ->")
                current = current.next
            print()
        end=time.perf_counter()
        exp=end-start
        print("display :")
        print("Execution time :",exp,"in seconds")
        print("Execution time :",exp*1000,"in milli seconds")


skip_list = SkipList()
exit=False
while exit==False:
    # Insert values into the skip list
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Print")
    ch=int(input("Enter the choice :"))
    if ch==1:
        print()
        v=int(input("Enter the value to be inserted :"))
        skip_list.insert(v)
        print()
    if ch==4:
    # Display the skip list
        print()
        print("Skip List:")
        skip_list.display()
        print()
    if ch==3:
    # Search for values in the skip list
        print()
        sr=int(input("Enter the value :"))
        print()
        print("Search Results:")
        print(skip_list.search(sr)) 
        print()
    if ch==2:
    # Delete values from the skip list
        print()
        dl=int(input("Enter the value :"))
        print()
        skip_list.delete(dl)
        # Display the updated skip list
        print("Updated Skip List:")
        skip_list.display()
    print()
    ex=input("Do you want to exit?")
    print()
    if ex=="Y":
        exit=True



