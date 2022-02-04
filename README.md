# pent-py

# My Own Private Functional Programming Pentomino Project

### INTRODUCTION
This project finds all rectangular solutions using 12 free pentominos
(see https://en.wikipedia.org/wiki/Pentomino for more details).  I wrote
this set of python functions in order to get used to writing code using
the functional programming paradigm.  This code essentially solves the cases described in the "Constructing rectangular dimensions" section of the above Wiki link.

This problem seemed well suited for functional programming learning since the
only output is a solution.  It runs on python 3.9 or newer.

As far as I can tell, no parameters are changed by the execution of this program.  So I believe that this code is a pure functional programming implementation.

### GENERAL ALGORITHM
This program recursively tries placing different pentominos in a grid.  When adding
a pentomino, the position that is selected to place a pentomino is the leftmost highest
empty square.  With this restriction, we know that any square in the pentomino added will
not be further left of that square, and any square in the pentomino in the same column
as that square will be lower in the grid.  We also know that every square in the pentomino
will be at most 4 horizontal + vertical steps away from that starting square.  So the figure
below is a template of all possible square locations that a pentomino can have relative to
the starting point (X in this figure).

 <p align="center">
 <img src="http://www.warrensusui.com/toybox/src/drawings/figure1.png" alt="figure1"/>
 </p>

Each square in this template is uniquely numbered.  By always including X in any pentomino,
a pentomino placed in the grid can be identified by four numbers.  For example, the W-pentomino
has the following four orientations: [1, 4, 19,17], [0, 4, 9, 17], [0, 2, 7, 13], and [0, 1, 2, 7].
When two is raised to the power of each of the identifying numbers and the values added together,
the result is a unique number representing one of the pentomino layouts.

### RECTANGLES AND X-PENTOMINO SYMMETRY

The number of squares in the rectangle being solved must be 60 (12 pentominos of 5 squares each).
No matter how it is oriented, any pentomino that takes up a 3x3 area (X, Y, Z, F, T, V) cannot fit
in a 1x60 or 2x30 rectangle.  So the only valid pentomino dimensions are 3x20, 4x15, 5x12, and 6x10
(7, 8, and 9 do not evenly divide 60, and any higher number that is valid will just be a rotation of
one of the other rectangles listed).

A solution can be rotation or reflection of another solution.  If we limit the row count to be the
smaller dimension, in most cases there are four possible orientations for a solution.  The soution
can be unchanged, flipped along the X-axis, flipped along the Y-axis, or flipped on both the X-axis
and the Y-axis. As it turns out, flipping along both axis is equivalent to rotating the pentomino
180 degrees.

If we limit the location of the center of the X-Pentomino to be in the upper left quadrant of a
solution, then the other three orientations of the solution would place the center of the X-pentomino
in each of the other three quadrants.  Thus we can solve for only one orientation by restricting
the X-Pentomino location.  This would work for any pentomino, but for simplification the X-pentomino
is the best since there is only one orientation for it so all that is needed to specify where it is
and how it is layed out is location of the center.

### SPECIAL SYMMETRY CASES AND THE W-PENTOMINO

When one of the dimensions of the rectangle is odd (the row count in 3x20 and 5x12 rectangles and
the column count in 4x15 rectangles), then if the center of the X-Pentomino is on the center axis
the solution can be flipped along that axis and essentially produce a mirror image duplicate.  To
avoid this from happening, the location of the W-Pentomino is checked.  If there are more points
in the W-Pentomino to the left of or above the axis of rotation, then that solution or partial
solution is rejected.  The W-Pentomino was chosen for this test because no matter how it is oriented,
it will never have the same number of points on the same side of either the X or the Y axis.
Testing that it is not in the first half of a partial solution is an easier check than making sure
that if it is placed it is placed in either half.

### TREE STRUCTURE

To display this value, run the following python commands:
```
from pentomino import pentomino
print(pentomino())
```
The tree structure is a tuple of Objects called tree nodes.  Element 0 of the tree is a
root node representing point [0, 0] of a potential pentomino placement.  The data in the tree
nodes consists of branching nodes and leaf nodes.  Each node has a point data structure which
represents the coordinates of the node. Each node also has a parent value which is the index
of a node "further down" on the tree (this value is undefined for the root node).

Branch nodes also have a tuple of indices called branches.  These indices are the locations of
nodes in the tree that are further toward the leaves than their parent nodes.  Leaf nodes do
not have a branches attribute but instead have a symbol values.  If you take a leaf node and
follow all the parent branches to the root, the set of points in the nodes that you encounter will
map into a layout of a pentomino that matches the symbol value.

The tree structure is used to find pentomino solutions inside a rectangle.  It is generated by the
code itself, and does not contain any duplicate layouts.  In other words, every possible pentomino
layout is represented by the path from one and only one leaf node.

### MORE DETAILED ALGORITHM DESCRIPTION

* Get tree data
* Loop for each possible rectangle location
    * Loop for each possible X-pentomino location in the left quadrant of a rectangle
        * Search for a pentomino solution
            * If invalid holes exist (available blank areas have a number of empty squares not divisible by 5) return
            * If X-Pentomino is on a middle axis and W-Pentomino test fails, return
            * Search for first open blank spot
            * If there are no blank spots, a solution has been found
                * save rectangle as a solution
                * return
            * Generate a list of all pentominos that can fit in the next spot
            * Use a map to insert the solutions into new recursive solver calls (not very efficient but I wanted to see
            if this works).


