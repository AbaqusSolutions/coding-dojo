def sum_numbers(a: float, b: float) -> float:
    """
    Calculates the sum of two numbers.
    
    :param a: The first addend
    :param b: The second addend
    :return: The sum of a and b
    """
    return a + b

def next_state(initial_state: tuple[int, int, str], action: str):
    x, y, direction = initial_state
    match action:
        case 'L':
            match direction:
                case 'N':
                    return (x, y, 'W')
                case 'W':
                    return (x, y, 'S')
                case 'E':
                    return (x, y, 'N')
                case 'S':
                    return (x, y, 'E')
        case 'R':
            match direction:
                case 'N':
                    return (x, y, 'E')
                case 'W':
                    return (x, y, 'N')
                case 'E':
                    return (x, y, 'S')
                case 'S':
                    return (x, y, 'W')
        case 'M':
            match direction:
                case 'N':
                    return (x, y+1, 'N')
                case 'W':
                    return (x-1, y, 'W')
                case 'E':
                    return (x+1, y, 'E')
                case 'S':
                    return (x, y-1, 'S')
        
def validate_state (state: tuple[int, int, str], xy_dimensions: tuple[int, int]):
