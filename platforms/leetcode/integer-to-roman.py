class Solution:
    def intToRoman(self, num: int) -> str:
        representation = []

        count = num // 1000
        for i in range(count):
            representation.append('M')
        num = num % 1000
        if num >= 900:
            representation.append('C')
            representation.append('M')
        num = num % 900

        count = num // 500
        for i in range(count):
            representation.append('D')
        num = num % 500
        if num >= 400:
            representation.append('C')
            representation.append('D')
        num = num % 400

        count = num // 100
        if count <= 3:
            for i in range(count):
                representation.append('C')
        else:
            representation.append('C')
            representation.append('D')
        num = num % 100
        if num >= 90:
            representation.append('X')
            representation.append('C')
        num = num % 90

        count = num // 50
        for i in range(count):
            representation.append('L')
        num = num % 50
        if num >= 40:
            representation.append('X')
            representation.append('L')
        num = num % 40

        count = num // 10
        if count <= 3:
            for i in range(count):
                representation.append('X')
        else:
            representation.append('X')
            representation.append('L')
        num = num % 10
        if num == 9:
            representation.append('I')
            representation.append('X')
            num = 0

        count = num // 5
        for i in range(count):
            representation.append('V')
        num = num % 5

        count = num
        if count <= 3:
            for i in range(count):
                representation.append('I')
        else:
            representation.append('I')
            representation.append('V')

        return "".join(representation)