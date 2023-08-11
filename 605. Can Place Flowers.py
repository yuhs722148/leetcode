class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if i == 0:
                    flowerbed[1] = 1
                    i = 2
                if i == len(flowerbed) - 1:
                    flowerbed[i-1] = 1
                flowerbed [i-1] = 1
                flowerbed [i+1] = 1
                i = i+2
        return flowerbed.count(0) >= n
                