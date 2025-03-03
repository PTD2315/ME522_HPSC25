x=12.0
s=1.0
kmax=12
for k in range(kmax):
	print (f"At Iteration {k}, the value of s={s}")
	s=0.5*(s+x/s)
