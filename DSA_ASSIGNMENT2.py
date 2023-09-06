
# BINARY SEARCH

def bsr(x,value,l,h):
    if l>h:
        return "value not found"
    m = (l+h)//2
    mid_value = x[m]

    if mid_value == value:
        return m
    
    if mid_value < value:
        l = m+1
    else:
        h = m-1
    return bsr(x,value,l,h)

x = [1,3,4,5,7,23,56,89,34,67,87,21]

print(bsr(x,5,0,len(x)-1))



# MERGE SORT

def merge(x,l,m,r):
    n1 = m-l+1
    n2 = r-m

    L = []
    R = []

    for i in range(0,n1):
        L.append(x[l+i])

    for j in range(0,n2):
        R.append(x[m+1+j])

    i = 0
    j = 0
    k = l 

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            x[k] = L[i]
            i+=1
        else:
            x[k] = R[j]
            j+=1
        k = k+1
    while i < n1:
        x[k] = L[i]
        i+=1
        k+=1

    while j < n2:
        x[k] = R[j]
        j+=1
        k+=1    


def mergesort(x,l,r):
    if l<r:
        m = l + (r-l)//2
        mergesort(x,l,m)
        mergesort(x,m+1,r)
        merge(x,l,m,r)


x = [1,3,6,7,3,4,99,34,56,23,78,21]

mergesort(x,0,len(x)-1)
print(x)



# QUICK SORT

def quicksort(x):
    if len(x)<=1:
        return(x)
    else:
        p = x[0]
        l = [i for i in x[1:] if i < p]
        r = [i for i in x[1:] if i >= p]
        return quicksort(l)+[p]+quicksort(r)
    
x = [1,3,4,5,7,23,56,89,34,67,87,21]

print(quicksort(x))



# INSERTION SORT

def insertionsort(x):
    l = len(x)
    if l<=1:
        return
    for i in range(1,l):
        n = x[i]
        j = i-1
        while j>=0 and n < x[j]:
            x[j+1] = x[j]
            j=j-1
        x[j+1]=n

x = [12,34,2,98,46,19,45,54,32,74,15,34]
insertionsort(x)
print(x)


# Sort list of strings

def sort_list_with_sorted(strings_list):
    sorted_list = sorted(input_list)
    return sorted_list

def sort_list_with_sort(input_list):
    input_list.sort()
    return input_list 

input_list = ["banana", "apple", "orange", "kiwi", "grape", "mango"]

sorted_list1 = sort_list_with_sorted(input_list)
print("Sorted list using sorted():",sorted_list1)

sorted_list2 = sort_list_with_sort(input_list.copy())
print("Sorted list using sort():",sorted_list2)





