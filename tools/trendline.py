#!/usr/bin/env python
'''trendline.py
takes a single two-dimensional numpy array as input and 
returns a tuple of slope and y-intercept values generated by linear 
regression/gradient descent with auto-selected learning rate alpha
based on precision defined as prec 
'''
prec = .0001

import numpy as np
import time
start_time = time.time()
#-------start functions---------#
def th0_sum(th0,th1,x,y):		#gradient sum of partial derivatives wrt th0
	return sum([th0+th1*x[i]-y[i] for i in range(len(x))])
	
def th1_sum(th0,th1,x,y):		#gradient sum of partial derivatives wrt th1
	return sum([( th0+th1*x[i]-y[i] )*x[i] for i in range(len(x))])
	
def J_sum(th0,th1,x,y):			#J(cost) sum for squared residuals
	return sum([ (th0+th1*x[i]-y[i])**2 for i in range(len(x))])
	
def compute_trendline(alpha,th0,th1,prec,x,y):
	th0_tmp=0.
	m=xy_length
	J_new=0.;J_old=0.
	grad_iter = 1
	
	while 1:
		th0_tmp=th0-alpha/m*th0_sum(th0,th1,x,y)
		th1=th1-alpha/m*th1_sum(th0,th1,x,y)
		th0=th0_tmp
		J_old=J_new
		J_new=1./(2*m)*J_sum(th0,th1,x,y)
		if J_new > (J_old+1000000):
			return 'high'
		diff=J_new-J_old
		grad_iter+=1
		if abs(diff) < prec:	#cost is minimized
			print 'gradient iterations:',grad_iter
			return th0,th1,grad_iter

#------get_trendline------#		
def get_trendline(xy_array):	#xy_array is np.array

	x = xy_array[:,0]
	y = xy_array[:,1]
	global xy_length 
	xy_length = len(xy_array)	
		#-----measure axis with largest range-----#	
	
		#-----get starting parameters-----#					
	th1 = 1.*(y[-1] - y[0])/(x[-1]-x[0])	# m=(y2-y1)/(x2-x1)
	th0 = y[0]-th1*x[0]										# b = y-mx
	alpha=.1
	alpha_iter=1	#track total iterations to finding alpha that promotes J convergence
	
	while 1:		#auto-generate alpha value
		result=compute_trendline(alpha,th0,th1,prec,x,y)	
		if result == 'high':
			alpha=alpha*9./10		#no convergence in J; reduce alpha
			alpha_iter+=1
		else:
			th0=int(100*result[0])/100.
			th1=int(100*result[1])/100.
			grad_iter=result[2]
			break
	elapsed_time = 1000./(time.time()-start_time),'s'
	return th0,th1

def main():
	pass
	
if __name__ == '__main__':
	main()