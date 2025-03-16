import time
import math

"Acts as a memory which stores every prime number in it to prevent repetition of prime check should a number be called more than once"
prime_counter = {}

"function to check a prime number"
def prime_number(n):
    if n in prime_counter:              ##if number is already in the prime_counter memory, it is returned straightaway
        return prime_counter[n]
    
    if n < 2 or (n % 2 == 0 and n > 2):             #if this condition is met, it is not added to the memory and it returns false.
        prime_counter[n] = False
        return False 
    
    if n == 2:
        prime_counter[n] = True
        return True
    
    for i in range(3, int(math.isqrt(n)) + 1, 2):       #condition checks a numbers from 3 to the approximated square root of n, checking odd numbers only
        if n % i == 0:
            prime_counter[n] = False
            return False
        
    prime_counter[n] = True 
    return True

# print(prime_number(11))


"function to check display the prime numbers less than number from a binary string"
def substrings(binary, Number):

    len_of_binary = len(binary)
    prime_set = set()                       ##stored in a set to remove duplicates


    ##Generation of substrings and simultenously convert them to decimals without storing for optimization
    for i in range(len_of_binary):
        decimal = 0
        for j in range(i, len_of_binary):
            try:
                decimal = decimal * 2 + int(binary[j])

                if decimal > Number:                #decimals greater than a given Number is unnecessary since this program checks primes less than the Number given
                    break

                else:
                    prime = prime_number(decimal)       #else, the decimal is checked using the prime_number function to determine if it is a prime or not


                if prime is True and prime < Number:        #if it is a prime, it is added to the prime set
                    prime_set.add(decimal)

            except ValueError:
                return f"{0}: Invalid binary string."
            except Exception as e:
                print(f"An unexpected error occured: {e}")      #error handling technique to prevent program from crashing incase of invalid entry

    prime_list = list(prime_set)                            #converts the set to a list to be sorted
    prime_list.sort()

    if len(prime_list) > 6:                             #if length of the primes are greater than 6, it outputs the first and last 3 of them using the slicing method
        large_prime_list = prime_list[0:3] + prime_list[-3:]
        return f"{len(large_prime_list)}: {large_prime_list}"
    
    else:                                               #else if it's 6 or lower, the entire primes are displayed
        return f"{len(prime_list)}: {prime_list}"


"To call the function and check the running time of the program" 
start = time.time()
print(substrings("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011", 12345678901234567890))
end = time.time()

total_time = end - start
print(f"{total_time:.20f} seconds")
