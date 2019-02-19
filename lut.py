import math

def DtoB(num, k):
	binary = ""
	Integer = int(num)
	fractional = num - Integer
	if Integer == 0:
		binary = '0.'
	else:
		while(Integer):
			rem = Integer%2
			binary = binary + str(rem)
			Integer = Integer //2
	
		binary = binary[ : : -1]
		binary = binary + '.'
	
	while(k):
		fractional = fractional*2
		f_bit = int(fractional)
		if (f_bit == 1):
			fractional = fractional - f_bit
			binary = binary+'1'
		else:
			binary = binary + '0'
		k = k-1
		
	return binary
	
def BtoD(binary,length):
	
	point = binary.find('.')
	
	intDecimal = 0
	intFractional = 0
	twos = 1
	
	for i in range(point-1, -1, -1):
		intDecimal = intDecimal + ((ord(binary[i])-ord('0'))*twos)
		twos = twos*2
		
	twos = 2
	
	for i in range(point+1, length):
		intFractional = intFractional + ((ord(binary[i])-ord('0'))/twos)
		twos = twos*2
	
	out = intDecimal + intFractional
	
	return out

def sigmoid(x):
	return 1 / (1+math.exp(-x))

sum=0

for x in range(-128,128):
	y = sigmoid(x)
	if y > 0.998:
		y_app = 1.0
	elif y > 0.9921875:
		y_app = 0.9921875
	elif y > 0.0078125:
		y_app = y
	elif y > 0.006:
		y_app = 0.0078125
	else :
		y_app =0 
	#diff = (y-y_app)*(y-y_app)
	#sum = sum+diff
	out = DtoB(y_app,7)
	p = BtoD(out,len(out))
	diff = (y-p)*(y-p)
	sum = sum+diff
	
	print('mem[',x,'] = ',out,';')
	
MSE = sum/256
print(MSE)
	

	
