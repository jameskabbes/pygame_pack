import numpy as np
from scipy.spatial import distance

def polar_to_cart(r, radians) -> np.array:

    """converts R,theta into X,Y"""

    x = r * np.cos(radians)
    y = r * np.sin(radians)
    return np.array( [x,y] )

def get_bearing( X: np.array ):

    """returns bearing in radians of (x,y) coordinates"""

    return np.arctan2( X[1], X[0])

def get_rot_matrix_2d( radians ) -> np.array:

    """get the 2d rotation matrix given radians"""

    return np.array( [ [np.cos(radians),-np.sin(radians)],[np.sin(radians),np.cos(radians)] ] )

def get_euc_dist( X1: np.array, X2: np.array ):

    """Given two position vectors, return the distance between the points"""

    return distance.euclidean( X1, X2 )

def is_collision( X1: np.array, X2: np.array, buffer ) -> bool:

    """Given two position vectors and a buffer, see if objects touch"""

    return get_euc_dist( X1, X2 ) < buffer

def angle_between_2d_vectors( X1: np.array, X2: np.array ):

    """find the angle from X1 to X2, returns radians"""

    return np.arctan2( (X2[1]-X1[1]) , (X2[0]-X1[0] ) )

def cap_magnitude( X: np.array, magnitude ) -> np.array:

    """cap the magnotude of Vector X at specified magnitude"""

    current_magnitude = np.linalg.norm(X)

    if current_magnitude > magnitude:
        X = X * (magnitude/current_magnitude)

    return X

def rotate_2d_vectors( X: np.array, radians ) -> np.array:

    """Given (x,y) pairs in matrix X, rotate"""

    rot_matrix = get_rot_matrix_2d( radians )
    rotated_coords = np.matmul( rot_matrix, X.T ).T
    return rotated_coords

