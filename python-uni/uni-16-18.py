# =============================================================================# # 16# # print('შეიყვანეთ კვადრატული განტოლების კოეფიციენტები: ')# # a = int(input("a: "))# b = int(input("b: "))# c = int(input("c: "))# # d = b**2 - 4*a*c# # print(a, b, c, d)# ans = ['', '']# # if d == 0 :#     ans[0] = -b / 2*a#     d = 1# elif d > 0 :#     ans[0] = (-b + d**0.5)/(2*a)#     ans[1] = (-b - d**0.5)/(2*a)#     d = 2# else :#     d = 0# # print("განტოლებას აქვს {d} ფესვი, ესენია: {frst} {scnd} ".format( d = d, frst = ans[0], scnd = ans[1] ))# # =============================================================================# =============================================================================# # 17 ფორმულა არასწორია, ლეიბნიცის ფორმულით:# # pi = 0# n = input('შეიყვანეთ რიცხვი: ')# # for i in range(int(n)):#     pi += (4/(2*i+1)) * ((-1) ** i)# # print(pi)# =============================================================================# =============================================================================# # 18# # n = int( input('შეიყვანეთ მნიშვნელობა: ') )# summ = 0# # for x in range(n) :#     summ += ( (-1) ** (x+1) ) * ( 1 / (2*n - 1) * (2*n +1) )#     # print("ა: ", summ/2)# # =============================================================================