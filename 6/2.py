class TreeNode:
    def __init__(self, label):
        self.parent = None
        self.label = label
        self.children = []
        self.depth = 0

    def __str__(self):
        return self.label

    def str_subtree(self):
        s = (" " * (self.depth - 1)) + \
            ["└> ", ""][self.parent is None] + \
            "%s (%s, P=%s, C=[%s])\n" % (self.label, self.depth, self.parent, ",".join([str(c) for c in self.children]))

        for c in self.children:
            s += c.str_subtree()

        return s

    def get_depth(self):
        depth = 0
        el = self

        while el.parent is not None:
            depth += 1
            el = el.parent

        return depth

    def attach(self, node):
        node.parent = self
        self.children.append(node)

    def find(self, node):
        if self.label == node:
            return self

        for c in self.children:
            n = c.find(node)
            if n:
                return n

        return None


def calculate_depths(node):
    node.depth = node.get_depth()
    for c in node.children:
        calculate_depths(c)


dependencies = {}
nodes = {}
for l in open("in").read().split():
    key = l.split(")")[0].strip()
    value = l.split(")")[1].strip()

    dependencies[value] = key

    # create nodes
    if not key in nodes:
        nodes[key] = TreeNode(key)
    if not value in nodes:
        nodes[value] = TreeNode(value)

# use dependencies to set correct parent for each node
root_node = None
for star in sorted(nodes):
    node = nodes[star]

    if star not in dependencies:
        root_node = node
    else:
        parent_node = nodes[dependencies[star]]
        parent_node.attach(node)

# print(root_node.str_subtree())

calculate_depths(root_node)

me = root_node.find("YOU")
santa = root_node.find("SAN")

# find deepest subtree containing santa and me
possible_subtrees = []


def find_subtree_root(node):
    if node.find("YOU") and node.find("SAN"):
        possible_subtrees.append(node)
        for c in node.children:
            find_subtree_root(c)
    return


find_subtree_root(root_node)

subtree_root = None
max_depth = 0
for st in possible_subtrees:
    if st.depth > max_depth:
        subtree_root = st
        max_depth = st.depth

# find and count nodes from me to root of subtree
me_to_subroot = 0
while me.parent != subtree_root:
    me_to_subroot += 1
    me.parent = me.parent.parent

# print(me_to_subroot)

# find and count nodes from root of subtree to santa
subroot_to_santa = 0
sr = subtree_root


def count_subroot_to_santa(node, count):
    if santa not in node.children:
        for c in node.children:
            count_subroot_to_santa(c, count + 1)
    else:
        global subroot_to_santa
        subroot_to_santa = count


count_subroot_to_santa(subtree_root, 0)

print(subroot_to_santa + me_to_subroot)