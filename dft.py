import scipy
import numpy
import matplotlib.pyplot as plt

#test comment
 
def random_data_creation():
	random_numbers = random.random(range(1000), 100)
	return (random_numbers)
	
def periodic_function():
	T = 0
	periodic_function_form = []
	while (T<1000):
		periodic_function_form.append(numpy.sin(T*((numpy.pi)/20))+(numpy.sin(T*((numpy.pi)/50))))
		T = T+1
		
	return (periodic_function_form)	

def main():
	data = periodic_function()
	data_length = len(data)
	x_im = []
	x_re = []

	n = 0
	k = 0
	container = 0
	container_2 = 0
	
	while (n<data_length):
		while (k<data_length):
			container = container + data[k]*numpy.cos(2*numpy.pi*k*n/1000)
			k = k+1
		x_re.append(container)
		container = 0
		k = 0
		n = n+1
	
	n=0
	k=0
	while (n<data_length):
		while (k<data_length):
			container_2 = container_2 - data[k]*numpy.sin(2*numpy.pi*k*n/1000)
			k = k+1
		x_im.append(container_2)
		container_2  = 0
		k = 0
		n = n+1
		
	i=0
	container_3 = 0
	amplitudes = []
	while (i<1000):
		container_3 = numpy.sqrt((x_im[i]*x_im[i] + x_re[i]*x_re[i]))
		amplitudes.append(container_3/1000)
		i = i+1
		container_3 = 0
	
	plt.plot(data)
	plt.plot(amplitudes)
	plt.show()	
		
main()	
	
