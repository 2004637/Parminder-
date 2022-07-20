##answer 1
print()
print("############ answer 1 ##############")
print("answer 1")
str="my first python class"
print(len(str))

##answer 2
print()
print("############ answer 2  ##############")
print("answer 2")
str="google"
str_count=str.count('g')
print(str_count)
str_count=str.count('o')
print(str_count)
str_count=str.count('l')
print(str_count)
str_count=str.count('e')
print(str_count)
##answer3
print()
print("############ answer 3 ##############")
print("answer 3")
str="w3resourse"
p=str[:2]
q=str[-2:]
print(p+q)
str="w3"
p=str[:2]
q=str[-2:]
print(p+q)

#answer 4
print()
print("############ answer 4 ##############")
str="restart"
print(str.replace('r','$'))

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))

##answer 5
print()
print("############ answer 5 ##############")
def string_mix(a,b):
    new_a=b[:2]+a[2:]
    new_b=a[:2]+b[2:]
    print(new_a +' '+ new_b)
print(string_mix('abc','xyz'))

##answer 6
print()
print("############ answer 6 ##############")
str="string"
if(str[-3:]!='ing'):
    print('expected result:' ,str + 'ing')
else:
    print("expected result:", str[:-3] + 'ly')


##answer 7
    print()
print("############ answer 7 ##############")

def not_poor(str1):
	  snot = str1.find('not')
	  spoor = str1.find('poor')
	  
	
	  if spoor > snot and snot>0 and spoor>0:
	    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
	    return str1
	  else:
	    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
print ("answer 5")

#answer 8
print()
print("############ answer 8 ##############")

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["Pooja", "nidhi", "parminder"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])

#answer 9
print()
print("############ answer 9 ##############")
str="online tutorial is best"
n=7
first_part= str[0:n]
second_part= str[n+1:]
print(first_part + " " + second_part)

#answer 10
print()
print("############ answer 10 ##############")
def word(str):
  str=str[-1:] + str[1:-1] + str[:1]
  print(str)
print(word('school'))

##answer 11
print()
print("############ answer 11 ##############")
print()
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('school'))

##answer 12  ***
print()
print("############ answer 12 ##############")
print()
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the Golden Temple is the holy place for sikh'))

##answer 13
print()
print("############ answer 13 ##############")
print()
#user_input=input("what is ur name?")
#print("what is ur name?",user_input.lower())
#print("what is ur name?",user_input.upper())

##answer 14 ***
print()
print("############ answer 14 ##############")
print()
#items = input("Input comma separated sequence of words")
#words = [word for word in items.split(",")]
#print(",".join(sorted(list(set(words)))))

##answer 17
print()
print("############ answer 17 ##############")
print()
str=input("enter the word:")
if(len(str)>2):
   print(str[-2:]+str[-2:]+str[-2:]+str[-2:])
else:
    print("word contains only 2 characters")


##answer 17 (another way
print()
print("############ answer 17 (another way) ##############")
print()
str=input("enter the word:")
print(str[-2:]+str[-2:]+str[-2:]+str[-2:])

##answer 18
print()
print("############ answer 18 ##############")
print()
string=input("enter the string")
new_string=string[:3]
if(len(string)>3):
    print("expected string=",new_string)
else:
     print(string)

print("*********ASSIGNMENT-1*******")
print("1.")
name='my first python class'
print(len(name))
print("2.")
fname='mississippi'
print(fname.count('s'))
print("3.")
m=input('enter:')
print(m)
if len(m)<2:
        print('empty string')
else:
     print(m[0:2]+m[-2:])
print("4.")
c=input('string')
temp=c[0]
for i in range(1,len(c)):
               if(c[0] == c[i] ):
                      temp = temp + '$'
               else:
                  temp = temp + c[i]
print(temp)
print("5.")
p=input('string')
q=input('string')
new_p = q[:2] + p[2:]
new_q = p[:2] + q[2:]
print(new_p + ' '+new_q)
print("6.")
c=input('string')
if len(c)>=3:
    if c[-3:]=='ing':
                   c=c+'ly'
                   print(c)
    else:
        c=c+'ing'
        print(c)
else:
    print('less than 3')
print("7.")
str1=input("enter a string:")
snot=str1.find('not')
spoor=str1.find('poor')
if spoor>snot and snot>0 and spoor>0:
         str1=str1.replace(str1[snot:(spoor+4)],'good')
         print(str1)
else:
   print(str1)
print("8.")
def  longest(a):
    max1=len(a[0])
    temp=a[0]
    for i in a:
        if len(i)>max1:
            max1=len(i)
            temp=i
    print("the longest word is:",temp,"and length is:",max1)
l1=["red","exercise","blue","white"]
longest(l1)
print("9.")
c=input('string')
index=int(input())
changed_string=''
for char in range(0,len(c)):
                    if char!=index :
                    changed_string+=c[char]
print(changed_string)
print("10.")
c=input('string')
new_string=c[-1]+c[1:-1]+c[0]
print(new_string)
print("11.")
c=input('string')
new_string=''
for char in range(len(c)):
                     if char%2==0:
                     new_string+=c[char]
print(new_string)
print("12.")
c=input("enter a sentence") 
char=input('char')
counter=c.count(char)
print(counter)
print("13")
c=input('string')
print(c.lower())
print(c.upper())
print("14.")
c=input('string')
print(c.lower())
print(c.upper())
