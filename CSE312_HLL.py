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
	def __init__(self, hash_size:int, m:int, filename:str):	
		self.m = m
		self.table = np.zeros((int (np.log2(m))))
		self.constants = np.array([0.673, 0.697, 0.709])
		self.tests = np.genfromtext(filename, dtype=str)

	# TODO: implement add method
	def add(self, v: str):
		hashed_data = __hash(self, input=v)
		prev_val = self.table[hashed_data//self.m]
		if (hashed_data % m > prev_val % m):
			self.table[hashed_data//self.m] = (hashed_data % m)
			
	# TODO: implement count method
	def count(self) -> int:
		harmonic_mean = 0.0;
		for i in range(0, shape(self.table)[1]):
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
		if (shape(self.table))[1] == (shape(other.table))[1]:
			for i in range(0, (shape(self.table))[1]):
				if (other.table[i] > self.table[i]):
					self.table[i] = other.table[i] 

	# Private hashing function
	# input: str of arbitrary length
	# hash_size: the length of the hashed output
	def __hash(self, input:str):
		return (mmh3.hash(input) % int((2**(np.log2(self.m) + self.m))))	

if __name__ == '__main__':
	# TODO: add main method testing and plotting
	pass
