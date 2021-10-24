class Node():
    def __init__(self, key):
        self.key = key
        self.next = None

def print_circular(head):
    if(head is None):
        return
    curr = head.next
    entered = False
    while(curr is not head):
        if(entered == False):
            print(head.key, end=" ")
            entered = True
        if(curr.next is head):
            print(curr.key)
        else:
            print(curr.key, end=" ")
        curr = curr.next
    if(entered == False):
        print(head.key)

def inser_beg(head, key):
    temp = Node(key)
    if(head is None):
        temp.next = temp
        return temp
    temp.next = head.next
    head.next = temp
    head.key, temp.key = temp.key, head.key
    return head

def insert_end(head, key):
    temp = Node(key)
    if(head is None):
        temp.next = temp
        return temp
    temp.next = head.next
    head.next = temp
    head.key, temp.key = temp.key, head.key
    return temp

def del_head(head):
    if(head is None):
        return
    elif(head.next is head):
        return
    else:
        head.key = head.next.key
        head.next = head.next.next
        return head

def del_kth_node(head, k):
    if(head is None):
        return
    elif(k == 1):
        return del_head(head)
    else:
        curr = head
        for i in range(k-2):
            curr = curr.next
        curr.next = curr.next.next
        return head

# Driver Code
head = Node(10)
head.next = head
head = insert_end(head, 20)
head = insert_end(head, 30)
head = insert_end(head, 40)
print_circular(head)
head = del_kth_node(head, 6)
print_circular(head)