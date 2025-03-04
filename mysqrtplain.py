def mysqrtfunc(x, debug=False):
	s=1.0
	kmax=12
	tol=1.0e-14
	for k in range(kmax):
		if(debug):
			print (f"At Iteration {k}, the value of s={s:20.15f}")
		s0=s
		s=0.5*(s+x/s)
		delta_s=s-s0
		if(abs(delta_s)/x < tol):
			break
	if(debug):
		print(f"Finally!The value of S is:{s:20.15f}")
	return s
