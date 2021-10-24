class Node():
    def __init__(self, key):
        self.key = key
        self.next = None

def print_list(head):
    curr = head
    while(curr is not None):
        if(curr.next is None):
            print(curr.key,end="\n")
        else:
            print(curr.key,end=" ")
        curr = curr.next

def search(head, x):
    pos = 1
    curr = head
    while(curr is not None):
        if(curr.key == x):
            return pos
        pos += 1
        curr = curr.next

def insert_begin(head, key):
    temp = Node(key)
    temp.next = head
    return temp

def insert_end(head, key):
    temp = Node(key)
    if(head is None):
        return temp
    curr = head
    while(curr.next is not None):
        curr = curr.next
    curr.next = temp
    return head

def insert_pos(head, pos, key):
    temp = Node(key)
    if(pos == 1):
        temp.next = head
        return temp
    curr = head
    for i in range(pos-2):
        curr = curr.next
        if(curr is None):
            return head
    temp.next = curr.next
    curr.next = temp
    return head

def del_first_node(head):
    if(head is None):
        return
    return head.next

def del_last_node(head):
    if(head is None):
        return
    elif(head.next is None):
        return
    curr = head
    while(curr.next.next is not None):
        curr = curr.next
    curr.next = None
    return head

def sorted_insert(head, key):
    temp = Node(key)
    if(head is None):
        return temp
    elif(key < head.key):
        temp.next = head
        return temp
    else:
        curr = head
        while(curr.next is not None and curr.next.key < key):
            curr = curr.next
        temp.next = curr.next
        curr.next = temp
        return head

def reverse_list(head):
    curr = head
    prev = None
    while(curr is not None):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def rec_reverse_1(head):
    if(head is None):
        return head
    elif(head.next is None):
        return head
    rest_head = rec_reverse_1(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None
    return rest_head

def rec_reverse_2(curr, prev=None):
    if(curr is None):
        return prev
    next = curr.next
    curr.next = prev
    return rec_reverse_2(next, curr)

# Driver Code
head = Node(10)
head = insert_end(head, 20)
head = insert_end(head, 30)
head = insert_end(head, 40)
print_list(head)
head = sorted_insert(head, 25)
print_list(head)
head = rec_reverse_2(head)
print_list(head)