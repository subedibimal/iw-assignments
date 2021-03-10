def is_prime(num: int) -> bool:

    if num == 1:
        return False
    
    for i in range(3,int(num ** 1/2)):
        
        if num % i == 0:
            return False
        
    return True