def two_sum(arr,k):
    d=dict()
    count=0
    for i in arr:
        if (k-i) in d:
            # print(d[k-i])
            count = count+d[k-i]

        if i in d:
            d[i]+=1

        else:
            d[i]=1

    return count



arr = [1, 1, 1, 1]
k = 2
print(two_sum(arr,k))