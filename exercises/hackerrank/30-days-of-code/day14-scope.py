class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    maximumDifference = 0
    def computeDifference(self):
        l = len(a)
        self.maximumDifference = abs(max(a) - min(a))

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)