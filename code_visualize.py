def is_prime(n:int)->bool:
    '''Check prime'''
    if n<= 1:
        return False
    for d in range(2,int(n**0.5)+1):
        if n%d == 0:
            return False
    return True 

is_prime(25)