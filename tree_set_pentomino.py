# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Set rotated pentomino value in each leaf node
"""
from tree_get_ancestors import tree_get_ancestors
from tree_figure_rotations import tree_figure_rotations
from utilities import eval_numb

def tree_set_pentomino(tree):
    """
    Set the pentomino value in all leaf tree nodes

    @param {dict} tree Tree
    @return {dict} tree with pentomino attributes added
    """
    return tuple(map(_set_pent(tree), enumerate(tree)))

def _set_pent(tree):
    def _inner1(node):
        if "branches" in node[1]:
            return node[1]
        return node[1] | {"pentomino": _pent_value(tree)(node)}
    return _inner1

def _pent_value(tree):
    def _inner1(pent_node):
        return min(tuple(map(_calc_pent, tree_figure_rotations(
            tree_get_ancestors(tree)(pent_node[0])))))
    return _inner1

def _calc_pent(points):
    return sum(tuple(map(_power_2, points))) - 1

def _power_2(point):
    return 2 ** eval_numb(point)
