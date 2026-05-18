class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        print("left before the loop", left)
        print("right before the loop", right)
        print("start of search")
        while left <= right:
            middle = (left + right) // 2
            print("middle calculation at the Begin of the loop", middle)
            if(target == nums[middle]):
                print('middle if the target == nums[middle]', middle)
                return middle
            elif (target > nums[middle]):
                left = middle + 1
                print("right if target is less then middle", right)
            elif (target < nums[middle]):
                right = middle - 1
                print("left if the target is greater then middle", left)

            
        return -1