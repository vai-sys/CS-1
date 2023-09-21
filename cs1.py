# mean using pythan
num=[1,4,7,9,2,5,6,7]
n=len(num)
sumation=sum(num)
mean=sumation/n
print("mean is\n" +str(mean))



# median 
num=[1,4,7,9,2,5,6,7]
n=len(num)
if(n%2==0):
  median1= num[n//2]
  median2=num[n//2-1]
  median=(median1+median2)/2
else:
  median=num[n//2]
print("median is\n" + str(median)) 



# Standard deviation
deviation=[x- mean for x in num]
deviationSquare=[d**2 for  d in deviation]
meanDeviationsquare=sum(deviationSquare)/len(deviationSquare)
standarDeviation=meanDeviationsquare**0.5
print("standard deviation is\n"+str(standarDeviation))

# variance
variance=standarDeviation**2
print("variance is :" +str(variance))


   

