# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Add_branches
"""
from tree_get_next_points import tree_get_next_points
from tree_get_ancestors import tree_get_ancestors
from utilities import flatten

def tree_add_branches(tree):
    """
    Given a node, if the node has no branches, place potential
    branch information into the node under a key named offspring.

    @param {Tuple} tree tuple of node objects forming the tree
    @return {node} new nodes with offspring key added when the node
                   has no branches
    """
    def _inner1(indx):
        if "branches" in tree[indx]:
            return tree[indx]
        return tree[indx] | {'offspring': {'index': indx,
                                           'points': _check_all_points(
                                               tree_get_ancestors(tree)
                                               (indx))}}
    return _inner1

def _check_all_points(apoints):
    return flatten(tuple([tuple(x) for x in
                          tuple(map(tree_get_next_points, apoints))]))
