import urllib
 
content = urllib.urlopen('http://www.iplaypy.com/').read()
 
s1=0
while s1>=0:
    begin = content.find(r'<a',s1) href=",begin)
    m2 = content.find(r" m1="content.find(r'">',m1)
 
    s1 = m2
    if(begin<=0):
        break
    elif(content[m1:m2].find(r" ")!=-1):
        m2 = content[m1:m2].find(r' ')
        url = content[m1+6:m1+m2-1]
        print url
    elif m2>=0:
        url = content[m1+6:m2-1]
        print url
print "end."
</a',s1)>
