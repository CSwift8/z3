# Instructions

With a provided amount of surface area, implement a function that calculates
the length, width, and height of an open rectangular prism that uses this surface area,
such that the volume of the open rectangular prism is maximimized.  Assume the base of the
rectangular prism is a square; in other words, the length and width of the rectangular 
prism are equal.  The rectangular prism is considered "open" because there is no sixth side of 
the prism; it is an open box with the square base and 4 adjacent side flaps.  The side 
length of the square base and height of the rectangular prism should be returned by the 
function as a tuple of floats.

Constraints on the side length and height may be needed to reduce computation time.

Since the model interpretation of a Z3 Real variable is an instance of
AlgebraicNumRef, IntNumRef, or RatNumRef, a function is provided to convert
this instance to a float.