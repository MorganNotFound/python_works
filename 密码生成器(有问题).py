__import__('random')
passlen = int(input("enter the length of password"))
s = " abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKL MNOPQRSTUVIXYZ!aN$x*6*( )?"
p = ".join(random.sample(s,passlen ))"
print(p)
