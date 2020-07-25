from collections import defaultdict

def run():
	Q, N = map(int, input().strip().split())
	parent = list(range(N))
	rank = [0]*N

	root_stack = []

	g = defaultdict(list)


	def find(u):
		while parent[u] != u:
			u, parent[u] = parent[u], parent[parent[u]]
		return u


	def union(u, v):
		uroot = find(u)
		vroot = find(v)
		if uroot == vroot:
			return uroot, vroot, 0
		if rank[uroot] < rank[vroot]:
			uroot, vroot = vroot, uroot

		parent[vroot] = uroot
		urank = rank[uroot]
		if rank[uroot] == rank[vroot]:
			rank[uroot] += 1
		return uroot, vroot, urank


	res_stack = [N]

	for _ in range(Q):
		queries = input().strip().split()
		if len(queries) > 1:
			u, v = map(int, queries[1:])
			u = int(u)-1
			v = int(v)-1
			uroot, vroot, urank = union(u, v)
			if uroot != vroot:
				res_stack.append(res_stack[-1]-1)
			else:
				res_stack.append(res_stack[-1])
			root_stack.append((uroot, vroot, urank))
			print(res_stack[-1])
		else:
			cur_res = res_stack[-1]
			res_stack.pop()
			uroot, vroot, urank = root_stack.pop()
			print(res_stack[-1])
			if cur_res != res_stack[-1]:
				parent[vroot] = vroot
				rank[uroot] = urank

run()