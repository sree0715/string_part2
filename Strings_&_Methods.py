# print(len("python")) 

# a="python"
# print(a,type(a))
# print(a[0])

# print("python"[0]) 
# print("python"[1]) 
# print("python"[2]) 
# print("python"[3]) 
# print("python"[4]) 
# print("python"[5]) 
# print("python"[6]) 

""" concatenation:=
Used only for strings. Will combine more than one string together.
we use + to represent concatentation in the strings concept.
string is immutable, modifications cannot be made"""

# v="department"
# print(v+'-'+str(5))
# print(v,str(5))
# print(v[0]+v[-1])
# print(v[3]+v[2]+v[3]+v[4]+v[5]+v[6]+v[7]+v[8]+v[9])

# print("python"[-1]) 
# print("python"[-2]) 
# print("python"[-3]) 
# print("python"[-4]) 
# print("python"[-5]) 
# print("python"[-6]) 
# print("python"[-7]) 

# w="python"
# print(w[:]) 
# print(w[0:]) 
# print(w[0:6]) 
# print(w[0:0]) 
# print(w[0:1]) 
# print(w[0:2]) 
# print(w[0:3]) 
# print(w[0:4]) 
# print(w[0:5]) 
# print(w[0:6]) 
# print(w[0:7]) 
# print(w[0:99]) 
# print(w[0:0]) 
# print(w[3:2]) 
# print(w[5:3]) 
# print(w[0:-1]) 
# print(w[0:-2]) 
# print(w[0:-3]) 
# print(w[0:-4]) 
# print(w[0:-5]) 
# print(w[0:-6]) 
# print(w[0:-7]) 

# r="python"
# print(r[2:5]) 
# print(r[3:4]) 
# print(r[5:2]) 
# print(r[5:5]) 

# y="python"
# print(y[-1:-6])
# print(y[2:-5])
# print(y[-6:])
# print(y[:-6])

# c="python"
# print(c[ : : ]) 
# print(c[0 : : 1]) 
# print(c[ : :2]) 
# print(c[ : :3]) 
# print(c[ : :4]) 
# print(c[ : :5]) 
# print(c[ : :6]) 
# print(c[: : -1]) 
# print(c[:  :-2]) 
# print(c[ : :-3]) 
# print(c[ : :-4]) 
# print(c[ : :-5]) 
# print(c[ : :-6]) 
# print(c[1: : ]) 
# print(c[2: : ]) 
# print(c[3: : ]) 
# print(c[4: : ]) 
# print(c[5: : ]) 
# print(c[6: : ]) 
# print(c[1: 6: ]) 
# print(c[2: 5: ]) 
# print(c[3: 4: ]) 
# print(c[4: 3: ]) 
# print(c[5: 2: ]) 
# print(c[6: 1: ]) 



"""Strings:
string is immutable, modifications cannot be made"""

# a="python"
# print(a,type(a))
# print(a[0])
# a[0]='P'

# print(dir(str))

# n="hEllo PyThon"
# print(n.capitalize())

# name="hEllopyThon"
# print(name.capitalize())

# name="hEllo pyThon"
# print(name.casefold())
# print(name.lower())

# name="hEllopyThon"
# print(name.casefold())
# print(name.lower())

# name="hEllo pyThony"
# print(len(name))
# print(name.center(50))
# print(name.center(50,'$'))
# print(name.center(70,'%'))


# name="hEllo pyThon"
# print(type(name))
# n=name.encode()
# print(n) 
# print(type(n))
# print(n.decode())



# name='hEllo pyThon'
# print(name.upper())
# print(name.lower())
# print(name.isupper())
# print(name.islower())
# b="CRICKET"
# print(b.isupper())
# m='worldcup t20'
# print(m.islower())

# t='hEllo pyThon'
# print(t.title())
# print(t.capitalize())
# print(t.istitle())
# c='Hello Python'
# print(c.istitle())

# n='hEllo pyThon'
# print(n.endswith(''))
# print(n.endswith(' '))
# print(n.endswith('n'))

# n='hEllo pyThon'
# print(n.startswith(''))
# print(n.startswith(' '))
# print(n.startswith('h'))

# z=' hEllo pyThon'
# print(z.startswith(''))
# print(z.startswith(' '))
# print(z.startswith(' h'))


# v=' 4  '
# g='    '
# print(v.isspace())
# print(g.isspace())

# q="hEllo pyo1Tholno"
# print(q.index('l'))
# print(q.index('l',4))
# print(q.index('o'))
# print(q.index('o',5))
# print(q.rindex('h'))
# print(q.index('1'))
# print(q.index('b'))

# print(dir(list))
# a=[10,40,80]
# print(a.index(20))


# r="hEllo pyThon programming"
# print(r.index('u')) 
# print(r.index('n'))
# print(len(r))
# print(r.rindex('g'))

# r="hEllo pyThon programming"
# print(len(r))
# print(len('hello world'))

# print(dir(str))
# n=['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
# 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
# 'removesuffix', 'replace','rfind', 'rindex', 'rjust', 'rpartition', 
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
# 'swapcase', 'title','translate', 'upper', 'zfill']
# print(len(n))


# print('ab'.isidentifier())
# print('a b'.isidentifier())
# print('a_b'.isidentifier())
# print('3ab'.isidentifier())
# print('ab_'.isidentifier())
# print('_'.isidentifier())
# print('a-b_'.isidentifier())
# print('a.b_'.isidentifier())

# _a=4
# print(_a)

# b="6python programming"
# print(b.find('p')) 
# print(b.find('u')) 
# print(len(b))
# print(b.rfind('g')) 

# v="python programming"
# print(v.count('p')) 
# print(v.count('m')) 
# print(v.count('i')) 
# print(v.count('e')) 

# h="python course"
# h[0]='P'
# print(h.replace('course','programming'))
# g="core python programing core"
# print(g.replace('core',2))
# print(g.replace('core',str(2)))
# print(g.replace('core','2'))
# print(g.replace('o','k'))
# print(g.replace('o','k',1))
# print(g.replace('o','k',2))
# print(g.replace('o','k',3))
# print(g.replace('o','k',4))
# print(g.replace('o','k',5))
# print(g.replace('o','k',(2)))

# a=' Ramesh '.strip()
# print(len(a))
# print(' hello '.strip())
# print(len(' hello '.strip()))

# a=' Ramesh '.lstrip()
# print(len(a))

# a='  Ramesh Kumar  '.lstrip()
# print(len(a))

# d="       python programming  .      "
# print(d.strip())
# print(d.lstrip())
# print(d.rstrip())

# a=' python '
# a=' python '.strip()
# print('we are learning',a,'programming')

# e="  hello python      ".strip()
# print(len(e))


# a=1.7,2.5
# print(type(a))

# a="hello","Python",'pro'
# print(a , type(a))
# b=' World ' .join(a)
# print(b)

# a='1','2','3','4','5'
# b='->'.join(a)
# print(b)

# print("Hello", "Python",sep=" World ")

# print('hey',sep='*') # not possible
# print('h','e','y',sep='*') # not possible

# print(1,2,3,4,5,sep='*')

# c="hey"
# d=" ".join(c)
# print(d)
# e="hey",
# f="*".join(e)
# print(f)
# g="hey",''
# h="*".join(g)
# print(h)

# c="Python Programming"
# print(c.removeprefix('p'))
# print(c.removeprefix('P'))
# print(c.removeprefix('Py'))
# print(c.removesuffix('g'))
# print(c.removesuffix('tng'))
# print(c.removesuffix('ming'))


"""isalnum: 
will return True , only if the string contains
only alphabets and numeric , even alphabets and
numeric can be kept inside the string , but
space/spaces and special symbols are not allowed.
if kept spaces or special symbols then it will return False
i.e. no spaces and no special symbols allowed"""


# a="hello_python"
# print(a.isalnum()) # space not allowed in isalnum

# a="hellopython"
# print(a.isalnum())  # returns True bcz no space

# a="hello.python"
# print(a.isalnum())  # returns False bcz .(point) or special symbols are not allowed

# a="hellopython39"
# print(a.isalnum()) # returns True because contains only alphabets and numeric


# b="core python"
# print(b.isalpha())

# b="corepython"
# print(b.isalpha())

# b="corepython39"
# print(b.isalpha())

# b="6"
# print(b.isalpha())

# b="H"
# print(b.isalpha())

# b=""
# print(b.isalpha())

# b=" "
# print(b.isalpha())

# v="august python"
# print(v.isascii())

# b=chr(0)
# c=chr(32)
# print(b.isspace())
# print(c.isspace())
# print("hello"+chr(32)+"Python")
# print("hello"+' '+"Python")
# print("hello","Python",sep=' ')
# print("hello","Python")

# print(chr(32)+"Hey")
# print(chr(0)+"Hey")

# print(chr(65))
# print(ord('a')) 
# print(ord('z')) 
# print(ord('A'))
# print(ord('Z'))
# print(ord('0'))
# print(ord('9'))
# print(ord(' '))
# print(ord('!'))

# v=bin(5)
# print(v,type(v))
# h=0b101
# print(h,type(h)) 
# j=0B101
# print(j,type(j))

# print(bin(7))
# print(0b111)
# print(0B111)

# f=oct(19)
# print(f,type(f))
# print(0o23)
# print(0O23)

# w=hex(36)
# print(w,type(w))
# print(0x24)
# print(0X24)
# print(0xA)
# print(0xa)
# print(0xD)
# print(0xF)

# p="pythON proGRAMming"
# print(p.swapcase()) 

# a=4  ; b=66
# print(b)
# del a,b
# print(b,a)

'''Format'''

# print("Buy this for Rs.{d} or for Rs.{ed}".format(d=11,ed=50))

'''expandtabs  , by default=8'''
# a='R\tS\tV'
# print(a.expandtabs(0))
# print(a.expandtabs(1))
# print(a.expandtabs(2))
# print(a.expandtabs(3))
# print(a.expandtabs(4))
# print(a.expandtabs(5))
# print(a.expandtabs(6))
# print(a.expandtabs(7))
# print(a.expandtabs(8))
# print(a.expandtabs())
# print(a.expandtabs(-1))

""" join """
# v='hello','python','core'
# n='python'
# print('-'.join(v))
# print('*'.join(n))
# print('*'.join("Hello"))

# """ maketrans and translate"""
# r="helly hello"
# a=r.maketrans("l",'r')
# print(a,type(a))
# print(r.translate(a))

# r={}
# print(r,type(r))
# v={1:'hello', 2:'python'}
# print(v[5])

# a="hello\nCore Python\nProgramming"
# print(a)
# g=a.splitlines()
# print(g,type(g))
# print(g[0])
# print(g[1])
# print(g[4])
# h="HelloWelcome to Josh Innovations"
# w=h.split()
# print(w)
# print(w[0][::-1])

# h="HelloWelcome to Josh Innovations"
# print(h.split(" "))
# print(h.split(' '))
# print(h.split())
# print(h.split(""))

# a=5.6,7
# print(a,type(a))

# a=[int(x) for x in input().split()]
# print(a,type(a))
# print(sum(a))
# print("The sum is"+' '+str(sum(a)))
# print("The sum is",sum(a))

# v="Hello Welcome to JoshInnovations"
# print(v.split())

# b="Hello:Welcome: To:Josh:Innovations"
# print(b.split(":"))

# n="Python#C#Java#R#Dart"
# print(n.split("#"))

# f=r'hi\nizambad'
# print(f)

# v=r"hello\bollywood"
# print(v,type(v))

# k="Hello!\nWelcome to \nJoshInnovations"
# print(k.splitlines())

# y="Hello!\nWelcome to \nJoshInnovations"
# print(y.splitlines(True))

# f="hello"
# print(f.zfill(9))

# j="Hey! How are you Doing?"
# print(j.partition("are"))

# t="Hey! How are you Doing?"
# r=t.partition("are")
# print(r)
# print(r[0])

# m="We are Learning Python Programming , Python is Basic need \
#  for ML,DS,AI,DL,BigData..etc"
# print(m.partition("Python"))
# print(m.rpartition("Python"))

# c="Python"
# print(c.ljust(8),"Programming Basics")

# x="Python"
# print(x.rjust(8),"Programming Basics")

# z="Python"
# print(z.rjust(10,'R'))

# s="Python"
# print(s.ljust(10,'R'))

# print(dir(str))


# a=int(input('Enter a:'))
# b=int(input('Enter b:'))
# print(a+b)

# a=[int(x) for x in input().split()]
# print(a)
# print(sum(a))