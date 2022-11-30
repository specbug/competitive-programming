t=' bottle'
z=lambda x:(t+'s' if x-1 else t)+' of beer on the wall'
m=lambda x,k=0:x%100 if x%100 else ('N' if k else 'n')+'o more'
p=lambda x:'Take one down and pass it around' if x else 'Go to the store and buy some more'
c=99
while c+1:
	print('{X}{b}, {x}{u}.\n{l}, {y}{B}.\n'.format(X=m(c,1),x=m(c),y=m(c-1),l=p(c),B=z(c-1),b=z(c),u=z(c)[:16-(c==1)]))
	c-=1