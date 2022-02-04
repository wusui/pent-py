# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Get Next Point
"""
def tree_get_next_points(point):
    """
    Given a point, list all valid neighboring points on the grid.

    @param {point} point Point
    @return {tuple} List of valid points next to point.
    """
    return filter(_is_valid_location, _get_neighbors(point))

def _get_neighbors(point):
    return ({"col": point["col"] + 1, "row": point["row"]},
            {"col": point["col"] - 1, "row": point["row"]},
            {"col": point["col"], "row": point["row"] + 1},
            {"col": point["col"], "row": point["row"] - 1})

def _is_valid_location(point):
    return point["col"] > 0 or (point["col"] == 0 and point["row"] >= 0)
