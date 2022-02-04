# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Common functions used by the pentomino solver
"""
def flatten(tuple_entry):
    """
    Given a tuple of tuples and objects, flatten into one tuple of objects

    @param {Tuple} tuple_entry Tuple containing possibly nested tuples
    @return {Tuple} One dimensional tuple of objects
    """
    if len(tuple_entry) == 0:
        return tuple_entry
    if isinstance(tuple_entry[0], tuple):
        return flatten(tuple_entry[0]) + flatten(tuple_entry[1:])
    return tuple_entry[:1] + flatten(tuple_entry[1:])

def comp_points(point1):
    """
    Compare two points.  Points are considered the same if their corresponding
    row values and col values are equal.

    @param {point} point1 First point
    @param {point} point2 Second point
    @return {Boolean} true if x and y are the same, false otherwise
    """
    def _inner1(point2):
        return (point1["row"] == point2["row"]) and (
            point1["col"] == point2["col"])
    return _inner1

def eval_numb(point):
    """
    Evaluate a point, returning a number uniquely representing that location.

    @param {tuple} point point
    @returns {integer} unique figure number
    """
    return _eval_numb2(abs(point["row"]) + abs(point["col"]))(point["row"])

def _eval_numb2(sumv):
    def _inner1(rowv):
        return (0, 0, 2, 6, 12)[sumv] + rowv + (0, 0, 1, 2, 3)[sumv]
    return _inner1

def flip_2d(arr):
    """
    Flip a board layout (nxm becomes mxn)

    @param {Array} arr Rectangle layout
    @return {Array} Rectangle layout flipped along diagonal
    """
    return tuple(zip(*arr[::]))

def conv_tup_to_str(tupl):
    """
    Join all the string entries inside a tuple

    @param {tuple} tupl Tuple of strings
    @return {tuple} Tuple of one concatenated string
    """
    return tuple(map("".join, tupl))

def find_first_empty(rect):
    """
    Scan a rectangle and find first open square

    @param {Array} rect Board layout (rectangle)
    @return {tuple} x & y coordinates of the leftmost top blank square
    """
    return _find_first_empty_wrapped(len(rect[0]))(rect)

def _find_first_empty_wrapped(lsize):
    def _inner1(rect):
        return _find_first_empty_get_pt(lsize)("".join(rect).find("."))
    return _inner1

def _find_first_empty_get_pt(lsize):
    def _inner1(point):
        if point < 0:
            return (-1, -1)
        return (point // lsize, point % lsize)
    return _inner1

def chunkstring(string, length):
    """
    Convert a string to an n x length array

    @param {string} string Input string to convert
    @param {Integer} length Length of an array element
    @return {Array} Intended layout of a rectangle
    """
    return tuple(string[0+i:length+i] for i in range(0, len(string), length))
