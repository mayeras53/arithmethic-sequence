# 5 + 7 + 9 + ... + p = 525
# sn = 525
# a = 5
# u2 = 7

sn = int(input("Sn = "))
a = int(input("a = "))
u2 = int(input("U2 = "))
b = u2 - a
 
for n in range(1, 100):
 
    if sn == n/2 * (a + (a+(n - 1)*b)):
        print("\nn = ",n)
 
        p = a + (n - 1)*b
        print("p = ",p)

#@mayer.py