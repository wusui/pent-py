# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Add figure to tree nodes
"""
from utilities import eval_numb

def tree_get_figs(tnew):
    """
    Follow parent links from leaf node to find all points.  Compute
    the figure number and add it to the the node on the tree

    @param {dict} tnew Node on the tree
    @param {dict} tree tree
    @return {dict} Node with figure value added.
    """
    def _inner1(tree):
        return tuple(map(_set_fig_value(tree), tnew))
    return _inner1

def _set_fig_value(tree):
    def _inner1(tnode):
        return tnode | {"figure": _get_fig_value(tree)(tnode)}
    return _inner1

def _get_fig_value(tree):
    def _inner1(tnode):
        if tnode["parent"] == []:
            return 0
        return ((2 ** (eval_numb(tnode["point"]))) +
                _get_fig_value(tree)(tree[tnode["parent"]]))
    return _inner1
