# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Do the pentomino rotations
"""

def tree_figure_rotations(figure):
    """
    Find all rotations of a pentomino

    @param {dict} set of points on the tree
    @return {dict} 8 sets of points on the tree, corresponding to all
             rotations of the tree that are possible.
    """
    return tuple(_shift_pent(_rotation_info(figure)))

def _shift_pent(rot_info):
    return tuple([_fix_sol(ppos) for ppos in rot_info])

def _fix_sol(ppos):
    return _do_shift(min([colv['col'] for colv in ppos[1]]))(ppos)

def _do_shift(xshift):
    def _inner1(ppos):
        return _do_shift2(xshift)(min([rowv['row'] for rowv in ppos[1]
                                       if rowv['col'] == xshift]))(ppos)
    return _inner1

def _do_shift2(xshift):
    def _inner1(yshift):
        def _inner2(ppos):
            return tuple([{"row": sqr["row"] - yshift,
                           "col": sqr["col"] - xshift}
                          for sqr in ppos[1]])
        return _inner2
    return _inner1

def _rotation_info(figure):
    return tuple(map(_flip_diag,
                     tuple(map(_flip_col,
                               tuple(map(_flip_row,
                                         tuple(enumerate(
                                             (figure,) * 8))))))))

def _flip_row(epoint):
    if epoint[0] & 1 == 0:
        return epoint
    return (epoint[0], tuple(map(_flip_fig_row, epoint[1])))

def _flip_fig_row(figure):
    return {"row": figure["row"] * -1, "col": figure["col"]}

def _flip_col(epoint):
    if epoint[0] & 2 == 0:
        return epoint
    return (epoint[0], tuple(map(_flip_fig_col, epoint[1])))

def _flip_fig_col(figure):
    return {"row": figure["row"], "col": figure["col"] * -1}

def _flip_diag(epoint):
    if epoint[0] & 4 == 0:
        return epoint
    return (epoint[0], tuple(map(_flip_fig_diag, epoint[1])))

def _flip_fig_diag(figure):
    return {"row": figure["col"], "col": figure["row"]}
