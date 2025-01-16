import numpy as np

#   Basic Flowfield
M1 = 5
gamma = 1.4
beta = 16.5
beta_rad = np.radians(beta)

#   Define TE constants
L = 10                                # Max. Length (See User Menu)
Rs = L * np.tan(np.radians(beta))    # Trailing Edge Parameter (See User Menu)
R1 = 0.2 * Rs                        # Trailing Edge Parameter (See User Menu)
W2 = 0.8 * Rs                        # Trailing Edge Parameter (See User Menu)

#   Resolution
N = 500                      # Leading Edge Resolution (500 or more is recommended!)
N_l = 12                     # Lower Surface Resolution
N_up = 10                    # Upper Surface Resolution

#   Trailing Edge Curve
a = -R1
b = 2 * (R1 - np.sqrt(Rs**2 - W2**2)) / W2**2
c = (np.sqrt(Rs**2 - W2**2) - R1) / W2**4

#   Trailing Edge Function
def z(y):
    func = a + b * y**2 + c * y**4    # Define Your Own Trailing Edge Function
    return func