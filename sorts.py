def insertion_sort(ar):
    for i in range(1, len(ar)):
        for j in range(i):
            if (ar[i]<ar[j]):
                k = ar[i]
                ar[i] = ar[j]
                ar[j] = k
    print(ar)

def bubble_sort(ar):
    for i in range(len(ar),0,-1):
        for j in range(i-1):
            if (ar[j]>ar[j+1]):
                k = ar[j]
                ar[j] = ar[j+1]
                ar[j+1] = k
    print(ar)



            
    
        
