from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.node_map = {}
        self.size = 0
# fixed size.
# When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element.

# List is ordered from oldest (head) - newest (tail) item
# If adding item and list is full, remove oldest (head) item and add newest (tail) - First in First out = queue

    def append(self, item):
        
        if self.capacity is self.size:
            oldest_node = self.storage.tail
            self.storage.remove_from_tail
            del self.node_map[oldest_node[0]]
            self.size -= 1
    
        else:
            node_value = self.node_map[item]
            self.storage.delete(item[1])
            self.storage.add_to_head(item)
            self.node_map[item] = [self.storage.head]
            return node_value

        self.storage.add_to_head(item)
        self.node_map[item] = [self.storage.head]
        self.size += 1



    def get(self, item):
        # list_buffer_contents = []
        if item in self.node_map:
            node = self.node_map[item]
            self.storage.move_to_end(node)
            return node[1]
        else:
            return None

        # return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass