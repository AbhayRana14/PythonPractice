import re
fname=open("regex_sum_837017.txt")
summ=0;
count=0;
for line in fname:
    f=re.findall('[0-9]+',line)
    for num in f:
        count+=1
        summ=summ+(int(num))
print("there are ",count,"values with a sum of ",summ)