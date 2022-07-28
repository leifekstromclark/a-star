import heap
import vector

def get_hcost(c, b):
    dx = abs(b.x - c.x)
    dy = abs(b.y - c.y)
    if dx < dy:
        hcost = dx * 14 + 10 * (dy - dx)
    else:
        hcost = dy * 14 + 10 * (dx - dy)
    return hcost

# a and b are vectors on node grid
def find_path(a, b, board):
    op = heap.Heap()
    cl = []
    op.append(heap.Node(a, get_hcost(a, b)))
    
    while True:
        current = op.take(0)
        cl.append(current)
        if current.position.x == b.x and current.position.y == b.y:
            path = [current]
            for node in path:
                if node.parent:
                    path.append(node.parent)
            for i in range(len(path)):
                path[i] = path[i].position
            path.reverse() 
            return path
        for i in range(current.position.y-1, current.position.y+2):
            for k in range(current.position.x-1, current.position.x+2):
                if 0 <= i < len(board) and 0 <= k < len(board[0]) and (i != current.position.y or k != current.position.x) and board[i][k] == 0:
                    proceed = True
                    for node in cl:
                        if node.position.y == i and node.position.x == k:
                            proceed = False
                    if proceed == True:
                        
                        if abs(current.position.y - i) + abs(current.position.x - k) == 2:
                            add_gcost = 14
                        else:
                            add_gcost = 10
                        
                        gcost = current.gcost + add_gcost
                        
                        present = False
                        for index, node in enumerate(op.items):
                            if node.position.y == i and node.position.x == k:
                                present = True
                                if node.gcost > gcost:
                                    old = op.take(index)
                                    op.append(heap.Node(old.position, old.hcost, gcost, current))
                        if not present:
                            position = vector.Vector(k, i)
                            op.append(heap.Node(position, get_hcost(position, b), gcost, current))