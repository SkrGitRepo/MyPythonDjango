# reduce applied only on single sequence
# Reduce should have only have two paramaeter


add=lambda x,y:x+y
print reduce(add,(1,2,3,4,5,6,7))#Here 1+2=3,3+3=6,6+4=10

mul=lambda x,y:x*y
print reduce(mul,(1,2,3,4,5,6,7)) #HERE 1*2=2,2*3=6,6*4=24......




div=lambda x,y:x/y
print reduce(div,(8,2,1,2)) #HERE 8/2=4,4/1=4,4/2=2,......



