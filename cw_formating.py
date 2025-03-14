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
    len_of_binary = len(binary)
    prime_set = set()        ##altered to a set to remove duplicates of decimal numbers

    ##Generation of substrings and simultenously convert them to decimals without storing them in a variable to reduce running time
    for i in range(len_of_binary):
        decimal = 0
        for j in range(i, len_of_binary):
            ##to effectively handle errors
            try:
                decimal = decimal * 2 + int(binary[j])        #convert each substring to a decimal

                if decimal > Number:        #break if the decimal is greater than the Number given to reduce running time
                    break  
                else:
                    prime = prime_number(decimal)

                #prime = prime_number(decimal)

                if prime is None:
                    pass

                elif prime is not None and prime < Number:
                    prime_set.add(decimal)

            except ValueError:
                return f"{0}: Invalid binary string."
            except Exception as e:
                print(f"An unexpected error occured: {e}")

    prime_list = list(prime_set)
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
print(substrings("1111111111111111111111111111111111111111", 999999))
end = time.time()
total_time = end - start
print(f"{total_time:.20f} seconds")
