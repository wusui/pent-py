# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Add symbol attribute to leaf nodes
"""

def tree_gen_symbols(tree):
    """
    Save pentomino symbols in the tree

    @param {dict} tree Tree
    @return {dict} Tree with symbol field added to all leaf nodes
    """
    return tuple(map(_set_symbol(_get_conv_data(tree)), tree))

def _set_symbol(ttable):
    def _inner1(tnode):
        if 'pentomino' not in tnode.keys():
            return tnode
        return tnode | {'symbol': 'FPXNVTYWZLUI'[ttable[tnode['pentomino']]]}
    return _inner1

def _get_conv_data(tree):
    return _mk_tbl(tuple(enumerate(_get_uniq_pent_numbs(tree))))

def _get_uniq_pent_numbs(tree):
    return tuple(sorted(list(set(map(_get_pent_num, tree))))[1:])

def _mk_tbl(pent_tab):
    if len(pent_tab) == 0:
        return {}
    return {pent_tab[0][1]: pent_tab[0][0]} | _mk_tbl(pent_tab[1:])

def _get_pent_num(pnumb):
    if 'pentomino' not in pnumb.keys():
        return -1
    return pnumb['pentomino']
