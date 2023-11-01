def make_binary_tree(root):
    return [root, [], []]


def insert_left(root, new_child):
    old_child = root.pop(1)
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []])
    else:
        root.insert(1, [new_child, [], []])
    return root

t = make_binary_tree('root')
insert_left(t, 'e')
insert_left(t, 'f')
insert_left(t, 'g')
insert_left(t, 'h')


print(t)