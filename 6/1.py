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


def preorder_traversal_sum(node):
    s = node.get_depth()
    for c in node.children:
        s += preorder_traversal_sum(c)
    return s


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
for star in nodes:
    node = nodes[star]

    if star not in dependencies:
        root_node = node
    else:
        parent_node = nodes[dependencies[star]]
        parent_node.attach(node)

del nodes

print(root_node.str_subtree())