from a4 import *

ones = [["abcdef'g'h'", "a'bcdefgh", "a'bc'd'e'f'gh", "a'b'cd'ef'g'h'", "abc'de'f'gh", "a'b'c'd'ef'g'h", "a'bc'd'efgh", "a'bc'defgh", "abcd'e'fg'h", "a'b'cd'e'fgh'", "a'b'cde'f'g'h'", "a'bc'd'efg'h", "a'b'cd'e'fgh", "ab'cde'f'gh'", "ab'cd'e'f'gh'", "ab'cd'e'fg'h", "a'bc'd'e'fg'h'", 'abcdefgh', "a'b'c'd'efgh", "a'b'cdef'g'h'", "a'b'c'def'g'h'", "abc'de'f'g'h", "abc'd'e'f'g'h'", "abcd'e'fgh'", "ab'cd'e'fgh'", "abc'd'efg'h'", "a'bcdefg'h", "a'bc'de'fgh'", "ab'cd'ef'gh'", "ab'c'de'f'g'h", "abc'de'fg'h", "a'bcdef'gh'", "abc'd'ef'gh'", "ab'c'defgh", "abcd'e'f'gh'", "ab'cd'efg'h", "ab'cde'fg'h'", "a'bc'de'fg'h", "a'b'cde'fgh'", "a'bcde'fg'h'", "abc'd'e'f'g'h", "a'bcdef'gh", "a'b'c'de'f'g'h'", "ab'c'd'efgh", "a'b'cdefgh", "a'bcd'e'f'g'h'", "ab'c'd'ef'gh", "a'bcd'e'f'g'h", "a'b'c'def'g'h", "a'b'cd'e'fg'h", "ab'cde'f'g'h", "a'b'c'def'gh'", "ab'c'de'fg'h'", "abcdefg'h", "abcd'ef'gh'", "a'b'cd'ef'g'h", "a'b'c'de'fg'h'", "a'b'c'd'ef'g'h'", "ab'c'def'g'h'", "a'b'c'd'ef'gh", "abc'def'g'h'", "abcdef'gh", "a'b'c'd'e'fgh'", "a'bc'def'gh", "abcde'fg'h", "a'b'cdefgh'", "ab'cdefgh", "a'bcde'f'gh", "ab'c'def'gh", "ab'cdefg'h", "a'bc'de'f'g'h", "abc'defg'h", "ab'c'de'fg'h", "ab'c'd'e'f'gh", "ab'c'd'e'fg'h"], 
        ["abc'd'ef'", "a'b'c'de'f'", "a'b'cde'f'", "abcde'f", "ab'c'd'ef'", "a'bc'd'ef'", "abcde'f'", "abcd'e'f", "abc'def'", "abcd'ef'", "a'bcd'e'f"], 
        ["abc'd'efg", "abcd'e'f'g", "abc'de'fg'", "a'bcde'fg'", "a'bcde'f'g", "abc'd'ef'g'", "abcd'e'fg'", "ab'cde'fg", "abcdef'g'", "a'b'c'de'fg'", "ab'c'd'e'f'g'", "a'b'cd'ef'g'", "a'b'cde'fg", "a'bcd'e'f'g", "abcd'ef'g'", "a'bc'de'f'g", "ab'c'de'fg'", "a'b'c'def'g", "ab'c'd'efg", "ab'c'd'e'fg", "ab'c'd'ef'g'", "a'b'c'd'e'fg", "a'bc'd'e'fg", "ab'cd'e'fg'", 'abcdefg', "abcdefg'", "abcd'e'fg", "a'bcdef'g", "a'bc'd'efg'", "a'b'cdefg", "a'bcd'efg'", "a'b'cdefg'", "ab'c'd'ef'g"], 
        ["a'b'c'd'e'f'g'h", "a'b'cde'fg'h'", "ab'cd'efgh", "a'bc'de'fgh'", "a'bcdefgh", "abc'defg'h'", "a'b'cdefgh'", "ab'cd'e'f'gh", "ab'c'd'efg'h'", "ab'c'd'e'fgh", "a'bc'def'gh", "a'b'c'd'efgh'", "a'b'c'd'ef'gh", "abcdef'gh'", "a'b'cd'ef'g'h'", "a'b'c'defgh'", "abc'de'f'g'h", "abc'defgh'", "ab'cd'efg'h'", "a'bc'de'f'g'h'", "a'bc'def'gh'", "a'b'cd'e'fg'h'", "a'b'cde'f'g'h'", "abcd'e'fgh", "abc'd'e'fgh", "a'bc'de'fg'h'", "ab'cd'e'f'gh'", "ab'c'def'g'h", "ab'cde'fg'h'", "a'b'cdefgh", "abc'de'fgh'", "a'bc'defg'h'", "a'bcd'efg'h", "ab'cdefgh'", "a'b'cde'fg'h", "a'b'cde'f'g'h", "ab'c'd'efgh'", "a'bcd'e'f'g'h", "a'bcd'e'fg'h", "abcd'e'f'g'h'", "a'bc'defg'h", "abcdef'gh", "a'bcdef'gh'", "abc'de'f'gh'", "ab'c'def'gh'", "a'b'cde'fgh", "a'b'cd'e'fgh", "a'bc'de'fg'h", "ab'cd'e'f'g'h", "abcd'e'fg'h'", "a'b'cd'e'f'g'h'", "a'b'c'd'ef'g'h'", "a'b'c'defg'h'", "abc'd'e'f'gh", "a'bcde'f'g'h'", "a'bcd'ef'gh", "a'b'cd'efgh'", "a'bc'd'efg'h'", "a'bc'defgh", "ab'cd'e'fg'h", "a'bc'def'g'h'", "abc'de'fgh", "a'bc'd'e'fgh", "a'bcd'efg'h'", "a'b'c'd'e'fg'h", "abc'de'f'gh", "abc'd'efgh", "abc'de'f'g'h'", "abc'def'g'h'", "ab'c'de'f'g'h'", "ab'c'de'f'gh"], 
        ["a'b'cd'ef", "a'bc'def"], 
        ["a'b'cde"], 
        ["abcd'e'", "a'b'c'de'", "a'bcde", "abc'de", "ab'c'de'", "a'bcd'e", "a'bc'd'e", "ab'cd'e'", "a'b'c'd'e", "ab'cde", "abc'd'e"], 
        ["a'b'cd'efg'", "ab'c'd'efg", "ab'c'de'fg'", "ab'cdefg'"], 
        ["abcde'fgh'", "a'b'c'd'e'fg'h", "a'bcde'fgh'", "a'bcde'f'g'h'", "a'b'c'd'ef'gh'", "a'b'c'def'g'h", "a'b'c'd'ef'gh", "a'bcd'ef'gh'", "abcdef'gh", "a'bc'd'e'f'g'h'", "ab'cde'fg'h'", "a'b'c'd'efgh'", "a'bcd'ef'g'h'", "a'bc'd'e'fg'h", "abc'de'fg'h'", "a'bc'd'e'fg'h'", "a'bc'defgh", "abcd'e'f'gh", "abc'de'fgh", "abcd'efgh", "ab'cde'f'g'h'", "a'bcde'f'gh", "abcde'fg'h'"], 
        ["a'bcd'efg'h'i", "ab'c'd'e'fghi", "ab'cde'f'g'h'i'", "a'b'c'de'fg'h'i'", "a'bc'de'fg'h'i'", "abcdefghi'", "a'b'c'defghi'", "a'b'cde'f'g'h'i", "abcdef'gh'i", "abcd'efgh'i", "ab'cd'efgh'i'", "ab'cd'ef'gh'i", "a'bcdefg'h'i'", "ab'c'de'fg'hi'", "a'bc'def'g'hi", "abcde'fg'h'i'", "a'bc'de'fgh'i'", "abc'de'f'g'hi", "ab'c'd'e'fg'h'i'", "ab'c'de'fgh'i'", "a'bcde'f'g'h'i'", "ab'c'd'ef'g'hi'", "a'bc'd'e'fg'hi'", "a'bcd'e'fg'hi", "a'bcde'fg'hi'", "ab'c'd'efg'h'i'", "a'bc'de'fghi'", "a'b'c'def'ghi", "a'bcdef'g'hi", "abc'de'f'ghi", "a'b'cde'fgh'i", "a'bcdef'g'h'i'", "abcde'f'g'h'i'", "abc'de'fg'h'i'", "a'b'cd'ef'g'h'i'", "a'bcdef'gh'i'", "ab'c'de'fghi", "abc'd'e'f'g'hi'", "abc'd'e'fg'h'i", "abcde'f'g'hi", "a'b'cdefgh'i'", "abc'de'fg'hi'", "a'b'cde'fghi", "a'b'c'd'e'fg'hi'", "a'bc'd'ef'gh'i'", "a'b'c'd'ef'g'h'i'", "a'b'cd'e'fg'h'i", "a'b'c'd'e'f'ghi", "abc'd'efg'h'i", "abc'def'g'h'i'", "a'b'c'd'e'f'g'hi'", "a'bcde'fg'hi", "a'b'c'd'efg'hi'", "a'b'c'd'efg'h'i'", "abc'defg'hi'"]]
dc = [["a'bcdefg'h'", "abcde'fgh'", "a'b'cde'fgh", "a'b'cdef'gh", "a'b'cde'f'gh'", "a'bc'd'e'f'g'h", "ab'cdefg'h'", "a'bc'de'fgh", "abcd'efg'h", "abcdefgh'", "ab'c'd'ef'gh'", "ab'c'defg'h'", "abcdef'gh'", "abcd'efgh'", "a'bc'de'f'gh", "a'bc'd'ef'gh'", "a'b'cde'fg'h", "a'b'c'd'e'f'gh", "a'bcd'e'fgh", "ab'c'de'f'gh", "abcd'efgh", "a'b'cdef'gh'", "a'b'cde'f'g'h", "abc'de'fgh", "a'bcd'ef'gh", "abc'd'e'fg'h'", "ab'c'd'e'fg'h'", "a'bc'def'gh'", "a'b'c'd'efg'h", "ab'c'defgh'", "abc'def'gh", "a'bc'de'f'g'h'", "a'bc'def'g'h", "abc'd'ef'gh", "abcdef'g'h", "a'bcd'ef'g'h'", "abc'defgh'", "a'b'c'defg'h'", "a'b'c'de'fg'h", "a'b'c'd'e'f'g'h'", "a'bc'd'ef'g'h", "a'b'cd'efg'h'", "abc'de'f'g'h'", "a'bcdefgh'", "a'bc'd'efg'h'", "abc'defg'h'", "a'bcde'fgh", "a'b'c'd'e'f'g'h", "a'b'cd'efgh'", "a'b'c'de'fgh'", "a'b'cd'e'fg'h'", "a'b'cd'ef'gh'", "ab'cd'ef'g'h", "a'bcd'e'fgh'", "ab'c'd'ef'g'h", "a'b'c'de'fgh", "abc'd'efgh'", "ab'cdef'g'h", "a'bc'd'e'f'g'h'", "a'b'cdefg'h", "abcde'f'gh", "ab'cd'e'fg'h'", "a'bc'defg'h", "a'b'cdef'g'h", "a'bc'd'ef'g'h'", "a'b'c'de'f'gh", "a'bc'd'e'fgh'", "a'b'c'd'e'f'gh'", "abcde'f'g'h'", "a'b'cd'efg'h", "ab'cd'ef'gh", "abc'def'gh'", "a'b'c'd'e'fg'h'", "abc'd'e'fgh'", "ab'c'defg'h", "abcde'f'gh'", "abc'defgh", "abcd'e'f'g'h'", "a'bcd'e'fg'h", "a'bc'd'ef'gh", "ab'c'de'f'gh'", "a'bcdef'g'h", "ab'cd'ef'g'h'", "a'b'c'defg'h", "a'b'c'd'e'fg'h", "abc'd'ef'g'h'"], 
      ["a'b'cd'ef'", "a'bc'de'f", "ab'cd'ef", "a'bcdef", "a'bc'def'", "ab'cde'f'", "abcd'ef", "abc'de'f'", "abcdef'", "a'b'c'd'e'f", "abc'de'f", "a'bcde'f"], 
      ["a'b'cdef'g", "a'b'c'd'e'f'g'", "a'b'cd'e'fg", "abcde'f'g", "abcde'fg", "ab'cde'f'g", "ab'cd'efg'", "a'bcdefg", "ab'cde'fg'", "a'b'c'd'efg", "a'bc'defg'", "ab'cde'f'g'", "a'bcd'e'fg", "ab'c'd'e'fg'", "abc'd'e'fg", "abc'defg'", "abcd'ef'g", "a'bcd'ef'g'", "ab'c'de'fg", "ab'c'd'efg'", "a'bcd'e'fg'", "a'bcd'efg", "a'bc'de'fg'", "abc'defg", "a'b'cde'fg'", "abc'd'e'f'g", "abc'de'f'g", "ab'c'def'g'", "a'bc'def'g", "a'bc'd'e'fg'", "a'b'cd'efg'", "a'bcd'e'f'g'"], 
      ["a'bcde'fg'h", "abcde'fgh'", "a'b'c'def'g'h'", "abcd'e'f'gh'", "abcd'ef'g'h'", "ab'cdef'g'h'", "a'bcd'e'f'gh", "a'bcd'e'fgh", "a'bc'def'g'h", "a'b'c'd'e'f'gh", "a'b'cd'ef'g'h", "ab'cd'e'fg'h'", "abcdefgh'", "ab'c'de'f'g'h", "abcd'e'fg'h", "abc'd'efg'h", "ab'cde'f'gh", "a'b'c'de'fg'h'", "a'b'c'd'ef'gh'", "ab'c'd'e'fg'h'", "a'b'c'de'fgh", "a'b'cdef'gh'", "ab'cde'f'gh'", "abcd'ef'gh'", "ab'cde'fg'h", "ab'cd'e'fgh", "abcd'efg'h'", "ab'c'defgh", "a'bc'd'e'fg'h", "a'bcde'f'g'h", "ab'cd'efg'h", "abc'defgh", "ab'cd'efgh'", "ab'c'def'g'h'", "a'b'c'def'gh'", "a'bc'd'efg'h", "a'bcd'e'f'g'h'", "abc'd'e'fg'h'", "a'b'cde'f'gh'", "abcd'e'f'gh", "a'bcd'efgh'", "a'b'c'de'fg'h", "ab'c'def'gh", "a'b'c'd'e'f'g'h'", "a'b'cd'e'f'g'h", "a'bcd'ef'gh'", "abcdef'g'h'", "ab'cdefg'h'", "a'bcde'f'gh'", "ab'c'd'efgh", "abcdefg'h", "abc'd'e'f'gh'", "ab'c'd'ef'gh'", "a'bcdefg'h'", "a'bc'd'e'fg'h'", "ab'c'd'e'f'gh'", "a'b'cd'e'fgh'", "abc'de'fg'h'", "ab'c'defgh'", "a'b'cd'efg'h", "a'bc'd'efgh", "ab'cd'ef'g'h", "a'bc'defgh'", "ab'c'de'fg'h'", "ab'c'd'ef'g'h'", "ab'cd'ef'gh", "a'bc'd'efgh'", "abc'd'ef'gh", "a'b'c'de'f'g'h'", "abc'defg'h", "a'b'c'd'ef'g'h", "ab'cdefgh", "ab'cde'fgh", "abcdef'g'h", "a'b'cd'efgh", "a'bcdefg'h", "abcd'e'f'g'h", "a'b'cd'ef'gh", "a'bc'de'f'gh"], 
      ['abcdef', "abc'def'", "a'bcd'e'f'", "ab'c'de'f", "abcd'ef'", "abcde'f", "ab'cd'e'f'"], 
      ["a'b'c'de'", "a'bc'd'e'", "a'bc'd'e"], 
      ["abcde'", "ab'c'd'e'", "abc'd'e'", "abcd'e", "a'bcde'", "ab'c'de", "a'bcd'e'", "ab'cd'e", "a'b'cd'e'", "a'b'c'de", "a'b'cd'e"], 
      ["ab'c'de'f'g", "a'bc'd'ef'g"], ["abc'd'e'f'g'h'", "a'bcdef'g'h", "a'bc'de'f'g'h'", "a'bcd'efg'h", "abc'd'ef'g'h'", "a'b'cde'fgh", "a'b'c'defg'h", "ab'c'd'efg'h'", "ab'c'd'e'fgh'", "abcd'e'f'g'h'", "ab'cdefgh'", "a'bcde'f'g'h", "a'bc'd'ef'gh'", "a'bcde'f'gh'", "ab'cd'e'f'g'h", "a'bc'defg'h", "a'bc'd'e'fgh'", "ab'c'de'fg'h", "a'bc'd'e'f'gh'", "abc'd'e'fg'h", "a'bc'defg'h'", "ab'cd'efgh", "abc'defg'h'"], 
      ["abcd'ef'gh'i'", "ab'c'de'f'ghi'", "a'b'c'd'e'fgh'i'", "a'bc'd'e'fg'h'i'", "abcd'e'fg'hi'", "a'bc'defg'hi'", "a'b'cde'f'g'hi'", "abc'd'e'fg'h'i'", "abc'defghi", "a'bc'd'e'f'g'h'i'", "abc'd'e'fghi", "ab'c'd'ef'g'h'i", "abcd'ef'g'h'i", "ab'c'd'e'f'ghi", "ab'cde'f'g'hi", "abc'de'f'ghi'", "ab'c'de'f'gh'i'", "a'b'cd'e'f'g'hi", "a'b'c'de'fgh'i'", "ab'c'd'e'f'g'hi", "a'bc'd'efgh'i'", "a'b'c'd'ef'ghi'", "abcde'fghi'", "a'bc'd'ef'g'h'i", "a'bcd'e'fghi'", "ab'cde'f'gh'i'", "a'bc'def'gh'i", "a'bcd'e'f'g'h'i'", "a'bcdefg'h'i", "a'bcd'e'f'g'hi'", "a'b'c'd'e'fgh'i", "a'bc'de'fg'hi'", "ab'c'defgh'i", "a'bcde'f'g'hi'", "a'bc'd'e'f'g'hi'", "a'b'c'd'e'fg'h'i", "a'bc'de'f'ghi", "a'b'c'd'e'fghi", "abc'd'efgh'i", "abc'd'ef'g'h'i", "a'bcd'efg'h'i'"]]

sol = [56,6,19,34,2,1,6,4,16,40]

l = len(ones)
score = 0
for i in range(l):
  ans = opt_function_reduce(ones[i], dc[i])
  mysol = len(ans)
  print(ans)
  print(mysol)
  score += sol[i]-mysol

print("Your score is: ", score)
