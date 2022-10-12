class Node: # node class
    def __init__(self, value):
        self.lt = None
        self.rt = None
        self.val = value
        self.leaves = 1

    def insert(self, value): # insert a value
        self.leaves += 1
        if self.val == None:
            self.val = value
            return
        elif value < self.val: # insert left if less than root
            if self.lt != None:
                self.lt.insert(value)
                return
            self.lt = Node(value)
            return
        else: # insert right if >= root
            if self.rt != None:
                self.rt.insert(value)
                return
            self.rt = Node(value)
            return

def factorial(n): # calculate factorial of given n
    fct = 1
    for i in range(1,n+1):
        fct = fct * i
    return fct

def simplify(m, n):
    greater = m if m > n else n
    sum = m + n
    result = 1
    while sum > greater:
        result *= sum
        sum -= 1
    return result

def calc_perm(node): # recursively calculate permutations of left and right trees from root
    m = node.lt.leaves if node.lt is not None else 0
    n = node.rt.leaves if node.rt is not None else 0
    lesser = m if m < n else n
    result = simplify(m, n) // factorial(lesser)
    if node.lt is not None:
        result *= calc_perm(node.lt)
    if node.rt is not None:
        result *= calc_perm(node.rt)
    return int(result)

n_values = int(input())
while(n_values != 0):
    values = list(map(int, input().split(" ")))
    tree = Node(values[0])
    for i in range(1, len(values)):
        tree.insert(values[i])
    print(calc_perm(tree))
    n_values = int(input())
