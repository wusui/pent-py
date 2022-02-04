# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Generate a tier
"""
from utilities import flatten

def tree_gen_next_tier(tree):
    """
    Generate the next tier on the tree

    @param {tuple} tree Existing tree
    @param {tuple} Updated tree with nodes of the next tier added
    """
    return _new_next_tier_nodes(_make_next_tier(_get_new_leaf_info(
        _find_new_nodes(tree))))

def _get_new_leaf_info(tree):
    return (tuple(map(_get_offspring_points, tree)),
            tuple(map(_get_offspring_index, tree)))

def _get_offspring_points(node):
    return node["offspring"]["points"]

def _get_offspring_index(node):
    return node["offspring"]["index"]

def _new_next_tier_nodes(info):
    return tuple(map(_next_tier_wrapped, info))

def _next_tier_wrapped(tier):
    return {"parent": tier[1], "point": tier[0]}

def _make_next_tier(lev_info):
    return zip(flatten(lev_info[0]), flatten(_get_flat_parent_links(
        tuple(_get_parent_link_values(lev_info)))))

def _get_parent_link_values(next_level):
    return zip(_extract_length(next_level[0]), next_level[1])

def _extract_length(next_level):
    return tuple(map(len, next_level))

def _get_flat_parent_links(link_info):
    return tuple([_flat_parent_links(xval) for xval in link_info])

def _flat_parent_links(xval):
    return tuple([xval[1] for _ in range(0, xval[0])])

def _find_new_nodes(tree):
    return tuple(filter(_find_new_nodes_wrapped, tree))

def _find_new_nodes_wrapped(node):
    return "offspring" in node
