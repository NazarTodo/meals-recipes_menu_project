class LinkedList:

    def __init__(self):
        """
        Initiates list
        """
        self._head = None
        self._tail = None

    def empty(self):
        """
        Checks emptiness of List.
        :return: True if List is empty and False otherwise.
        """
        return self._head == None

    def change_metric(self):
        """
        Changes metrics
        """
        meas = ''
        am = ''
        node = self._head
        while node != None:
            if len(node.item) != 3:
                node = node.next
                continue
            name, amount, measure = node.item

            if measure == 'g':
                am = amount / 1000
                meas = 'kg'
            elif measure == 'ml':
                am = amount / 1000
                meas = 'l'
            else:
                am = amount
                meas = ''
            tup = (name, am, meas)
            node.item = tup
            node = node.next

    def __contains__(self, value):
        """
        Checks existence of value in the List.
        :param value: the value to be check.
        :return: True if value is in the List and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
            self._tail = self._head
        else:
            self._tail.next = Node(value)
            self._tail = self._tail.next

    def __str__(self):
        """
        Returns string representation
        :return: str
        """
        current = self._head
        to_return = '['
        while current != None:
            to_return += str(current.item) + ', '
            current = current.next
        to_return += ']'
        return to_return

    def __len__(self):
        """
        Finds length of a list
        :return length of a list
        """
        length = 0
        current = self._head
        while current != None:
            length += 1
            current = current.next

        return length


class Node:

    def __init__(self, item, next=None):
        """Instantiates a Node with default next of None"""
        self.item = item
        self.next = next

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.data)


class TwoWayNode(Node):
    def __init__(self, item, previous=None, next=None):
        Node.__init__(self, item.next)
        self.previous = previous
