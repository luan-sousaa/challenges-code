from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for indice,numero in enumerate(nums):
            if hasher.get(numero) is not None:
                return [hasher.get(numero), indice]
            else:
                hasher[target - numero] = indice
lista_numero = [2, 6, 11, 15 , 7]
target = 9
print(Solution().twoSum(lista_numero, target))