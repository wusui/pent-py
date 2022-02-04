# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Get Parents
"""
from utilities import flatten
def tree_get_ancestors(tree):
    """
    Given a node in the tree, get all points that are predecessors.

    @param {tuple} Tree tree
    @param {Integer} indx Index of node in tree
    @return {tuple} list of all points in the path from this node to the root
    """
    def _inner1(indx):
        return tuple(map(_get_pts_only,
                         flatten(_find_all_ancestors(tree)(tree[indx]))))
    return _inner1

def _get_pts_only(tnode):
    return tnode['point']

def  _find_all_ancestors(tree):
    def _inner1(tnode):
        if tnode["parent"] != []:
            return (tnode, _find_all_ancestors(tree)(tree[tnode["parent"]]))
        return (tnode,)
    return _inner1
