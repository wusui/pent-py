# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Hole validity checker
"""
import re
from utilities import flatten
from utilities import flip_2d
from utilities import conv_tup_to_str
from utilities import find_first_empty

def rect_holes_good(rect):
    """
    Check open areas in a board

    @param {tuple} rect Partially filled board
    @return {boolean} True if hole sizes are valid. (divisible by 5)
    """
    return _scan_for_hole(find_first_empty(rect))(rect)

def _scan_for_hole(ospot):
    def _inner1(rect):
        if _hole_is_bad(rect):
            return False
        if ospot == (-1, -1):
            return True
        return rect_holes_good(_fill_hole(ospot)(rect))
    return _inner1

def _fill_hole(ospot):
    def _inner1(rect):
        return _add_to_rect(ospot)(_clear_marks(len(rect[0]))(rect))
    return _inner1

def _clear_marks(col_cnt):
    def _inner1(rect):
        return flatten(_make_rect_new(col_cnt)("".join(
            rect).replace("1", "2")))
    return _inner1

def _make_rect_new(col_cnt):
    def _inner1(old_str):
        if len(old_str) == 0:
            return ()
        return (old_str[0:col_cnt], _make_rect_new(col_cnt)(
            old_str[col_cnt:]))
    return _inner1

def _hole_is_bad(rect):
    return len(tuple(filter(_hcount, tuple("".join(rect))))) % 5 != 0

def _add_to_rect(ospot):
    def _inner1(rect):
        return _fill_sq(len(rect) * 2)(tuple(map(_add_to_square(ospot),
                                                 enumerate(rect))))
    return _inner1

def _fill_sq(count):
    def _inner1(rect):
        if count == 0:
            return rect
        return _fill_sq(count - 1)(conv_tup_to_str(
            flip_2d(_fix_rect(rect))))
    return _inner1

def _add_to_square(ospot):
    def _inner1(rect):
        if ospot[0] == rect[0]:
            return rect[1][0:ospot[1]] + '1' + rect[1][ospot[1]+1:]
        return rect[1]
    return _inner1

def _hcount(rchar):
    return rchar == "1"

def _re_repl(mtemp):
    return '1' * len(mtemp.group())

def _fix_rect(rect):
    return tuple(map(_fix_row, rect))

def _fix_row(rect_row):
    return re.sub(r'\.*1', _re_repl, re.sub(r'1\.*', _re_repl, rect_row))
