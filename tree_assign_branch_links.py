# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Assign branch values to non-leaf nodes.
"""

def tree_assign_branch_links(tree):
    """
    After n
    @param {dict} tree tree
    @return {dict} Updated tree with branch values added
    """
    return tuple(map(_find_branches(_get_maxp(tree))(tree), enumerate(tree)))

def _get_maxp(tree):
    return max(map(_parent_chk, tree))

def _parent_chk(node):
    if node["parent"] == []:
        return -1
    return node["parent"]

def _find_branches(nonb_max):
    def _inner1(tree):
        def _inner2(node):
            if node[0] > nonb_max:
                return node[1]
            return node[1] | {"branches": _get_branch_list(enumerate(tree))(node)}
        return _inner2
    return _inner1

def _get_branch_list(tree):
    def _inner1(node):
        return tuple(map(_get_indx, tuple(filter(_chk_parent(node), tree))))
    return _inner1

def _chk_parent(node):
    def _inner1(tnode):
        return tnode[1]["parent"] == node[0]
    return _inner1

def _get_indx(node):
    return node[0]
