import math
from typing import Dict


def reach_point(x: float, y: float, z: float, smooth: bool = True) -> Dict[str, float]:
    """
    Move the robot arm to a given (x, y, z) coordinate.

    Parameters:
    x (float): Target x-coordinate (mm)
    y (float): Target y-coordinate (mm)
    z (float): Target z-coordinate (mm)
    smooth (bool): Enable smooth trajectory motion

    Returns:
    dict: Motion details including steps, distance, and estimated time
    """

    # -------- Input Validation --------
    try:
        x, y, z = float(x), float(y), float(z)
    except ValueError:
        raise ValueError("Coordinates must be numeric values")

    # -------- Robot Configuration --------
    STEPS_PER_MM = 100          # motor resolution
    SPEED_MM_PER_SEC = 10       # arm speed

    # -------- Convert Coordinates to Steps --------
    steps = {
        "x_steps": int(x * STEPS_PER_MM),
        "y_steps": int(y * STEPS_PER_MM),
        "z_steps": int(z * STEPS_PER_MM)
    }

    # -------- Kinematics Calculations --------
    distance = math.sqrt(x**2 + y**2 + z**2)

    # -------- Time Estimation --------
    estimated_time = round(distance / SPEED_MM_PER_SEC, 2)

    # -------- Motion Execution (Simulation) --------
    motion_type = "Smooth trajectory" if smooth else "Direct movement"
    

    print(f"\n🔹 Target Position: X={x} mm, Y={y} mm, Z={z} mm")
    print(f"🔹 Motion Type: {motion_type}")
    print(f"🔹 Motor Steps: {steps}")
    print(f"🔹 Distance to Target: {round(distance, 2)} mm")
    print(f"🔹 Estimated Time: {estimated_time} seconds")

    return {
        "target": (x, y, z),
        "steps": steps,
        "distance_mm": distance,
        "estimated_time_sec": estimated_time,
        "smooth_motion": smooth
    }


# -------- Example Call --------
reach_point(500, 100, 150)
