# Authors: Vikram Guhan Subbiah, Alexander Hughes
# Date: 13th August 2020
# Course: CSE 312 20su
# Title: Final Project
# Instructor: Alex Tsun

# HyperLogLog
# ---------------------
# A data structure to count distinct elements
# with higher efficiency using a low amount of
# vairance.
# ---------------------

# Import statements
import numpy as np
import matplotlib.pyplot as plt
import mmh3

# HyperLogLog 
class Hll312:
	def __init__(self, m:int):	
		self.m = m
		self.table = np.zeros((int (np.log2(m))))
		self.constants = np.array([0.673, 0.697, 0.709])
		self.hash_limit = int((2**(np.log2(self.m)+self.m)))

	def add(self, v: str):
		hashed_data = self.hash(v) 
		prev_val = self.table[int(np.log2(hashed_data//(2**self.m) + 1)) - 1]
		if (hashed_data % (2**self.m) > prev_val % (2**self.m)):
		    	self.table[int(np.log2(hashed_data//(2**self.m) + 1)) - 1] = (hashed_data % self.m)
			
	def count(self) -> int:
		harmonic_mean = 0.0
		for i in range(0, self.table.shape[0]):
			harmonic_mean = 2**(-self.table[i])

		harmonic_mean = harmonic_mean**(-1)

		if (self.m//16 <= 1):
			return int(self.constants[0]*(self.m**2)*harmonic_mean)
		elif (self.m//32 <= 1):
			return int(self.constants[1]*(self.m**2)*harmonic_mean)
		elif (self.m//64 <= 1):
			return int(self.constants[2]*(self.m**2)*harmonic_mean)
		else:
			constant = (0.7213)/(1 + 1.079/self.m)
			return int(constant*(self.m**2)*harmonic_mean)

	def merge(self, other):
		if (self.table.shape[0]) == (other.table.shape[0]):
			for i in range(0, (self.table.shape[0])):
				if (other.table[i] > self.table[i]):
					self.table[i] = other.table[i] 

	def hash(self, input:str):
		return ((int(mmh3.hash(str(input), signed=False)))%self.hash_limit)

if __name__ == '__main__':
	print("Generating data set")
	test = np.genfromtxt('stream_small.txt', delimiter='\n', dtype=str)
	control = set([])

	# Initialise numpy arrays
	control_res = np.zeros(15)
	exp_res = np.zeros(15)
	indp = np.arange(15)
	indp += 1

	# Control results
	for j in range (0, test.shape[0]):
		control.add(test[j])

	# HLL results
	for i in range (1, 15):
		testhll = Hll312(m=i)
		for j in range (0, test.shape[0]):
			testhll.add(test[j])
		exp_res[i] = testhll.count()
		control_res[i] = len(control)

	# Plot lines
	plt.plot(indp, exp_res, "r", label="HLL", linestyle="-")
	plt.plot(indp, control_res, "black", label="Control", linestyle="-.")
	
	# Format plot
	plt.title("CSE 312 stream_small test results")
	plt.legend(loc="upper left")
	plt.xlabel("m")
	plt.ylabel("Distinct elements")

	# Save plot
	plt.savefig('test1.png')
