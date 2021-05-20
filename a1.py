def computepay(h,r):
    if(h>40):
        pay40=40*r
    	pay_above_40=(h-40)*(1.5*r)
        pay=pay40+pay_above_40
	else:
        pay=h*r

    return pay

hrs = input("Enter Hours:")
h=float(hrs)
rate=input("enter rate:")
r=float(rate)
p = computepay(h,r)
print(p)
