from z3 import *

def max_volume_from_sa(surface_area):
    """
    Calculates the side length of the square base and height
    of a rectangular prism that uses the given surface area
    to maximize its volume
    """

    side_length = Real("side_length")
    height = Real("height")

    opt = Optimize()

    # Add constraints on the side length and height to
    # reduce computation time for the Optimizer
    opt.add(side_length > 0)
    opt.add(height > 0)
    opt.add(side_length <= RealVal(surface_area))
    opt.add(height <= RealVal(surface_area))

    # Add surface area constraint
    surface_area_constraint = (side_length ** 2) + (4 * side_length * height) == RealVal(surface_area)
    opt.add(surface_area_constraint)

    # Equation to maximize
    opt.maximize((side_length ** 2) * height)

    if opt.check() != sat:
        raise ArithmeticError("Optimization not satisfiable")
    m = opt.model()

    side_length = convert_to_float(m.eval(side_length))
    height = convert_to_float(m.eval(height))

    print(f"Calculated Volume = {(side_length ** 2) * height}")

    return side_length, height

# Do not modify this function!
# Works as described below
def convert_to_float(z3_number):
    """ 
    Converts AlgebraicNumRef, IntNumRef, and RatNumRef
    to a float from its string representation
    """

    # Get the Z3 Number's string representation
    z3_number_string = str(z3_number)

    # Remove ? from long decimal number if necessary
    z3_number_string = z3_number_string.rstrip('?')

    # Convert remaining string to a float
    z3_number_float = float(z3_number_string)

    return z3_number_float