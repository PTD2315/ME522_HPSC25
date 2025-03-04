def test_case1():
	from mysqrtplain import mysqrtfunc
	from numpy import sqrt
	xValues=[0,2,100,10000,0.0001,1e8]
	small=1.0e-14
	for x in xValues:
		s_numpy=sqrt(x)
		s=mysqrtfunc(x)
		print(f"Value of s={s} and s_numpy={s_numpy}")
		assert(-s_numpy)<small,f"my square rood disagrees with numpy square root for x={x}"

def test_case2():
	from mysqrtplain import mysqrtfunc
	from numpy import sqrt
	xValues=[3,4,0]
	small=1.0e-14
	for x in xValues:
		s_numpy=sqrt(x)
		s=mysqrtfunc(x)
		print(f"Value of s={s} and s_numpy={s_numpy}")
		assert(-s_numpy)<small,f"my square rood disagrees with numpy square root for x={x}"
