import math

#First Function simply adds 1 to each values so
#[1,2,3,4] -> [2,3,4,5]

def easy1(A):
    B = []
    for number in A:
        B.append(number + 1)

    return B


#Second function will be 2^A power so
#[1,2,3,4] -> [2,4,8,16]
def easy2(A):
    B = []
    for number in A:
        B.append(2 ** number)

    return B



#Third function will add the number previous (does not add for first number)
#[1,2,3,4] - > [1,3,5,7]
def easy3(A):

    B = A.copy()
    for i in range(1, len(B)):
        B[i] = A[i] + A[i - 1]

    return B


#Fourth function multiplies each value by 7
#[1,2,3,4] -> [7,14,21,28]
def easy4(A):
    B = []
    for number in A:
        B.append(number * 7)

    return B


#5th function cubed roots each value
#[1, 2, 8, 27] - > [1.0, ~1.26, 2.0, 3.0]]
def easy5(A):
    B = []
    for number in A:
        B.append(number ** (1/3))

    return B




#1st medium function is e^n / 2
#[1,2,3,4] - > [1.36, 3.69, 10.04, 27.30]

def medium1(A):
    B = []

    for number in A:
        B.append( (math.e ** number) / 2)


    return B


#This is nthroot(n) so
#[1,2,3,4,5] - > [1, 1.41, 1.44, 1.41, 1.37]
def medium2(A):
    B = []

    for number in A:
        B.append(number ** (1 / number))

    return B



#This multiplies each value by 1/2 its index so
#[1,2,3,4] - > [0, 1, 3, 6]
def medium3(A):
    B = []

    for i in range(len(A)):
        B.append(A[i] * (1/ 2) * i)

    return B


#This is (each value + 2) ^ 2 
#[1,2,3,4] -> [9, 16, 25, 36]
def medium4(A):
    B = []
    for number in A:
        B.append((number + 2) ** 2)


    return B




#This is each value * (the number behind + 4) (except the first)
#[1,2,3,4] -> [1, 10, 18, 28]
def medium5(A):
    B = A.copy()
    for i in range(1, len(A)):
        B[i] = A[i] * (A[i - 1] + 4)

    return B




#This is (number / (pi ^ e)) - index
#[1,2,3,4] -> [0.445, -0.911, -1.866, -2.8218]
def hard1(A):
    B = A.copy()

    for i in range(len(A)):
        B[i] = (A[i] / (math.pi ** math.e)) - i


    return B


#This is each number + 1.23 * (pi ^ (number * 3) / (5 * (index + 1)))
#[1,2,3,4] -> [8.62, 120.25, 2447.34, 56846.55]
def hard2(A):
    B = A.copy()

    for i in range(len(A)):
        B[i] = A[i] + 1.23 * (math.pi ** (A[i] * 3) / (5 * (i+1)))

    return B


#The equation here isnumber / (3.2^(pi - (1/2 number)))
#[1,2,3,4] ->  [0.046, 0.165, 0.445, 1.060]
def hard3(A):
    B = []
    for number in A:
        B.append(number / (3.2 ** (math.pi - (1/2) * number)))

    return B



#The equation here is ((n factorial / (e)) + 1928 - 3n)
#[1,2,3,4] -> [1925.368, 1922.7357, 1921.2072, 1924.8291]
def hard4(A):
    B = []
    for number in A:
        B.append((math.factorial(number) / math.e) + 1928 - (3 * number))

    return B


#This equation is 
#((Sum of every number except final - final number) ** 2) / (number* pi) + (number-1)!
def hard5(A):
    B = []
    all_values_but_final = sum(A) - A[len(A) - 1]
    final_value = A[len(A) - 1]
                    
    temp1 = all_values_but_final - final_value
    temp1 = temp1 ** 2

    for number in A:
        temp2 = number * math.pi + math.factorial(number - 1)

        final = temp1 / temp2
        B.append(final)

    return B

print(hard5([1,2,3,4]))