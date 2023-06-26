from K_map_gui_tk import *

# standard gray-code implementation
def gray_code(n):
    # print(f"n {n} ")
    if n < 1:
        g = []
    else:
        g = ['0', '1']
        n -= 1
        while n > 0:
            k = len(g)
            for i in range(k-1, -1, -1):
                char = '1' + g[i]
                g.append(char)
            for i in range(k-1, -1, -1):
                g[i] = '0' + g[i]
            n -= 1
    # print(f" g {g} ")
    return g

# for i in range (5):
#     gray_code(i)


def get_ends(a, n):
    if len(a) == n:
        return (0, n-1)
    
    if not (min(a) == 0 and max(a) == n-1):
        return (min(a), max(a))
    
    ct = 0
    while ct in a:
        ct += 1
    r = ct - 1

    ct = n - 1
    while ct in a:
        ct -= 1
    l = ct + 1
    
    return (l, r)
        
def is_legal_region(kmap_function, term):
    """
    determines whether the specified region is LEGAL for the K-map function
    Arguments:
    kmap_function: n * m list containing the kmap function
    for 2-input kmap this will 2*2
    3-input kmap this will 2*4
    4-input kmap this will 4*4
    term: a list of size k, where k is the number of inputs in function (2,3 or 4)
    (term[i] = 0 or 1 or None, corresponding to the i-th variable)
    Return:
    three-tuple: (top-left coordinate, bottom right coordinate, boolean value)
    each coordinate is represented as a 2-tuple
    """
    n = len(term)
    rows_set = set(range(len(kmap_function)))
    cols_set = set(range(len(kmap_function[0])))
    
    n_r = len(rows_set)
    n_c = len(cols_set)

    col_vars = {}
    row_vars = {}
    # row_vars = {2: [1], 3: [2], 4: [2, 3]}
    # col_vars = {2: [0], 3: [0, 1], 4: [0, 1]}
    v_c = (n+1)//2
    v_r = n - v_c
    col_vars[n] = list(range(v_c))
    row_vars[n] = list(range(v_c, n))

    k = {}
    # k[2] =  {0: [1], 1: [1]}
    # k[3] = {0: [2, 3], 1: [1, 2], 2: [1]}
    # k[4] = {0: [2, 3], 1: [1, 2], 2: [2, 3], 3: [1, 2]}
    k[n] = {}
    
    g_c = gray_code(v_c)
    g_r = gray_code(v_r)
    
    for i in range(n):
        k[n][i] = []

    for i in range(len(g_c)):
        for j in range(v_c):
            if g_c[i][j] == '1':
                k[n][j].append(i)

    
    for i in range(len(g_r)):
        for j in range(v_r):
            if g_r[i][j] == '1':
                k[n][j+v_c].append(i)
    # print(col_vars, row_vars)
    for i in row_vars[n]:
        if term[i] == 0:
            rows_set = rows_set - set(k[n][i])
        elif term[i] == 1:
            rows_set = rows_set.intersection(k[n][i])
    for i in col_vars[n]:
        if term[i] == 0:
            cols_set = cols_set - set(k[n][i])
        elif term[i] == 1:
            cols_set = cols_set.intersection(k[n][i])
    rows = [0] * n_r
    cols = [0] * n_c
    for r in rows_set:
        rows[r] = 1
    for c in cols_set:
        cols[c] = 1

    (u, d) = get_ends(rows_set, n_r)
    (l, r) = get_ends(cols_set, n_c)
    # print(rows_set, cols_set)
    # print ((u, l), (d, r))
    legal = True
    for i in rows_set:
        for j in cols_set:
            if kmap_function[i][j] == 0:
                legal = False
    
    return ((u, l), (d, r), legal)
    
# ########## Test - 4 vars ##########

# kmp4 = [[1,1,1,'x'], ['x',1,'x',0], [1,0,0,0], [1,'x',0,1]]
# root = kmap(kmp4)

# out = is_legal_region(kmp4, [0, None, None,None])
# root.draw_region(out[0][0], out[0][1], out[1][0], out[1][1],'blue')
# print(out)

# out = is_legal_region(kmp4, [1,1, None, None])
# root.draw_region(out[0][0], out[0][1], out[1][0], out[1][1],'green')
# print(out)

# out = is_legal_region(kmp4, [None,0,None,0])
# root.draw_region(out[0][0], out[0][1], out[1][0], out[1][1],'red')
# print(out)

# out = is_legal_region(kmp4, [1,0,0,1])
# root.draw_region(out[0][0], out[0][1], out[1][0], out[1][1],'yellow')
# print(out)

# root.mainloop()

# ########## Test - 3 vars ##########

kmp3 = [[0,1,'x', 0], ['x',1, 1,1]]
root = kmap(kmp3)

root.draw_region(0,1,1,2,'black')

out = is_legal_region(kmp3, [None, 0, None])
root.draw_region(out[0][0], out[0][1], out[1][0], out[1][1],'red')
print(out)

out = is_legal_region(kmp3, [0, 1, 1])
root.draw_region(out[0][0], out[0][1], out[1][0], out[1][1],'blue')
print(out)

out = is_legal_region(kmp3, [None, None, 0])
root.draw_region(out[0][0], out[0][1], out[1][0], out[1][1],'yellow')
print(out)

out = is_legal_region(kmp3, [1, 1, None])
root.draw_region(out[0][0], out[0][1], out[1][0], out[1][1],'green')
print(out)

root.mainloop()

# ######### Test - 2 vars ##########

# kmp2 = [[0,1], ['x', 1]]
# root = kmap(kmp2)

# out = is_legal_region(kmp2, [None, None])
# root.draw_region(out[0][0], out[0][1], out[1][0], out[1][1],'yellow')
# print(out)

# out = is_legal_region(kmp2, [0, 1])
# root.draw_region(out[0][0], out[0][1], out[1][0], out[1][1],'blue')
# print(out)

# out = is_legal_region(kmp2, [None, 1])
# root.draw_region(out[0][0], out[0][1], out[1][0], out[1][1],'red')
# print(out)

# root.mainloop()
# print(is_legal_region([[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1]], [1,1,1,1,1]))