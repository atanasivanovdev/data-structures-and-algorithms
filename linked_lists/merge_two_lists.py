from linked_list import LinkedList

linked_list1 = LinkedList()
linked_list1.append(-9)
linked_list1.append(3)

linked_list2 = LinkedList()
linked_list2.append(5)
linked_list2.append(7)


def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    
    if list2 is None:
        return list1

    new_head = None
    current = None
    while list1.head is not None and list2.head is not None:
        if list1.head.value <= list2.head.value:
            head = list1.head
            list1.head = list1.head.next
        else:
            head = list2.head
            list2.head = list2.head.next

        if new_head is None:
            new_head = head
            current = new_head
        else:
            current.next = head
            current = current.next

    while list1.head is not None:
        current.next = list1.head
        list1.head = list1.head.next
        current = current.next

    while list2.head is not None:
        current.next = list2.head
        list2.head = list2.head.next
        current = current.next

    return new_head

print(mergeTwoLists(linked_list1, linked_list2))