import itertools
U = {1,2,3,4,'a','b','c','d','ee','tt','ww'}
A = {1,2,'ee','a','d'}
B = {'d','ee',4,3}
F = ((A^B)&(A|B))
C1 = {(a,b) for a, b in itertools.product(A,B)}
C2 = {(b,a) for b, a in itertools.product(B,A)}
print("Об'єднання А та В:", A|B, "\nПеретин А та В:",  A&B, "\nРізниця А і В:", A-B,"\nРізниця В і А:", B-A, "\nСиметрична різниця А та В:", A^B, "\nДоповнення А:",U-A, "\nДоповнення В:",U-B)
print("Декартовий добуток АхВ:", C1, "\nДекартовий добуток ВхА: ", C2, "\nМножина F за формулою: ", F)