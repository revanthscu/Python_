import emp,pickle
with open('emp.dat','rb') as f:
    print('unpickling in progress.....')
    while True:
        try:
            for i in range(1000):
                i=pickle.load(f)
                i.display()
        except EOFError:
            print('all objects unpickled')
            break

f.close()
