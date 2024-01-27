input = 'Sarma/ Sen/ Ram; Kumar/ Hari; Roy/ Koushik'

# output = {3: ['Ram Sen Sarma'], 2: ['Hari Kumar', 'Koushik Roy']}

n = [name.strip() for name in input.split(';')]
g = {}
for name in n:
    p = name.split('/')
    count = len(p)
    p = p[::-1]
    n_str = ' '.join(p)
    if count not in g:
        g[count] = []
    # s = n_str[::-1]
    g[count].append(n_str) 
    # s = dict(sorted(g.items), reverse = True)
    
# output = sorted([(count , n) for count, n in g.items()], reverse=True)
output = {count : n for count, n in g.items()}
# s = dict(reversed(output.items()))

print("Output : ", output)
    

