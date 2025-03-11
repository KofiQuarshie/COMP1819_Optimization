import time
import math

def prime_number(n):
    if n < 2 or (n % 2 == 0 and n > 2):
        return
    if n == 2:
        return n
    for i in range(3, int(math.sqrt(n)) + 1, 2):  
        if n % i == 0:
            return
    return n  

# print(prime_number(11))

def substrings(binary, Number):
    substrings = set()
    len_of_binary = len(binary)

    for i in range(len_of_binary):
        substring = ""
        for j in range(i, len_of_binary):
            substring += binary[j]
            substrings.add(substring)

    decimal_substrings = set()
    for sub in substrings:
        try:
            decimal = int(sub, 2)
            decimal_substrings.add(decimal)
        except ValueError:
            return f"{0}: Invalid binary string."
        except Exception as e:
            print(f"An unexpected error occured: {e}")
        
    prime_list = []

    for n in decimal_substrings:
        prime = prime_number(n)
        #print(prime)

        if prime is None:
            pass

        elif prime is not None and prime < Number:
            prime_list.append(prime)
    prime_list.sort()

    if len(prime_list) > 6:
       # print(substrings_list)
       # print(decimal_list)
        large_prime_list = prime_list[0:3] + prime_list[-3:]
        return f"{len(large_prime_list)}: {large_prime_list}"
    
    else:
        #print(substrings_list)
        #print(decimal_list)
        return f"{len(prime_list)}: {prime_list}"



start = time.time()
print(substrings("010000110100111101001101010100000011000100111000001100010011100100100001", 123456789012345678))
end = time.time()
total_time = end - start
print(f"{total_time:.20f} seconds")