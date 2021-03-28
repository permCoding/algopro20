import re

class CaptchaNums:
    nums = '########.###.#.###.##.####.#.#######.#.####..###.##.######.##.#.##..########.##.'


    def __init__(self, num):
        self.num = num


    def get_image_num(self):
        i = self.num*8
        line = self.nums[i:i+8]
        # lst = re.findall('..', line) # 1 -> ['.#', '##', '.#', '.#']
        lst = re.findall('[.#]{2}', line) # 1 -> ['.#', '##', '.#', '.#']
        return '\n'.join(lst)


obj = CaptchaNums(int(input()))
print(obj.get_image_num())
