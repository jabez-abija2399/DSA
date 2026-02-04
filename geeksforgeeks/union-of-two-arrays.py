class Solution:    
    def findUnion(self, a, b):
        # code here
        
        unqUnion = set(a+b)
        list(unqUnion).sort()
        return unqUnion