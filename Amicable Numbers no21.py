



amicable_numbers_list = []

amicable_numbers_sum = 0


def proper_devisors(i):
    devisor_sum = 0
    n = 2
    #base case of 1
    if i == 1:
        return 1
    #base case of 2
    elif i == 2:
        return 3
    
    while n<i:
        if i%n==0:
            devisor_sum += n
        n += 1
    return devisor_sum + 1

def amicable_pair(a,b):
    
    if proper_devisors(a) == b and proper_devisors(b)== a and a!=b:
        amicable_numbers_list.append(a)
    else:
        pass



for n in range(1,10000):
    devisor_sum = proper_devisors(n)
    amicable_pair(n, devisor_sum)    

print(amicable_numbers_list)
for i in amicable_numbers_list:
    amicable_numbers_sum += int(i)

print(amicable_numbers_sum)
