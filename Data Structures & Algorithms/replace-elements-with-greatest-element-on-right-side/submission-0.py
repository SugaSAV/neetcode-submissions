class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lastValue = -1
        for i in range(len(arr) -1, -1, -1):
            newValue = max(lastValue , arr[i])
            arr[i] = lastValue
            lastValue = newValue
        return arr

         

        