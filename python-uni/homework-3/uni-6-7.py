import random 
import math
# import numpy

# =============================================================================
# # 6
# 
# arr = []
# summ = 0
# 
# for i in range(5):
#     a = []
#     
#     for j in range(5):
#         a.append(random.randint(0, 10))
#     
#     arr.append(a)
# 
# 
# # # a
# # for i in range(5):
# #     summ +=arr[i][i]**2
#     
# # print(math.sqrt(summ))
# 
# 
# 
# # b
# # sum2 = sum(x for x in numpy.transpose(arr)[1] )
# # sum1 = sum(x for x in arr[2] )
# 
# sum1 = 0
# sum2 = 1
# for i in range(5):
#     sum1 +=arr[2][i]
#     sum2 *=arr[i][1]
#         
# print(sum1 - sum2)
# =============================================================================


# 7

arr = []

myDict = {}

for i in range(10):
    arr.append(random.sample(range(1, 500), 10)) 
        
for i in range(len(arr)):
    for j in range(len(arr[i])):
        try:
            myDict[arr[i][j]] += 1
        except KeyError:
            myDict[arr[i][j]] = 1
            
max_value = max(myDict.values())
max_keys = [k for k, v in myDict.items() if v == max_value]
        
print(max_keys, max_value)