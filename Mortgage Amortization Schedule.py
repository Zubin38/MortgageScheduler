#Amortization monthly scheduler
#Zubin Meyer

#get inputs from user
begbal=float(input("Balance/Amount: $"))
rate=float(input("Rate (as a %): "))
years=float(input("How many years to maturity?: "))

#calculate monthly payment in steps
n=12*years
rate/=1200
rateexp=(1+rate)**(n)
monthlypay=begbal*(rate*rateexp)/(rateexp-1)

#create a running balance variable
runbal=begbal

#print table headers
print("Month\t Interest\t    Principal\t  EndBal")

#in loop calculate interest and principal for each payment for every month, print 5 decimals out
month=1
while month<=n:
    interest=runbal*rate
    pcpl=monthlypay-interest
    runbal-=pcpl
    print(month,"\t","%.5f" % interest,"\t","%.5f" % pcpl,"\t","%.5f" % runbal)
    month+=1

#show monthly payments
print("Monthly payment is: ",monthlypay)





