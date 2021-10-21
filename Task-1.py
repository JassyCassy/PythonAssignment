def shuffleArray(a, n):
 

    i, q, k = 0, 1, n
    while(i < n):    
        j = k
        while(j > i + q):
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
        i += 1
        k += 1
        q += 1
 

a = [2, 5, 1, 3, 4, 7]
n = len(a)
shuffleArray(a, int(n / 2))
for i in range(0, n):
    print(a[i], end = " ")



#Exercise Task #1:
#Given the list nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#Return the list in the form [x1,y1,x2,y2,...,xn,yn].    