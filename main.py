def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0],signature[1]]
    else:
        i=0
        while i < n-3:
            signature.append(signature[i]+signature[i+1]+signature[i+2])
            i +=1
    return signature

print(tribonacci([1, 1, 1], 10))
# output [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]