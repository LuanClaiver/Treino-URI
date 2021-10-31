parent = [0] * 200000
def init(m):
	for i in range(m):
		parent[i] = i
		
def find(v):
	if parent[v] == v:
		return v
	
	parent[v] = find(parent[v])
	return parent[v]

def union(u, v):
	a, b = find(u), find(v)
	
	if a != b:
		parent[a] = b

while True:
	m, n = [int(x) for x in input().split()]

	if m == n == 0:
		break
	
	init(m)
	somaTotal = 0
	lista = []
	
	for i in range(n):
		x, y, z = [int(a) for a in input().split()]
		somaTotal += z
		lista.append((z,x,y))
		
	lista.sort()
	somaMinima = 0
	
	for a, b, c in lista:
		p = find(b)
		q = find(c)
		
		if p != q:
			union(p, q)
			somaMinima += a
		
	print(somaTotal - somaMinima)

