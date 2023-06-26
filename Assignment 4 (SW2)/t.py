from K_map_gui_tk import *

def get_literals(term):
    if len(term) == 0:
        return []
    ls = []
    prev = term[0]
    for i in term[1:]:
        if i == '\'':
            prev = str(prev) + '\''
        else:
            ls.append(prev)
            prev = i

    ls.append(prev)
    return ls

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

print(gray_code(3))

def get_coordinate(term):
    literals = list(get_literals(term))
    n = len(literals)
    n_row = n//2
    n_column = (n+1)//2

    l_row = gray_code(n_row)
    l_column = gray_code(n_column)

    # print(term)
    # print(f"lrow {l_row} \nlcol {l_column} ")

    row_literal = literals[n_column:]
    col_literal = literals[0:n_column] 

    # print(f"rowlit {row_literal} collit {col_literal} ")

    s1 = ""; s2 = ""

    for lit in row_literal:
        if(len(lit) == 1): s1+='1'
        else: s1+='0'
    for lit in col_literal:
        if(len(lit) == 1): s2+='1'
        else: s2+='0'

    # print(f"s1 {s1} s2 {s2} ")

    return (l_row.index(s1), l_column.index(s2))


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

def end_points(kmap_function, term):
    n = len(term)
    rows_set = set(range(len(kmap_function)))
    cols_set = set(range(len(kmap_function[0])))
    
    n_r = len(rows_set)
    n_c = len(cols_set)

    col_vars = {}
    row_vars = {}
    v_c = (n+1)//2
    v_r = n - v_c
    col_vars[n] = list(range(v_c))
    row_vars[n] = list(range(v_c, n))

    k = {}
    k[n] = {}
    
    g_c = gray_code(v_c)
    g_r = gray_code(v_r)
    
    for i in range(n): k[n][i] = []

    for i in range(len(g_c)):
        for j in range(v_c):
            if g_c[i][j] == '1':
                k[n][j].append(i)
    
    for i in range(len(g_r)):
        for j in range(v_r):
            if g_r[i][j] == '1':
                k[n][j+v_c].append(i)

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
    
    return (u, l, d, r)

def draw_area(root, term, color, kmapl, n):
    t =  [None for i in range(n)]
    literals = get_literals(term)
    s = "abcdefghijklmnopqrstuvwxyz"
    for lit in literals:
        if(len(lit) == 1):
            t[s.find(lit[0])] = 1
        else:
            t[s.find(lit[0])] = 0

    x1, y1, x2, y2 = end_points(kmapl, t)
    root.draw_region(x1, y1, x2, y2, color)



def main(func_TRUE, func_DC):
    n = len(get_literals(func_TRUE[0]))
    n_row = n//2
    n_column = (n+1)//2

    # print(n)

    kmapl = []
    for i in range(pow(2, n_row)):
        kmapl.append([])
        for _ in range(pow(2, n_column)): 
            kmapl[i].append(0)

    for term in func_TRUE:
        (x, y) = get_coordinate(term)
        print(f"{term} {x} {y} ")
        kmapl[x][y] = 1


    for term in func_DC:
        (x, y) = get_coordinate(term)
        print(f"{term} {x} {y} ")
        kmapl[x][y] = 'x'

    print(kmapl)
    root = kmap(kmapl)

    draw_area(root, "ac'", 'green', kmapl, n)

    root.mainloop()


# func_TRUE = ["a'bc'", "abc", "a'b'c", "a'bc"]
# func_DC = ["abc'"]

func_TRUE = ["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"]
func_DC = ["abc'd"]


# func_TRUE = ["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'",
#              "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"]
# func_DC = ["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]

print(main(func_TRUE, func_DC))
