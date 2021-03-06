# Name: Dinh Nguyen
# CS260 Summer 2020
import math
# initialize data/data structure
x_values = [1, 2, 4, 8, 16, 32, 64]
f_values = [[],[],[],[],[],[],[],[],[],[],[],[]]

# calculation
for x in x_values:
    f_values[0].append(x**3)                        #f1
    f_values[1].append(math.log2(x))                #f2
    f_values[2].append(x * math.log2(x))            #f3
    f_values[3].append((3.0 / 2.0) ** x)            #f4
    if math.log2(x) != 0:
        f_values[4].append(x / (math.log2(x)))      #f5
        f_values[7].append(math.log2(math.log2(x))) #f8
    else:
        f_values[4].append(float('inf'))
        f_values[7].append(float('-inf'))

    f_values[5].append(2 ** x)                      #f6
    f_values[6].append(math.sqrt(x))                #f7
    f_values[8].append(x ** 2)                      #f9
    f_values[9].append(x)                           #f10
    f_values[10].append((math.log2(x)) ** 2)        #f11
    f_values[11].append((1.0 / 3.0) ** x)           #f12

#printing output
for i in range(0,12):
    print("\nx\tf{:d}".format(i+1))
    for k in range(0,len(x_values)):
        print("{:2d}\t{}".format(x_values[k],f_values[i][k]))
