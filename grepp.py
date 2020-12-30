import fileinput
import os

#print(os.getcwd())
word = input()
print(word)
filen =[]
dirfi= []
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    '''
    print('current path:', dirpath)
    print('directories:',dirnames)
    print('files', filenames)
   '''
    for j in filenames:
         filen.append(j)
         dirfi.append(os.path.join(dirpath,j))
    print()

for  i  in dirfi: 
    with open(i,'r')as f: 
        for line in f: 
            if word in line: 
                print(i,": ",line,end='') 
                