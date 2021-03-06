"""  დავალება 1. დავალების მაქსიმალური შეფასებაა 10 ქულა.

    შენიშვნა.
        რიგ შემთხვევებში კოდის გაფორმება ფუნქციის სახით ჯობია. შესაბამისად, თუ საჭიროდ ჩათვლით განსაზღვრეთ და
        კოდის ნებისმიერ ადგილას გამოიყენეთ ფუნქცია.

        დავალების გაკეთება შესაძლებელია იმ მასალით, რომელიც განვიხილეთ ლაბორატორიულ მეცადინეობებზე, ამიტომ
        სხვა მოდულების გამოყენების შემთხვევაში შესაბამის დავალებას არ ჩავთვლი.

"""
import random

""" 1 ქულა = 10% 
    1. დაწერეთ გენერატორი, რომელიც წინასწარ დასახელებული [a=100, b=999] შუალედიდან აღებული N (=5000) 
       3 თანრიგა შემთხვევითი მნიშვნელობით შეავსებს ლისტს შემდეგი პრინციპის გათვალისწინებით: 3 თანრიგა 
       მნიშვნელობიდან მესამე თანრიგზე განთავსებული იქნება პირველ ორ თანრიგზე განთავსებული მნიშვნელობის 
       ჯამის ტოლი ან ჯამის ერთეულოვანი თანრიგის მნიშვნელობის ტოლი (მაგალითად, 123 --> 1+2=3 ან 
       583 --> 5 + 8 = 13, 13 --> 3 == 3). 
       
       დაითვალეთ და დაბეჭდეთ სიმრავლეში ელემენტების რაოდენობა და სიმრავლის პირველი 20 ელემენტი. 
       თუ სიმრავლე ცარიელია დაბეჭდეთ შესაბამისი გზავნილი. 
       
       შენიშვნა. დავალების გაკეთება შეიძლება დამხმარე ფუნქციის გამოყენებით. დავალებაში აუცილებლობას
                არ წარმოადგენს მიღებული სიმრავლე შეიცავდეს უშუალოდ 5000 ელემენტს.      """


def task1(a, b, N):
    myList = []
    for i in range(N):
        x = random.randint(a, b)
        if ( (x%100)//10 + x//100 ) == x%10 or ( ((x%100)//10 + x//100) %10 == x%10 ):
            myList.append(x)
    print("დავალება 1: \n სიმრავლეში ელემენტების რაოდენობაა: {x} \n სიმრავლის პირველი 20 ელმენტია: {y}".format( x = len(myList), y = myList[:20]))
    
task1(100, 999, 5000)





""" 1 ქულა = 10%
    2. შექმენით ლისტი, რომელიც შეივსება უშუალოდ N (=2000) 15 თანრიგა მნიშვნელობებით შემდეგი პრინციპის
       გათვალისწინებით: სიმრავლეში უნდა ჩავარდეს ის შემთხვევითი მნიშვნელობა, რომლის 3-3 თანრიგებად
       დაყოფის შემთხვევაში ყოველი სამეული დააკმაყოფილებს წინა დავალებაში გამოყენებულ პრინციპს. 
       
       მიღებულ სიმრავლეში დაითვალეთ და დაბეჭდეთ იმ ელემენტების რაოდენობა, რომელშიც ციფრები თანრიგების 
       მიხედვით დალაგებული იქნება ზრდადობით. თუ სიმრავლე ცარიელია დაბეჭდეთ შესაბამისი გზავნილი.     """


def task2(N):
    myList = []
    count_sorted_elements = 0
    for i in range(N):
        sub_int_str = ""
        for j in range(5):
            x = random.randint(100, 999)
            if ( (x%100)//10 + x//100 ) == x%10 or ( ((x%100)//10 + x//100) %10 == x%10 ):
               sub_int_str += str(x) 
        if len(sub_int_str) == 15:
            myList.append( int(sub_int_str) )
    print("\nდავალება 2: \n15 სიმბოლოიანი მნიშვნელობები რომელბიც პირობას აკმაყოფილებენ: ", myList)  # 2000 ძალიან პატარაა რომ შედეგი მოგვცეს, 100000 იც იშვიათად იძლევა შედეგს.
    for i in myList:
        subList = list( str(i) )
        if subList == sorted(subList):
            count_sorted_elements += 1
    print("ზრდადობით დალაგებული ელემენტების რაოდენობაა: ", count_sorted_elements) if count_sorted_elements > 0 else print("ზრდადობით დალაგებული ელემენტები არ მოიძებნა")


task2(100000)



alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', ',', ':', ';']
N = 10000

""" 2 ქულა = 20%
    3. მოცემული alfa სიმრავლისგან შექმენით N სიმბოლოიანი სტრიქონი, რომელშიც სტრიქონის ფორმირების პროცესში 
       სასვენი სიმბოლოების შეცვლა მოხდება ჰარის (' ') სიმბოლოთი. 
       
       სტრიქონის ცალკეულ სიტყვებად დაყოფით მიღებული სიტყვების სიმრავლის გამოყენებით მოახდინეთ ლექსიკონის 
       ფორმირება შემდეგი პრინციპის გათვალისწინებით: თუ სიტყვა იწყება და მთავრდება ციფრითი მნიშვნელობით, 
       მაშინ შესაბამისი წყვილი გამოიყენეთ ლექსიკონის გასაღების როლში, ხოლო მნიშვნელობა კი მიამატეთ ამ 
       გასაღებზე მნიშვნელობების სიმრავლეს. თუ სიტყვა იწყება ან მთავრდება ციფრითი მნიშვნელობით, მაშინ 
       შესაბამისი ელემენტი გამოიყენეთ ლექსიკონის გასაღების როლში, ხოლო მნიშვნელობა კი მიამატეთ ამ გასაღებზე 
       მნიშვნელობების სიმრავლეს. წინააღმდეგ შემთხვევაში ელემენტი მოათავსეთ 'other' გასაღებზე განთავსებული 
       სიტყვების სიმრავლში. 
       
       მიღებულ ლექსიკონში ყოველ გასაღებზე განთავსებული სიმრავლე შეცვალეთ ახალი სიმრავლით, რომელშიც 
       სიტყვებიდან ამოღებული იქნება ციფრითი მნიშვნელობები მიმდევრობების შეუცვლელად. გამოთვალეთ და 
       დაბეჭდეთ ლექსიკონის ორ ელემენტიანი გასაღებიდან იმ გასაღების მნიშვნელობა, რომელშიც ყველაზე მეტი 
       ელემენტია განთავსებული.      """



def task3(main = False):
    change_to_har = ['.', ',', ';', ':']
    myStr = ''
    myDict = {'other': []}
    
    # შევქმნათ N სიმბოლოიანი სტრიქონი და სასვენი სიმბოლოები შევცვალოთ ჰარით:
    for i in range(N):
        x = random.choice(alfa)
        if x in change_to_har:
            x = ' '
        myStr += x
      
    fortask5 = myStr # მეხუთე დავალებისთვის
    
    # დავყოთ სტრიქონი ცალკეულ სიტყვებად და შევავსოთ ლექსიკონი
    for i in myStr.split(" "):
        # გავფილტროთ ცარიელი ელემენტები
        if not i:
            continue
        
        # შევავსოთ
        if i[0].isdigit() or i[-1].isdigit():
            if i in myDict:
                myDict[i].append(i)
            else:
                myDict[i] = [i]
        else:
            myDict['other'].append(i)
            
    # print(myDict)
    
            
    # ამოცანის მეორე ნაწილი:
    # ლექსიკონის მნიშვნელობების გაფილტვრა არა რიცხვითი მნიშვნელობისგან:
    for i  in myDict:
        temp_arr = []
        for j in myDict[i]:
            temp_str = ''
            for k in list(j):
                if k.isdigit():
                    temp_str += k
            temp_arr.append(temp_str)
        myDict[i] = temp_arr
    # print(myDict)
    
    # ყველაზე მეტ ელემენტიანი სიმრავლის არჩევა 
    my_key = ''
    my_length = 0
    
    
    for i in myDict:
        if i == 'other':
            continue
        if len(myDict[i]) > my_length:
            my_length = len(myDict[i])
            my_key = i
    
    if main:
      print("\nდავალება 3: \n ყველაზე მეტ ელემენტიანი გასაღებია: ", my_key, "\n")
    
    # მეოთხე და მეხუთე დავალებისვის დავაბრუნოთ საჭირო დათა:
    return [ myDict['other'], fortask5]
    
task3(main = True)





''' 1 ქულა = 10%
    4. წინა დავალებაში მიღებული ლექსიკონი other გასაღებზე განთავსებული მნიშვნელობების სიმრავლიდან 
       შექმენით ორი სიმრავლე s1 და s2 შემდეგი პრინციპით: საწყის სიმრავლეში ელემენტების რაოდენობის 
       ნახევარის ტოლი მნიშვნელობით s1 და s2 სიმრავლეში ჩაწერეთ მნიშვნელობები შემთხვევითი პრინციპით 
       და არა ინდექსების სიმრავლის შუაზე გაყოფით. (მაგალითად, თუ გასაღებზე 1000 ელემენტია, მაშინ 
       ორივე სიმრავლე შემთხვევითი პრინციპით უნდა შეიტანოთ 500-500 ელემენტი. აუცილებელი არაა ამ 
       რაოდენობის ელემენტების შემდგარი სიმრავლის მიღება.)
        
       იპოვეთ და დაბეჭდეთ თუ რომელ სიმრავლეზე (s1-s2, s2-s1 თუ მათ თანაკვეთაზე) მიიღწევა საშუალო 
       არითმეტიკულის უდიდესი მნიშვნელობა.    '''


def task4():
    # წინა დავალებიდან წამოვიღოთ other გასარებზე არსებული მნიშვნელობები და გავფილტროთ ცარიელი მნიშვნელობებისგან
    other = []
    for i in task3()[0]:
        if not i:
            continue
        other.append(i)
    
    # შევქმნათ s1 და s2 სიმრავლეები
    n = len(other) // 2
    s1, s2 = set(), set()

    for i in range(n):
        s1.add(random.choice(other))
        s2.add(random.choice(other))
    
    s3 = s1.difference(s2)
    s4 = s2.difference(s1)
    s5 = s1.intersection(s2)
    
    sum3 = sum(int(x) for x in s3)
    sum4 = sum(int(x) for x in s4)
    sum5 = sum(int(x) for x in s5)

    if sum3/len(s3) >= sum4/len(s4) and sum3/len(s3) >= sum5/len(s5):
        print("დავალება 4: \n s1-s2 სიმრავლეზე მიიღწევა საშუალო არითმეტიკულის უდიდესი მნიშვნელობა")
    elif sum4/len(s4) >= sum3/len(s3) and sum4/len(s4) >= sum5/len(s5):
        print("დავალება 4: \n s2-s1 სიმრავლეზე მიიღწევა საშუალო არითმეტიკულის უდიდესი მნიშვნელობა")
    elif sum5/len(s5) >= sum3/len(s3) and sum5/len(s5) >= sum4/len(s4):
        print("დავალება 4: \n s1 ის და s2 ის სიმრავლეთა თანაკვეთაზე მიიღწევა საშუალო არითმეტიკულის უდიდესი მნიშვნელობა")

task4()





""" 1.5 ქულა = 15% 
    5. დავალება 3-ში მიღებული სიტყვების სირავლის გამოყენებით შეავსეთ ორგანზომილებიანი ბიბლიოტეკა:
       თუ სიტყვა იწყება ალფავიტის სიმბოლოთი და მთავრდება ციფრითი  
       მნიშვნელობით, მაშინ ეს წყვილი გამოიყენეთ გასაღების როლში და სიტყვა მოათავსეთ ამ გასაღების ქვეშ 
       განთავსებულ სიტყვების სიმრავლეში. ის სიტყვები, რომლებშიც დარღვეულია პირობა მოათავსეთ "other"
       გასაღებზე განთავსებულ სიტყვების სიმრავლეში. შიდა გასაღები განუსაზღვრეთ "other" გასაღების გარდა 
       სხვა ყველა გასაღებს. კერძოდ, ყოველი სიტყვა შესაბამის გასაღებზე განათავსეთ ისეთ შიდა ციფრით
       გასაღებზე, რომელზეც მთავრდება ეს სიტყვა, ხოლო სიტყვა კი განათავსეთ ასეთ ციფრით გასაღებზე
       განთავსებულ მნიშვნელობათა სიმრავლეზე. ყოველ გასაღებზე განთავსებულ სიტყვების სიმრავლეში 
       სიტყვა შეცვალეთ მასში შემავალი ციფრების (თანმიმდევრობის შეუცვლელად) მიმდევრობისგან შემდგარი 
       მნიშვნელობით. ეს ეხება "other" გასაღებისაც.
       
       მიღებული ლექსიკონისთვის იპოვეთ წყვილი გარე და შიდა გასაღებისა, რომელზეც ორგანზომილებიან
       ლექსიკონში მიიღწევა ელემენტის მაქსიმალური მნიშვნელობა. 
"""


def task5():
    myStr = task3()[1]; # წამოვიღოთ N სიმბოლოიანი სტრიქონი, რომელსაც მესამე დავალებიდან მასივის მეორე ელემენტის სახით ვაბრუნებ 
    myDict = {'other': []}
    
    # დავყოთ სტრიქონი ცალკეულ სიტყვებად და შევავსოთ ლექსიკონი
    for i in myStr.split(" "):
        # გავფილტროთ ცარიელი ელემენტები
        if not i:
            continue
        
        # შევავსოთ
        if i[0].isalpha() and i[-1].isdigit():
            if i in myDict:
                myDict[i].append({ i[-1]: [i] })
            else:
                myDict[i] = [ { i[-1] : [i]  } ]
        else:
            myDict['other'].append(i)
                

    #ლექსიკონშ გვაქვს  გვაქვს ასეთი სტუქტურა: გასაღები: [ 'other': [], { გასაღები1: [ მნიშვნელობა1, მნიშვნელობა2 ... ] }, { გასაღები2: [ მნიშვნელობა1, მნიშვნელობა2 ... ] } ]
    
    # შევცვალოთ 'other' გასაღებში არსებული მნიშვნელობები მხოლოდ შესაბამისი რიცხვითი მნიშვნელობებით
    temp_arr = []
    for i in myDict['other']:
        temp_str = ''
        for j in list(i):
            if j.isdigit():
                temp_str += j
        if not temp_str:
            continue
        temp_arr.append(temp_str)
    myDict['other'] = temp_arr
    
    
    # ქვემოთ მოცემული for ციკლები ჩავლენ ყველაზე დაბალ საფეხურზე და შეცვლიან ელემენტს ისე რომ მხოლოდ რიცხვი დარჩეს
    for i in myDict:
        if i == 'other':
            continue
        for j in myDict[i]:
            for k in j:
                temp_arr = []
                for kk in j[k]:           
                    temp_str = ''
                    for kkk in kk:
                       if kkk.isdigit():
                           temp_str += kkk
                    temp_arr.append(temp_str)
                j[k] = temp_arr
    
    # print(myDict) 
    
    
    # ელემენტის მაქსიმალური მნიშვნელობის ძებნა
    
    # ჯერ მოვძებნოთ 'other' გასაღებშi მაქსიმალური
    max_key = 'other'
    max_val = 0
    
    for i in myDict['other']:
        if int(i) > max_val :
            max_val = int(i)
    
    # ახლა დანარჩენ გასაღებებში
    for i in myDict:
        if i == 'other':
            continue
        for j in myDict[i]:
            for k in j.values():
                if int(k[0]) > max_val :
                    max_val = int(k[0])
                    max_key = i
            
            
    print("\nდავალება 5: \n მაქსიმუმი მნიშვნელობა არის გასაღებ: ", max_key, "-ში და არის: ",  max_val, )
    # print(myDict)



    # ლექსიკონის დაბრუნდება მე-6 დავალებისთვის
    return myDict

task5()







""" 2.5 ქულა = 25% 
   6. დაწერეთ ფუნქცია, რომელიც მიიღებს რამდენიმე პარამეტრს და დააბრუნებს ორგანზომილებიანი ლექსიკონის 
      მითითებულ გასაღებზე განთავსებული სიმრავლის ელემენტების საშუალო არითმეტიკულის მნიშვნელობას. 
      ფუნქციის პარამეტრები განსაზღვრეთ შემდეგი პრინციპით:
         1. ლექსიკონი - სიმრავლე, რომლის ელემენტებზეც უნდა განხორციელდეს გამოთვლები;
         2. ლექსიკონის გასაღები - თუ გასაღები არაა ლექსიკონი, მაშინ ფუნქციამ დააბრუნოს ლექსიკონის  
            წინასწარ განსაზღვრულ გასაღებზე განთავსებული მნიშვნელობების სიმრავლის საშუალო 
            არითმეტიკულის მნიშვნელობა. წინააღმდეგ შემთხვევაში ფუნქციამ გამოითვალოს და დააბრუნოს მესამე
            პარამეტრით გაჩუმების პრინციპით გადაცემულ (შიდა) გასაღებზე განთავსებული მნიშვნელობების
            სიმრავლის საშუალო არითმეტიკულის მნიშვნელობა.
         3. ლექსიკონის შიდა გასაღები (გაჩუმებითი მნიშვნელობით - '0') - თუ ეს პარამეტრი ცხადი სახითაა
            გამოყენებული, მაშინ ფუნქციამ უნდა დაითვალოს და დააბრუნოს შესაბამის შიდა გასაღებზე
            განთავსებული მნიშვნელობათა სიმრავლის საშუალო არითმეტიკულის მნიშვნელობა.
         4. მეოთხე პარამეტრი (გაჩუმებითი მნიშვნელობით - None) - თუ ეს პარამეტრი ცხადი სახითაა
            მითითებული, მაშინ აღნიშნული სიმრავლიდან მოხდეს იმ ელემენტების საშუალო არითმეტიკულის 
            მნიშვნელობის დათვლა, რომლებიც გარკვეულ პირობას აკმაყოფილებენ. ცხადია, ამ პარამეტრიდან
            მოხდება ფუნქციაზე მიმთითებლის გადაცემა, რომლითაც მოხდება შესაბამისი სიმრავლიდან 
            პირობის (მაგალითად, ლუწი რიცხვების, ან ისეთი, რომლის ციფრები დალაგებულია ზრდადობით) 
            დამაკმაყოფილებელი ქვესიმრავლის მოძიება. 
          
      ფუნქცია გამოიყენეთ დავალება 5-ში მიღებული ლექსიკონის მიმართ. დაითვალეთ და დაბეჭდეთ აღნიშნული
      ლექსიკონის იმ გასაღების ან გასაღებების წყვილის მნიშვნელობა, რომელზეც მიიღება საშუალო არითმეტიკულის
      მინიმალური მნიშვნელობა. საშუალო არითმტიკული დაითვალეთ იმ ელემენტების მიმართ, რომლის ლუწ
      ინდექსზე მდგომი მნიშვნელობები ლუწია.
      
      შენიშვნა. აუცილებლობის შემთხვევაში ობიექტის ტიპის დასადგენად (სტრიქონული სახით მისაღებად
               შესაძლებელია შემდეგი კონსტრუქციის გამოყენება: მაგალითად,
               dct = {}
               print(dct.__class__.__name__)    # --> დაიბეჭდება dict
"""

ans_key = ''
min_value = 9999999

def task6function(dct, key, in_key = 0, func = None):
    
    # ის შემთხვევა როცა გასაღები ლექსიკონი არ არის
    if not type(dct[key][0]) is dict:
        # დააბრუნებს გასაღების არსებული სიმრავლის რიცხვთა ჯამის საშუალო არითმეტიკულს გადაცემული ფუნქციის გათალისწინებით
        return sum( int(x) for x in dct[key] if func(x)) / len(dct[key])
    else:
        # შემთხვევა როცაგასაღები ლექსიკონია
        # ჩავა ლექსიკონ-გასაღების ქვედა სიმრავლეებშ და დათვლის საშუალო არითმეტიკულს
        for i in dct[key]:
                return sum ( int(x) for x in i[in_key] if func(x) ) / len (i[in_key])

# ფუნქცია იმის დასადგენად არის თუ არა ლუწ ადგილზე მდგომი ელემენტი ლუწი
def conditionfunc(x):
    for i in list(x)[::2]:
        if int(i) % 2 != 0:
            return False
    return True


# მეექვსე დავალების მტავარი ფუნქცია !!! 
def task6():
    
    # წამოვიღოღ მეხუთე დავალებიდან მიღებული ლექსიკონი
    myDict = task5()
    # გამოვიყენოთ გლობალური ცვლადები მინიმაულირი მნიშვნელობის დასადგენად და მინიმალური მნიშვნელობის გასაღების დასამახსოვრებლად
    global min_value
    global ans_key
    
    for key in myDict:
        
        # ის შემთხვევა როცა გასაღები არ არის ლექსიკონი
        if not type(myDict[key][0]) is dict:
            # task6function ფუნცია myVal  ში დააბრუნებს საშუალო არითმეტიკულის მნიშვნელობას
            myVal = task6function(myDict, key, func = conditionfunc )
            
            # თუ myVal ტოლია 0 ის, ეს ნიშნავს რომ ლუწ ადგილებზე მდგომი ციფრები ლუწი არ არის, ამიტომ გამოვტოვოთ
            if min_value > myVal > 0 :
               min_value = myVal
               ans_key = key
           
        # ის შემთხვევა როცა გასაღები ლექსიკონია
        else:
            # ამ შემთხვევაში გვექნება ასეთი სტრუქტურა: გასაღები: [ { გასაღები: მნიშვნელობა } ]
            # რომ მივწვდეთ შიდა გასარებს გვჭირდება 2 იტერაცია, ქვედა 2 for  ციკლი სწორედ ამას აკეთებს
            for in_key in myDict[key]:
                for in_key_key in in_key:
                   # task6function ფუნცია myVal  ში დააბრუნებს საშუალო არითმეტიკულის მნიშვნელობას
                   myVal = task6function(myDict, key, in_key_key, func = conditionfunc) 
                   # თუ myVal ტოლია 0 ის, ეს ნიშნავს რომ ლუწ ადგილებზე მდგომი ციფრები ლუწი არ არის, ამიტომ გამოვტოვოთ
                   if min_value > myVal > 0 :
                       min_value = myVal
                       ans_key = key

    print("\nდავალება 6: \n მინიმალური საშუალო არითმეტიკულის მნიშვნელობაა {x}  და ის მდებარეობს გასაღებ {y} ში".format(x = min_value, y = ans_key))


task6()











""" 1 ქულა = 10% 
    7. დააკომენტარეთ დავალება 5 და 6. დამატებით დავალება 6-ზე განსაზღვრულ ფუნქციას გაუკეთეთ 
       დოკუმენტირების სტრიქონი.
       
       შენიშვნა. აღწერილი უნდა იყოს ყოველი ახალი ობიექტის დანიშნულება და მოქმედებები, რისი გაკეთება
                ხდება კომენტარის შემდეგ ხაზზე. წინააღმდეგ შემთხვევაში კომენტარს სრულად არ ჩავთვლი.
                დოკუმენტირების სტრიქონში უნდა იყოს აღწერილი: ავტორი, თარიღი, რა პარამეტრები 
                გადაეცემა, რას აკეთებს ფუნქცია და რას აბრუნებს.      """

