class Solution:
    def findPages(self, arr, k):
        # code here
        n = len(arr)
        if k > n: return -1
        
        l = max(arr) #set max value in arr as start pointer 
        r = sum(arr) #sum of all value in arr as last as answer will lie in between
        ans = -1
        
        while l <= r:
            m = l + (r-l)//2
            
            if self.isvalid(arr,k,m):
                ans = m
                r = m - 1   #looking for small ans now
            else:
                l = m + 1 #got small now looking for big
        
        return ans
            
    def isvalid(self, arr, k , m):
        student = 1
        pages = 0
        
        for book in arr:
            if pages + book > m:  # if pages + boook is greater than our m than student will increase by 1 and their pages is set to current value
                student += 1
                pages  = book
                if student > k:
                    return False
            else:
                pages += book
                
        return True

if __name__ == "__main__":
    sol = Solution()
    arr = [12, 34, 67, 90]
    k = 2
    result = sol.findPages(arr, k)
    print(result)