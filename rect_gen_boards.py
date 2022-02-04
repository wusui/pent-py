# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Generate starting rectangles
"""
from utilities import flatten

def rect_gen_boards():
    """
    Generate tuple of board sizes.  Each board size tuple will contain
    a set of tuples representing the board layout with the X-pentomino
    placed

    @return {tuple} board layouts
    """
    return tuple(map(_make_rectangles, _get_rectangles(tuple(range(3, 7)))()))

def _get_rectangles(rowc):
    def _inner1():
        return _get_dimensions(rowc)(tuple(map(_div_to_get_cols, rowc)))()
    return _inner1

def _div_to_get_cols(rowc):
    return 60 // rowc

def _get_dimensions(rowc):
    def _inner1(colc):
        def _inner2():
            return _collect_info(tuple(zip(rowc, colc)))
        return _inner2
    return _inner1

def _collect_info(rowsxcols):
    return tuple(zip(_gen_centers(rowsxcols), rowsxcols))

def _gen_centers(rowsxcols):
    return tuple(map(_gen_one_center, rowsxcols))

def _gen_one_center(rowsxcols):
    return _get_points(_comp_half(rowsxcols[0]))(_comp_half(rowsxcols[1]))()

def _get_points(rowr):
    def _inner1(colr):
        def _inner2():
            return tuple(zip(_get_row_pt(rowr, len(colr)),
                             _get_col_pt(colr)))[1:]
        return _inner2
    return _inner1

def _get_col_pt(colr):
    return colr * 2

def _get_row_pt(rowr, numb):
    return flatten(tuple(map(_get_a_row(numb), rowr)))

def _get_a_row(numb):
    def _inner1(rnum):
        return (rnum,) * numb
    return _inner1

def _comp_half(numb):
    return tuple(range(1, (numb + 1) // 2))

def _get_lines(indx):
    return ("." * 20, "." * 10 + 'X' + "." * 20, "." * 9 + 'XXX' +
            "." * 19)[indx]

def _make_rectangles(rect_data):
    return tuple(map(_mk_rect(rect_data[1]), rect_data[0]))

def _mk_rect(dims):
    def _inner1(cpoint):
        return tuple(map(_mk_lines(dims)(cpoint), tuple(range(0, dims[0]))))
    return _inner1

def _mk_lines(dims):
    def _inner1(cpoint):
        def _inner2(line_no):
            if line_no == cpoint[0]:
                return _get_lines(2)[10 - cpoint[1]:10 - cpoint[1] + dims[1]]
            if abs(line_no - cpoint[0]) == 1:
                return _get_lines(1)[10 - cpoint[1]:10 - cpoint[1] + dims[1]]
            return _get_lines(0)[0:dims[1]]
        return _inner2
    return _inner1
