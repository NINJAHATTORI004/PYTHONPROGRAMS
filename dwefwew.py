with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
        for line in readfile:
            writefile.write(line)
