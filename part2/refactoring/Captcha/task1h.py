class CaptchaNums:
    def __init__(self, nums):
        x = int(nums[0])
        y = int(nums[1])
        nums = nums[2:]
        long = len(nums)
        count = x * y
        lines = [nums[i:i+count] for i in range(0,long,count)]
        self.lst = [[line[i:i+x] for i in range(0,x*y,x)] for line in lines]

    def get_image_num(self, num):
        return '\n'.join(self.lst[num]) if num < len(self.lst) else num


nums = '24########.###.#.###.##.####.#.#######.#.####..###.##.######.##.#.##..########.##.'
nums = '35XXXX.XX.XX.XXXX..X.XXX.X..X..XXXX..X..X.X.XXX'

obj = CaptchaNums(nums)
num = int(input())
print(obj.get_image_num(num))


'''
можно сделать цифры с другими размерами
XXX
X.X
X.X
X.X
XXX

..X
.XX
X.X
..X
..X

XXX
..X
..X
.X.
XXX

XXXX.XX.XX.XXXX..X.XXX.X..X..XXXX..X..X.X.XXX
'''
