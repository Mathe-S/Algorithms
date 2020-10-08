alfa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t', 'u',
 'v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ','\t','\n', '.' , ',' ]
import random
N = 10000
st = ''.join([random.choice(alfa) for i in range(N)])

# 1 
st1 = st.split(".")
# 6
str2 = []
for k in st1:
    k = k.split("\t")
    for i in k:
        i = i.split("\n")
        str2.extend(i)


# 8

# =============================================================================
# # a
# for j in str2:
#     if j.isdigit():
#         modInt = list(j)
#         modInt = [int(i) for i in modInt] 
#         print( max(modInt)**min(modInt) )
# =============================================================================

# =============================================================================
# # g
# count = 0
# countNums = 0
# for j in str2:
#     if j.isdigit():
#         if len(j) > 1 and j[0] == j[-1] :
#             count += int(j)
#             countNums +=1
#             
# if countNums == 0:
#     countNums = 1
# print(count / countNums )
# =============================================================================

# =============================================================================
# # 9
# 
# # a b
# # countac = 0
# # countxy = 0
# 
# # for i in str2:
# #     if i.isalpha():
# #         if i.startswith("ac"):
# #             countac += 1
# #         if i.endswith("xy"):
# #             countxy += 1
#             
# 
# # print("elements startwing with 'ac': ",countac)
# # print("elements ending with 'xy", countxy)
# 
# # # d
# # uniqArr = []
# 
# # for i in str2:
# #     if i.isalpha():
# #         if not i in uniqArr:
# #             uniqArr.append(i)
#             
# # print(uniqArr)
# 
# # # e
# 
# # maxLength = 0
# # thisWord = ""
# 
# # for i in uniqArr:
# #     if len(i) > maxLength:
# #         maxLength = len(i)
# #         thisWord = i
#         
# # print(thisWord, maxLength)
# 
# 
# # # v
# 
# # countmn = 0
# 
# # for i in str2:
# #     if i.isalpha():
# #         if i.startswith("mn", 3):
# #             countmn += 1
# #             print(i)
#             
# 
# # print("elements startwing with 'mn' from position 4 is: ",countmn)
# =============================================================================


# =============================================================================
# # 10
# 
# for i in str2:
#     i = i.strip(" ")
#     countDigit = 0
#     countLetter = 0
#     if not i.isalpha() and not i.isdigit() :
#         for j in i:
#             if j.isalpha():
#                 countLetter += 1
#             elif j.isdigit():
#                 countDigit += 1
#     if countDigit > countLetter:
#         print(i)
# =============================================================================

