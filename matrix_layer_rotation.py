
## MATRIX LAYER ROTATION
# Hard


def left_rotation(seq, d):
    # shifts elements in array (seq) d elements to the left
    retval = [seq[i-(len(seq)-d)] for i in range(len(seq))]
    return retval


def rotate_loop(loop_list, rotations):
    # rotates items defining a loop 'rotations x' anticlockwise
    rot_apply = rotations % len(loop_list)
    retval = left_rotation(loop_list,rot_apply)
    return retval


def get_loops(m,n, loops):
    # define (i,j) coordinate lists of concentric 'loops'in matrix m x n
    i_tl, j_tl, i_br, j_br = 0,0,m-1,n-1
    loop_arrays = []
    loop_count = 1

    while loop_count <= loops:
        loop, top, rhs, bottom, lhs = [], [],[],[],[]
        top = [(i,j) for j in range(j_tl, j_br+1) for i in range(i_tl,i_tl+1)]
        rhs = [(i,j) for i in range(i_tl+1,i_br+1) for j in range(j_br,j_br+1)]
        bottom = [(i,j) for j in reversed(range(j_tl, j_br)) for i in range(i_br,i_br+1)]
        lhs = [(i,j) for i in reversed(range(i_tl+1,i_br)) for j in range(j_tl,j_tl+1)]
        loop = top+rhs+bottom+lhs
        loop_arrays.append(loop)
        loop_count+=1
        i_tl += 1
        j_tl += 1
        i_br -= 1
        j_br -= 1

    return loop_arrays


def matrixRotation(matrix, r):
    # get m,n # of loops and create blank new matrix
    m = len(matrix)
    n = len(matrix[0])
    loops = int(min(m, n)/2)
    newmat = [[0 for x in range(n)] for y in range (m)]

    # get loops and rotate
    loop_coords = get_loops(m,n,loops)
    rotated_coords = [rotate_loop(loop, r) for loop in loop_coords]

    # set values of new mat from rotated coords ref to mat
    for orig, rotd in zip(loop_coords, rotated_coords):
        for mat_ij, ref_ij in zip(orig, rotd):
            newmat[mat_ij[0]][mat_ij[1]] = matrix[ref_ij[0]][ref_ij[1]]

    return newmat
