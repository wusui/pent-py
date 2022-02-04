# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Add traversing links to the nodes in the tree
"""
def tree_add_links(tree):
    """
    TO DO: docstring this
    """
    return _tree_adjust_links(4, tuple(map(_tree_set_first_links(
        tuple(map(_tree_first_links(tree), tuple(enumerate(tree))))),
                                           enumerate(tree))))

def _tree_set_first_links(info):
    def _inner1(node_data):
        return node_data[1] | {"next": info[node_data[0]]}
    return _inner1

def _tree_first_links(tree):
    def _inner1(node_info):
        if node_info[1]["parent"] == []:
            return []
        if node_info[0] + 1 in tree[tree[node_info[0]]['parent']]['branches']:
            return node_info[0] + 1
        return -1
    return _inner1

def _tree_adjust_links(numb, tree):
    if numb == 0:
        return tree
    return _tree_adjust_links(numb - 1, _tree_mod_node(tree))

def _tree_mod_node(tree):
    return tuple(map(_tree_set_node(tree), tree))

def _tree_set_node(tree):
    def _inner1(node_info):
        if node_info["next"] == -1:
            return dict(node_info, next=tree[node_info['parent']]['next'])
        return node_info
    return _inner1
