lst=[80,90,60,70,55,44,33,88,99,55,11,22]
lst.sort()
print (lst)

num=int(input("Enter the number to  search: "))


beg=0
last=len(lst)-1

while beg<=last:
  mid=(beg+last)/2
  #print mid
  if lst[mid]==num:
    print num,'Found at position',mid
    break
  elif num<lst[mid]:
    last=mid-1
  else:
    beg=mid+1
else:
  print "Not found in list"
    
