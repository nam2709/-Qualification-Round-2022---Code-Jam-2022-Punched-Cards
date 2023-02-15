import random
T = int(input())
for v in range(0,T):
	E, D  = input().split()
	C = int(D)
	R = int(E)
	# join the list to string

	print('Case #' + str(v+1) + ':')
	a = '+-'
	ae = [a for m in range (1,C)]
	ae_str = ''.join(ae)

	print('..'+ae_str+'+')


	b = '.'
	be = [b for m in range (1,C)]
	be_str = '|'.join(be)

	print('..|'+be_str+'|')
	c = '.'
	c_str =''.join(c)

	print('+-'+ae_str+'+')


	a = '+-'
	am = [a for m in range (1,C+1)]
	am_str = ''.join(am)



	t = '.'
	t_str =''.join(t)

	for e in range (1,R):
		ar =[t_str for i in range (1,C+1)]
		ar = '|'.join(ar)


		print('|' + ar ,end = '|' + '\n' + am_str + '+' + '\n')
		



