# advanced function demonstration
PI = 3.14159 #____
def calculate_sphere_volume(radius: float) -> float:
    """Calculate the volume of a sphere given its radius.

    Uses the mathematical formula: V = (4/3) * PI * r^3
    and utilizes the global constant PI.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.

    """
    return (4 / 3) * PI * (radius ** 3)

    