from K_map_gui_tk import *
import time

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
    if n < 1: g = []
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
    return g

def get_coordinate(term):
    literals = list(get_literals(term))
    n = len(literals)
    n_row = n//2
    n_column = (n+1)//2

    l_row = gray_code(n_row)
    l_column = gray_code(n_column)
    row_literal = literals[n_column:]
    col_literal = literals[0:n_column] 

    s1 = ""; s2 = ""

    for lit in row_literal:
        if(len(lit) == 1): s1+='1'
        else: s1+='0'
    for lit in col_literal:
        if(len(lit) == 1): s2+='1'
        else: s2+='0'

    return (l_row.index(s1), l_column.index(s2))

def merge(term1, term2):
    
    t1 = set(get_literals(term1))
    t2 = set(get_literals(term2))
    x = list(t1-t2)
    y = list(t2-t1)
    if (len(x) == 1) and (len(y) == 1):
        if x[0] in str(y[0]) or y[0] in str(x[0]):
            ls = list(t1-set(x))
            ls.sort()
            return (True, "".join(ls))
    return (False, "")

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

def combinations(comb, c, list):
    if c==0:
        s = "abcdefghijklmnopqrstuvwxyz"
        t = ""
        for i in range(len(list)):
            t += s[i]
            if(list[i]==0):
                t+="'"
        comb.append(t)
        return

    for i in range(len(list)):
        if list[i] == -1:
            list[i]=0
            combinations(comb, c-1, list.copy())
            list[i]=1
            combinations(comb, c-1, list.copy())


def demo(n, term):
    literals = get_literals(term)
    new_literals = []
    s = "abcdefghijklmnopqrstuvwxyz"
    flag = True

    list  = [-1 for i in range(n)]
    for lit in literals:
        if flag:
            flag=False
            if(len(lit) == 2):
                list[s.find(lit[0])] = 1
            else:
                list[s.find(lit[0])] = 0
        else: 
            new_literals.append(lit)
            if(len(lit) == 1):
                list[s.find(lit[0])] = 1
            else:
                list[s.find(lit[0])] = 0

    comb=[]
    combinations(comb, n-len(literals), list.copy())

    print(f"N = {n}")
    print(f"Current term expansion: {term}")
    print(f"Next Legal Terms for Expansion: {comb} ")

    ans = "".join(sorted(set(new_literals)))
    if(len(new_literals)==0): print("Expanded Term: \"1\"")
    else: print(f"Expanded Term: {ans}")

def legal_term_list(n, term):
    literals = get_literals(term)
    new_literals = []
    s = "abcdefghijklmnopqrstuvwxyz"

    list  = [-1 for _ in range(n)]
    for lit in literals:
        new_literals.append(lit)
        if(len(lit) == 1):
            list[s.find(lit[0])] = 1
        else:
            list[s.find(lit[0])] = 0

    comb=[]
    combinations(comb, n-len(literals), list.copy())
    return comb

def comb_function_expansion(func_TRUE, func_DC):
    """
        determines the maximum legal region for each term in the K-map function
        Arguments:
            func_TRUE: list containing the terms for which the output is '1'
            func_DC: list containing the terms for which the output is 'x'
        Return:
            a list of terms: expanded terms in form of boolean literals
    """
    
    # when 1 kmap will be shown
    kmap_on = 0

    n = len(get_literals(func_TRUE[0])) 
    n_row = n//2
    n_column = (n+1)//2

    if kmap_on:
        kmapl = []
        for i in range(pow(2, n_row)):
            kmapl.append([])
            for _ in range(pow(2, n_column)): 
                kmapl[i].append(0)
        for term in func_TRUE:
            (x, y) = get_coordinate(term)
            kmapl[x][y] = 1
        for term in func_DC:
            (x, y) = get_coordinate(term)
            kmapl[x][y] = 'x'

        if kmap_on: root = kmap(kmapl)
        colors = ['green', 'blue', 'red', 'yellow', 'lightgray', 'cyan', 'pink', 'beige', 'plum']

    # x is list of sets
    x = []
    x.append(set(func_TRUE+func_DC))
    for i in range(n):
        ls = set(); m = len(x[i])
        for j in range(m):
            for k in range(j+1, m, 1):
                t1 = list(x[i])[j]
                t2 = list(x[i])[k]
                possible, merged = merge(t1, t2)
                if possible:
                    ls.add(merged)
        x.append(ls)

    best = []
    areas_marked = []; c=0
    for t1 in func_TRUE:
        done = False
        for i in range(n, -1, -1) :
            if done: 
                    break
            for t2 in x[i]:
                if done: 
                    break
                term2 = set(get_literals(t2))
                if term2.issubset(set(get_literals(t1))) and not done:
                    term2 = list(term2)
                    term2.sort()
                    best.append("".join(term2))
                    if (t2 not in areas_marked) and kmap_on:
                        areas_marked.append(t2)
                        draw_area(root, t2, colors[c], kmapl, n)
                        c+=1
                    done = True
                    break

    # # this shows the terms and the list of terms from which it is formed
    # for term in best:
    #     lis = legal_term_list(n, term)
    #     print(f"term: {term} list: {lis}")

    if kmap_on: root.mainloop()
    return best

# func_TRUE = ["a'b", "ab'"]
# func_DC = ["ab"]

# func_TRUE = ["a'bc'", "abc", "a'b'c", "a'bc"]
# func_DC = ["abc'", "ab'c"]

# func_TRUE = ["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"]
# func_DC = ["abc'd"]

# func_TRUE = ["a'bc'd'", "ab'cd'", "a'b'cd", "a'bcd"]
# func_DC = ["abc'd", "abcd'", "abcd"]

# func_TRUE = ["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'",
#              "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"]
# func_DC = ["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]

# func_TRUE = ["a'b'c'd'e'", "a'bc'd'e'", "abc'd'e'", "ab'c'd'e'", "abc'de'", "abcde'",
#              "a'bcde'", "a'bcd'e'", "abcd'e'", "a'bc'de", "abc'de", "abcde",
#              "a'bcde", "a'bcd'e", "abcd'e", "a'b'cd'e", "ab'cd'e"]
# func_DC = []

# print(f"func_TRUE: {func_TRUE} \nfunc_DC: {func_DC}")
# best = comb_function_expansion(func_TRUE, func_DC)
# print(f"ANS: {best}")
# print(f"Legal Regions: {set(best)}")