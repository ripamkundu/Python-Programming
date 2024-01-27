import sys

def matrixChainMultiplication(dims, i, j):
	if j <= i + 1:
		return 0
	min = sys.maxsize

	'''
		(M[i+1]) × (M[i+2]………………M[j])
		(M[i+1]M[i+2]) × (M[i+3…………M[j])
		…
		…
		(M[i+1]M[i+2]…………M[j-1]) × (M[j])
	'''
	for k in range(i + 1, j):
		cost = matrixChainMultiplication(dims, i, k)
		cost += matrixChainMultiplication(dims, k, j)
		cost += dims[i] * dims[k] * dims[j]

		if cost < min:
			min = cost
	return min

if __name__ == '__main__':
	dims = [10, 30, 5, 60]
	print('The minimum cost is', matrixChainMultiplication(dims, 0, len(dims) - 1))
