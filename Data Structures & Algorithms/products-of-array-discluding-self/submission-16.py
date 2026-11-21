class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums[::-1]

        product = 1
        productAux = 1
        result = []
        countZero = 0

        for n in nums:            
            product *= n
            if n != 0:
                productAux *= n
            if n == 0:
                countZero += 1 
        
        for n in nums:
            if n == 0:
                if countZero >= 2:
                    result.append(product)
                else:
                    result.append(productAux)
            else:
                result.append(int(product / n))

        
        return result
