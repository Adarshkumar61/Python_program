import math

def inverse_kinematics(x, y, L1, L2):
    
    # Compute joint angles (theta1, theta2) for a 2-link planar robot arm.
    # Parameters:
    #     x, y : target coordinates
    #     L1, L2 : lengths of links
    # Returns:
    #     (theta1, theta2) in radians (two possible solutions)


    # Step 1: distance from base to target
    d = math.sqrt(x**2 + y**2)

    # Step 2: check reachability
    if d > (L1 + L2):
        raise ValueError("Target is out of reach")

    # Step 3: cosine rule for theta2
    cos_theta2 = (d**2 - L1**2 - L2**2) / (2 * L1 * L2)

    # Clamp value to avoid floating point errors
    cos_theta2 = max(-1, min(1, cos_theta2))

    theta2a = math.acos(cos_theta2)        # Elbow down
    theta2b = -math.acos(cos_theta2)       # Elbow up

    # Step 4: compute theta1 for both cases
    def compute_theta1(theta2):
        alpha = math.atan2(y, x)
        beta = math.atan2(L2 * math.sin(theta2), L1 + L2 * math.cos(theta2))
        return alpha - beta

    theta1a = compute_theta1(theta2a)
    theta1b = compute_theta1(theta2b)

    return (theta1a, theta2a), (theta1b, theta2b)



L1, L2 = 10, 10
x, y = 10, 10

solutions = inverse_kinematics(x, y, L1, L2)

print("Solution 1 (elbow down): θ1 = {:.2f} rad, θ2 = {:.2f} rad".format(solutions[0][0], solutions[0][1]))
print("Solution 2 (elbow up):   θ1 = {:.2f} rad, θ2 = {:.2f} rad".format(solutions[1][0], solutions[1][1]))
