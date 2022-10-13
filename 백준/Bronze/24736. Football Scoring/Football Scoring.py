T, F, S, P, C = map(int, input().split())
t, f, s, p, c = map(int, input().split())

A = (T* 6) + (F* 3) + (S* 2) + (P* 1) + (C* 2)
B = (t* 6) + (f* 3) + (s* 2) + (p* 1) + (c* 2)
print(A, B)
