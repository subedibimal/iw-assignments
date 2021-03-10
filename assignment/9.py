numbers = [1,2,3,5,6,7,9,13,16]
def binarySearch(arr: list[int],  l: int, r: int, x: int) -> int:
    
        if (r >= l):
            mid = int(l + (r - l) / 2)
    
            
            if (arr[mid] == x): 
                return mid
        
            if (arr[mid] > x): 
                return binarySearch(arr, l, mid - 1, x)
    
            return binarySearch(arr, mid + 1, r, x)
         
    
    
        return -1
    
