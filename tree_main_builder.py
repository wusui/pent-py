# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Make me a tree
"""
from tree_add_branches import tree_add_branches
from tree_rm_dup_pts_in_path import tree_rm_dup_pts_in_path
from tree_gen_next_tier import tree_gen_next_tier
from tree_rm_dup_paths import tree_rm_dup_paths
from tree_assign_branch_links import tree_assign_branch_links
from tree_get_figs import tree_get_figs
from tree_set_pentomino import tree_set_pentomino
from tree_gen_symbols import tree_gen_symbols
from tree_add_links import tree_add_links

def tree_main_builder():
    """
    Generate the tree by adding 4 tiers from the root point

    @return {tuple} tree
    """
    return tree_add_links(
        _tree_cleanup(tree_gen_symbols(tree_set_pentomino(
            tree_assign_branch_links(_get_full_tree(4)(_get_origin()))))))

def _get_origin():
    return ({"parent": [], "point": {"col": 0, "row": 0}},)

def _get_full_tree(levels):
    def _inner1(tree):
        if levels == 0:
            return tree
        return _get_full_tree(levels - 1)(_fix_origin(
            tuple(tree_rm_dup_pts_in_path(
                tuple(map(tree_add_branches(tree),
                          tuple(range(0, len(tree)))))))))
    return _inner1

def _fix_origin(ntree):
    return _get_origin() + _dup_path_fixer(ntree)

def _dup_path_fixer(old_tree):
    return tree_rm_dup_paths(tree_get_figs(
        tree_gen_next_tier(old_tree))(old_tree))

def _tree_cleanup(tree):
    return tuple(map(_clean_node, tree))

def _clean_node(tnode):
    if 'branches' in tnode:
        return {'branches': tnode["branches"], 'parent': tnode["parent"],
                'point': tnode["point"]}
    return {'parent': tnode["parent"], 'point': tnode["point"],
            'symbol': tnode["symbol"]}
