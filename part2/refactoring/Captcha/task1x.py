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
        try:
            res = '\n'.join(self.lst[num])
        except:
            res = num
        return res


with open('dicts.ini') as f:
    dicts = f.read().splitlines()

num_dict = 1
obj = CaptchaNums(dicts[num_dict])
num = int(input())
print(obj.get_image_num(num))
