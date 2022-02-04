# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Extra symmetry check
"""
from utilities import flip_2d
from utilities import conv_tup_to_str

def rect_asymmetry(rect):
    """
    Test for W-pentomino symmetry issues

    @param {Array} rect Rectangle with squares filled
    @return {Boolean} False if W-pentomino in first part of symmetric layout
    """
    return _test_asymmetry(_align_asymmetry(rect))

def _align_asymmetry(rect):
    if len(rect[0]) % 2 == 1:
        return conv_tup_to_str(flip_2d(rect))
    return rect

def _test_asymmetry(rect):
    if len(rect) % 2 == 0:
        return True
    if "XXX" not in rect[len(rect) // 2]:
        return True
    if _bad_w_pos(len(rect[0]) // 2)("".join(rect)):
        return False
    return True

def _bad_w_pos(bsize):
    def _inner1(rect):
        return  (rect[0 : 30 - bsize].count('W') >
                 rect[30 + bsize : 60].count('W'))
    return _inner1
