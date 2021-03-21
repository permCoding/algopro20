class CaptchaNums:
    def __init__(self, file_name, num_dict):
        nums = self.get_dict(file_name, num_dict)
        x = int(nums[0])
        y = int(nums[1])
        nums = nums[2:]
        long = len(nums)
        count = x * y
        lines = [nums[i:i+count] for i in range(0,long,count)]
        self.lst = [[line[i:i+x] for i in range(0,x*y,x)] for line in lines]


    def get_dict(self, file_name, n):
        with open(file_name) as f:
            dicts = f.read().splitlines()
            return dicts[n-1] # переводим в нумерацию компьютера


    def get_image_num(self, num):
        try:
            res = '\n'.join(self.lst[num])
        except:
            res = num
        return res