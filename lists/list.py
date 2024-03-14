#Соин, Мищенко, Чулков БПМ-22-3
class ArrayList:
    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def append(self, value):
        self.data.append(value)

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def set(self, index, value):
        if 0 <= index < len(self.data):
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    def remove(self, value):
        try:
            self.data.remove(value)
        except ValueError:
            raise ValueError("Value not found in the list")

    def size(self):
        return len(self.data)
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return '[' + ', '.join(result) + ']'

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def get(self, index):
        if not self.head:
            raise IndexError("List is empty")
        current = self.head
        for _ in range(index):
            if current.next:
                current = current.next
            else:
                raise IndexError("Index out of range")
        return current.data

    def remove(self, value):
        if not self.head:
            raise ValueError("List is empty")
        if self.head.data == value:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        while current:
            if current.data == value:
                prev.next = current.next
                return
            prev = current
            current = current.next
        raise ValueError("Value not found in the list")

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

import unittest

class TestArrayList(unittest.TestCase):
    def test_append_and_get(self):
        arr_list = ArrayList()
        arr_list.append(1)
        arr_list.append(2)
        self.assertEqual(arr_list.get(0), 1)
        self.assertEqual(arr_list.get(1), 2)

    def test_set(self):
        arr_list = ArrayList()
        arr_list.append(1)
        arr_list.append(2)
        arr_list.set(1, 3)
        self.assertEqual(arr_list.get(1), 3)

    def test_remove(self):
        arr_list = ArrayList()
        arr_list.append(1)
        arr_list.append(2)
        arr_list.append(10)
        arr_list.remove(10)
        self.assertEqual(arr_list.size(), 2)
        with self.assertRaises(ValueError):
            arr_list.remove(4)

    def test_size(self):
        arr_list = ArrayList()
        arr_list.append(1)
        arr_list.append(2)
        self.assertEqual(arr_list.size(), 2)

class TestLinkedList(unittest.TestCase):
    def test_append_and_get(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        self.assertEqual(linked_list.get(0), 1)
        self.assertEqual(linked_list.get(1), 2)

    def test_remove(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.remove(2)
        self.assertEqual(linked_list.size(), 2)
        with self.assertRaises(ValueError):
            linked_list.remove(4)

    def test_size(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        self.assertEqual(linked_list.size(), 2)
    def test_print(self):
        linked_list = LinkedList()
        linked_list.append([1,2,3])
        linked_list.append([])
        print(linked_list)

if __name__ == "__main__":
    unittest.main()
