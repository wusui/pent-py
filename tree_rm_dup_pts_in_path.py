# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Remove duplicate points in path
"""
from functools import reduce
from utilities import comp_points
from tree_get_ancestors import tree_get_ancestors

def tree_rm_dup_pts_in_path(tree):
    """
    Remove duplicate points in a tree's path (essentially remove a point
    from the list of points to be added if that point exists in a node
    somewhere in the ancestor path)

    @param {tuple} tree Tree
    @return {tuple} Tree with duplicate points removed
    """
    return map(_rm_same_point(tree), tree)

def _rm_same_point(tree):
    def _inner1(tnode):
        if "offspring" in tnode:
            return {
                "offspring": _rm_same_pt_offspring(tree)(tnode),
                "parent": tnode["parent"],
                "point": tnode["point"]
            }
        return tnode
    return _inner1

def _rm_same_pt_offspring(tree):
    def _inner1(tnode):
        return {
            "index": tnode["offspring"]["index"],
            "points": _rm_dup_pts(tree_get_ancestors(tree)
                                  (tnode["offspring"]["index"]))(
                                      tnode["offspring"]["points"])
        }
    return _inner1

def _rm_dup_pts(plist):
    """
    Remove points in one list from another list

    @param {tuple} plist Points to be removed
    @param {tuple} point_list Points to be searched
    @return {tuple} List of Points with plist entries removed
    """
    def _inner1(point_list):
        return tuple([cpoint for cpoint in point_list
                      if _point_not_match(plist)(cpoint)])
    return _inner1

def _point_not_match(plist):
    def _inner1(entry):
        return not reduce(_or_reduction, tuple(map(comp_points(entry),
                                                   plist)))
    return _inner1

def _or_reduction(aval, bval):
    return aval or bval
