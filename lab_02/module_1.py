f = open("example.txt", 'r')
for line in f:
    print(line, end = ' ')
f.close()

f = open("writeTo.txt", 'w')
f.write("I wrote this line using Python!")
f.close()

# f = open("random.txt", 'r')
# for line in f:
#     print(line, end = ' ')
# f.close()

# d_path = 'random.txt'
# d_n_path = 'new_random.txt'
# with open(d_path, 'r') as reader, open(d_n_path, 'w') as writer:
#     random = reader.readlines()
#     writer.writelines(random)

with open('names.txt', 'r') as reader, open('new_names.txt', 'w') as writer:
    newNames = ''
    names = reader.readlines()
    for line in names:
            newNames = line + newNames
    writer.writelines(reversed(newNames))               
            
        
        
                    
        
        




    
  

    
        
             
