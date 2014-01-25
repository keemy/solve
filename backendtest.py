#!/usr/bin/python
print "Content-Type: text/plain"
print
print """\
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
"""
import cgi
import cgitb;cgitb.enable()
import os
import Cookie
import json
import string
from itertools import permutations

def RPN(n):
  if n == 1:
    yield ' {} '
  for i in range(1,n):
    for left in RPN(i):
      for right in RPN(n - i):
        yield left + right + ' + '
        yield left + right + ' * '
        yield left + right + ' - '
        yield left + right + ' / '

def evaluate(st):
    s=[1,1]
    #import pdb; pdb.set_trace()
    try:
        for i in st.split():b,a=map(float,s[:2]);s[:2]=[[a+b],[a-b],[a*b],[a/b],[i,b,a]]["+-*/".find(i)]
    except:
        return -1
    return s[0]

def solve(arr,k):
    n=len(arr)
    possible=list(RPN(n))
    perms=permutations(arr)
    stop=0
    
    for perm in perms:
        for form in possible:
            s=form.format(*perm)
            #print s
            
            k1=evaluate(s)
            
                
            if k1==k:
                return s,k
                stop=1
                break
        if stop:
            break
			
			


form=cgi.FieldStorage()

nums = form.getfirst('nums', 'empty')
nums.split(",")
goal = form.getfirst('goal', 'empty')

out,_=solve(nums,goal)

print """\
Content-Type: text/html\n
<html><body>
<p>"%s"</p>
</body></html>
""" % out







