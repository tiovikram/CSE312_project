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

# HyperLogLog 
class Hll312():
	# TODO: Add default m value and filename
	def __init__(self, hash_size:int, m:int, filename:str):	
		self.hash_size = hash_size
		self.m = m
		self.table = np.zeros(shape((int)np.log2(m), m))
		self.tests = np.genfromtext(filename, dtype=str)

		self.bucket_bitmap = np.concatenate((np.ones(shape(hash_size), np.zeros(shape(m)), axis=None)
		self.value_bitmap = np.logical_not(self.bucket_bitmap)

	# TODO: implement add method
	def add(self, v: str):
		hashed_data = __hash(input=v, hash_size=self.hash_size)
		bucket = np.logical_and(hashed_data, self.bucket_bitmap)
			
	# TODO: implement count method
	def count(self) -> int:

	# TODO: implement merge method
	def merge(self, other:Hll312):

	# Private hashing function
	# input: str of arbitrary length
	# hash_size: the length of the hashed output
	# return: an 1-dimensional array of m boolean elements
	def __hash(input:str, hash_size:int):

if __name__ == '__main__':
	# TODO: add main method testing and plotting
