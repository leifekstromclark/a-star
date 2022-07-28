class Node():
    def __init__(self, position, hcost, gcost=0, parent=None):
        self.position = position
        self.hcost = hcost
        self.gcost = gcost
        self.fcost = self.hcost + self.gcost
        self.parent = parent

class Heap():
    def __init__(self):
        self.items = []
    
    def get_children(self, i):
        return (2 * i + 1, 2 * i + 2)
    
    def get_parent(self, i):
        return (i - 1) // 2
    
    def switch(self, a, b):
        h = self.items[a]
        self.items[a] = self.items[b]
        self.items[b] = h
    
    def get_smallest_child(self, child_indices):
        child_fcosts = (self.items[child_indices[0]].fcost, self.items[child_indices[1]].fcost)
        if child_fcosts[0] > child_fcosts[1]:
            smallest_index = child_indices[1]
        elif child_fcosts[0] == child_fcosts[1]:
            child_hcosts = (self.items[child_indices[0]].hcost, self.items[child_indices[1]].hcost)
            if child_hcosts[0] > child_hcosts[1]:
                smallest_index = child_indices[1]
            else:
                smallest_index = child_indices[0]
        else:
            smallest_index = child_indices[0]
        return smallest_index

    def bubble_down(self, i):
        bubble = self.items[i]
        child_indices = self.get_children(i)
        if child_indices[0] < len(self.items):
            if child_indices[1] < len(self.items):
                smallest_index = self.get_smallest_child(child_indices)
            else:
                smallest_index = child_indices[0]
            smallest = self.items[smallest_index]
            while bubble.fcost > smallest.fcost or (bubble.fcost == smallest.fcost and bubble.hcost > smallest.hcost):
                self.switch(i, smallest_index)
                i = smallest_index
                child_indices = self.get_children(i)
                if child_indices[0] < len(self.items):
                    if child_indices[1] < len(self.items):
                        smallest_index = self.get_smallest_child(child_indices)
                    else:
                        smallest_index = child_indices[0]
                    smallest = self.items[smallest_index]
                else:
                    break

    
    def bubble_up(self, i):
        if i > 0:
            bubble = self.items[i]
            parent_index = self.get_parent(i)
            parent = self.items[parent_index]
            while parent.fcost > bubble.fcost or (parent.fcost == bubble.fcost and parent.hcost > bubble.hcost):
                self.switch(i, parent_index)
                i = parent_index
                if i == 0:
                    break
                parent_index = self.get_parent(i)
                parent = self.items[parent_index]

    def take(self, index):
        item = self.items[index]
        if len(self.items) >= 3 and index != len(self.items) - 1:
            self.items[index] = self.items.pop(-1)
            self.bubble_up(index)
            self.bubble_down(index)
        else:
            del self.items[index]
        return item
    
    def append(self, item):
        self.items.append(item)
        self.bubble_up(len(self.items)-1)