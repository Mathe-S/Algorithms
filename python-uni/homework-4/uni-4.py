import random# 4s1 = set(  [ random.randint(1, 9999) for i in range(1000)  ]  )s2 = set(  [ random.randint(1, 9999) for i in range(1000)  ]  )# =============================================================================# # ა# # print( len( s1.union(s2)) )# =============================================================================# =============================================================================# # ბ# # s3 = s1.intersection(s2)# # print( sum(x for x in s3 ) / len(s3)  )# =============================================================================# =============================================================================# # გ# # print ( s1.symmetric_difference(s2) )# =============================================================================# დs3 = s1.difference(s2)s4 = s2.difference(s1)ans1 = sum( x**2 for x in s3 ) ** (1/2)ans2 = sum( x**3 for x in s4 ) ** (1/3)print(ans1 - ans2)