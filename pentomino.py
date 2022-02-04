# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Pentomino Rectangle Solver
"""
from functools import reduce
from rect_gen_boards import rect_gen_boards
from rect_holes_good import rect_holes_good
from rect_asymmetry import rect_asymmetry
from tree_main_builder import tree_main_builder
from utilities import conv_tup_to_str
from utilities import flip_2d
from utilities import find_first_empty
from utilities import flatten
from utilities import chunkstring

def pentomino():
    """
    Main pentomino routine

    @return {string} solution as rectangles separated by a blank line
    """
    return _stringify(
        _pent_wrapper1(tree_main_builder())(rect_gen_boards()))

def _pent_wrapper1(tree):
    def _inner1(rects):
        return tuple(map(_pent_wrapper2(tree), rects))
    return _inner1

def _pent_wrapper2(tree):
    def _inner1(rects):
        return tuple(map(_solver_start(tree), rects))
    return _inner1

def _solver_start(tree):
    def _inner1(rect):
        return tuple(zip(*(iter(
            flatten(tuple(map(_solver(tree), (rect,))))
        ),) * len(rect)))
    return _inner1

def _solver(tree):
    def _inner1(rect):
        if not rect_holes_good(rect):
            return tuple([])
        if not rect_asymmetry(rect):
            return tuple([])
        return _place_piece(tree)(rect)(
            _get_swpoint(find_first_empty(conv_tup_to_str(flip_2d(rect)))))
    return _inner1

def _place_piece(tree):
    def _inner1(rect):
        def _inner2(origin):
            if origin == (-1, -1):
                return rect
            return tuple(map(_solver(tree),
                             tuple(map(_fill_figure(tree)(rect)(origin),
                                       tuple(filter(_check_unique(tree)(rect),
                                                    flatten(
                                                        _span_path(rect)(
                                                            origin)(tree)(
                                                                0))[0:-1]))))))
        return _inner2
    return _inner1

def _fill_figure(tree):
    def _inner1(rect):
        def _inner2(origin):
            def _inner3(node):
                return chunkstring(
                    str(
                        bytes(
                            tuple(
                                reduce(
                                    _xor_reduction, tuple(
                                        map(_use_bytes,
                                            tuple(
                                                map(
                                                    _add_symbol(
                                                        tree[node]["symbol"])(
                                                            "".join(
                                                                rect)),
                                                    tuple(
                                                        flatten(
                                                            _get_pent_points(
                                                                tree)
                                                            (rect)(origin)(
                                                                node)
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )[2:-1], len(rect[0]))
            return _inner3
        return _inner2
    return _inner1

def _use_bytes(string):
    return tuple(bytearray(string, "utf8"))

def _xor_reduction(aval, bval):
    return tuple(map(_xor_op(aval), enumerate(bval)))

def _xor_op(aval):
    def _inner1(bval):
        return aval[bval[0]] ^ bval[1]
    return _inner1

def _add_symbol(symbol):
    def _inner1(rect):
        def _inner2(symb):
            return rect[0:symb] + symbol + rect[symb+1:]
        return _inner2
    return _inner1

def _get_pent_points(tree):
    def _inner1(rect):
        def _inner2(origin):
            def _inner3(node):
                if node == []:
                    return node
                return (_get_1d_indx(tree[node])(origin)(len(rect[0])),
                        tuple(_get_pent_points(tree)(rect)(origin)(
                            tree[node]['parent'])))
            return _inner3
        return _inner2
    return _inner1

def _get_1d_indx(node):
    def _inner1(origin):
        def _inner2(rsize):
            return ((origin[0] + node['point']['row']) * rsize +
                    (origin[1] + node['point']['col']))
        return _inner2
    return _inner1

def _check_unique(tree):
    def _inner1(rect):
        def _inner2(pent):
            return tree[pent]["symbol"] not in  "".join(rect)
        return _inner2
    return _inner1

def _get_swpoint(point):
    return (point[1], point[0])

def _span_path(rect):
    def _inner1(start):
        def _inner2(tree):
            def _inner3(pointr):
                if pointr == []:
                    return []
                if _pt_is_bad(rect)(start)(tree)(pointr):
                    return _span_path(rect)(start)(tree)(
                        tree[pointr]["next"])
                if "branches" not in tree[pointr]:
                    return (pointr, _span_path(rect)(
                        start)(tree)(tree[pointr]["next"]))
                return _span_path(
                    rect)(
                        start)(
                            tree)(tree[pointr]["branches"][0])
            return _inner3
        return _inner2
    return _inner1

def _pt_is_bad(rect):
    def _inner1(start):
        def _inner2(tree):
            def _inner3(node):
                return not _is_point_okay(rect)(
                    (tree[node]['point']['row'] + start[0],
                     tree[node]['point']['col'] + start[1]))
            return _inner3
        return _inner2
    return _inner1

def _is_point_okay(rect):
    def _inner1(point):
        if point[0] < 0:
            return False
        if point[0] >= len(rect):
            return False
        if point[1] < 0:
            return False
        if point[1] >= len(rect[0]):
            return False
        if rect[point[0]][point[1]] != ".":
            return False
        return True
    return _inner1

def _stringify(pent_tups):
    return ''.join(flatten(tuple(map(_get_groups, pent_tups))))

def _get_groups(pgroup):
    if len(pgroup) == 0:
        return ""
    return tuple(map(_get_rects, pgroup))

def _get_rects(prect):
    return tuple(map(_fmt_rect, prect))

def _fmt_rect(pline):
    return reduce(_concat_lines, pline) +"\n\n"

def _concat_lines(aval, zval):
    return aval + "\n" + zval

print(pentomino())
