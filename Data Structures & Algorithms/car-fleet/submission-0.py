class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse =True)
        time = []
        stack = []
        for pos, sp in cars:
            time.append((target - pos)/sp)

        for i in range(len(time)):
            if i == 0:
                stack.append(time[i])
            else:
                if time[i] > stack[-1]:
                    stack.append(time[i])
                else:
                    continue
        return len(stack)



        