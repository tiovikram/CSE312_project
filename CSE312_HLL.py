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
	# TODO: Add default m value and filename
	def __init__(self, m:int):	
		self.m = m
		self.table = np.zeros((int (np.log2(m))))
		self.constants = np.array([0.673, 0.697, 0.709])
	
	# TODO: implement add method
	def add(self, v: str):
		hashed_data = hash(v)
		prev_val = self.table[hashed_data//self.m]
		if (hashed_data % m > prev_val % m):
			self.table[hashed_data//self.m] = (hashed_data % m)
			
	# TODO: implement count method
	def count(self) -> int:
		harmonic_mean = 0.0;
		for i in range(0, self.table.shape[0]):
			harmonic_mean = 2**(self.table[i])

		if (m//16 <= 1):
			return int(self.constants[0]*(self.m**2)*harmonic_mean)
		elif (m//32 <= 1):
			return int(self.constants[0]*(self.m**2)*harmonic_mean)
		elif (m//64 <= 1):
			return int(self.constants[0]*(self.m**2)*harmonic_mean)
		else:
			constant = (0.7213)/(1 + 1.079/self.m)
			return int(constant*(self.m**2)*harmonic_mean)

	# TODO: implement merge method
	def merge(self, other):
		if (self.table.shape[0]) == (other.table.shape[0]):
			for i in range(0, (self.table.shape[0])):
				if (other.table[i] > self.table[i]):
					self.table[i] = other.table[i] 

	# input: str of arbitrary length
	# hash_size: the length of the hashed output
	def hash(self, input:str):
		print("Hash limits: " + str(int((2**(np.log2(self.m) + self.m)))))
		return (mmh3.hash(input, signed=False) % int((2**(np.log2(self.m) + self.m))))

if __name__ == '__main__':
	# TODO: add main method testing and plotting
	tests = np.genfromtxt('stream_small.txt', dtype=str)
	hll = Hll312(m=16) 

	for i in range(0, tests.shape[0]):
		hll.add(v=tests[i])

	print("Total Elements: " + str(hll.count))
