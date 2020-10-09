import random 

myDict = { key : random.randint(100, 9999) for key in range(1000) }



# 1 

# =============================================================================
# # ა
# count500 = 0
# 
# 
# for key in myDict:
#     if myDict[key] == 500:
#         count500 += 1
#     
#     
# print(count500)
# =============================================================================


# =============================================================================
# # ე
# 
# unique_numbers = set(myDict.values())
#     
# print(unique_numbers)
# =============================================================================


# =============================================================================
# # ვ
# 
# numSum = 0
# numCount = 0 
#  
# for key in myDict:
#    if str(myDict[key]) == str(myDict[key])[::-1] :
#        numCount += 1
#        numSum += myDict[key]
# 
# 
# print(numSum / numCount)         
# =============================================================================


# =============================================================================
# # ზ
# 
# countno57 = 0
# 
# for key in myDict:
#     if str(myDict[key]).find('5') == -1 and  str(myDict[key]).find('7') == -1 :
#         countno57 += 1
#         
# print(countno57)
# 
# =============================================================================


# =============================================================================
# # თ
# samenums = 0
# 
# for key in myDict:
#     myarr = list( str(myDict[key]) )
#     for i in myarr:
#        if myarr.count(i) > 1:
#            samenums += 1
#            
# print(samenums)
# =============================================================================

# =============================================================================
# # ი 
# 
# countoddpols = 0
# 
# for key in myDict:
#     mystr = str(myDict[key])[::2]
#     if mystr == mystr[::-1]:
#         countoddpols += 1
#         
# print(countoddpols)
# =============================================================================
        
        
# =============================================================================
# # კ
# 
# sortedcount = 0
# 
# for key in myDict:
#     flag = True
#     myarr = list( str(myDict[key]) )
#     if int(myarr[0]) >= int(myarr[-1]) :
#         for i in range( len(myarr) - 1 ):
#             if myarr[i] < myarr[i+1]:
#                 flag = False
#                 break
#     else:
#         for i in range( len(myarr) - 1 ):
#             if myarr[i] > myarr[i+1]:
#                 flag = False
#                 break
#     if flag :
#        sortedcount += 1
#        
# print( sortedcount )
# =============================================================================
            
        
        
        
        
        
        
        
        
        