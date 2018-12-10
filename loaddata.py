with open('kargerMinCut.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)
data = [[int(x) for x in line[0:-1]] for line in d]



data = np.loadtxt('QuickSort.txt')
P = data.tolist()


with open(fname) as f:
    content = f.readlines()
    
    
with open("C:/Users/kenzo/Desktop/output04.txt") as f:
        content = f.readlines() 
output =  [list(map(int, x.rstrip().split())) for x in content[:]]
output = [x[0] for x in output]