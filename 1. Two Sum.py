from typing import *
import numpy as np

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = np.array(nums)
        for indx_1, number_1 in enumerate(nums):
            summed_array = nums + number_1
            mask = summed_array == target
            indxes = np.arange(len(nums),dtype=int)
            if len(indxes[mask]) == 0:
                continue
            else:
                indx_2 = indxes[mask][0]
            if indx_1 != indx_2:
                return [indx_1,indx_2]

                