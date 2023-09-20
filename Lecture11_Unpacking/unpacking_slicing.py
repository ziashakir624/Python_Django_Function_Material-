# scilicing
a = [1,2,3,4,"this is python",[1,[1,2,3,4,5,6,7,8]]]
a = a[4][2:-2]
print(a)



a = [1,2,3,4,'This is python',[1,[1,2,3,4,5,7,8]]]

#  Slicing Method

# answer should equal to ( 'is is pyth' ) so print out b.

b = [a[4][2:-2]]
print(b)


# answer should equal to  (c = [8,7,5,4,3,2,1]) so print out c.

c = [a[-1][1][::-1]]
print(c)


#  Unpacking Method

# a = [1,2,3,4,'This is python',[1,[1,2,3,4,5,7,8]]]

# answer should equal to (['i', 's', ' ', 'i', 's', ' ', 'p', 'y', 't', 'h'] ) so print out e , y.

a,*b,(c,d,*e,f,g),(h,*i) = [1,2,3,4,'This is python',[1,[1,2,3,4,5,7,8]]]
print(e)

*_,(_,_,*y,_,_),(_,*_) = [1,2,3,4,'This is python',[1,[1,2,3,4,5,7,8]]]
print(y)

# answer should equal to  ( 8 7 5 4 3 2 1 ) so print out (l,k,j,i,h,g,f).

a,*b,(c,*d),(e,(f,g,h,i,j,k,l)) = [1,2,3,4,'This is python',[1,[1,2,3,4,5,7,8]]]

print(l,k,j,i,h,g,f)


_,*_,(_,*_),(_,(m,n,o,p,q,r,s)) = [1,2,3,4,'This is python',[1,[1,2,3,4,5,7,8]]]

print(s,r,q,p,o,n,m)
