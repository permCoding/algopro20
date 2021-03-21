
class CaptchaNums:
    nums = '########.###.#.###.##.####.#.#######.#.####..###.##.######.##.#.##..########.##.'


    def __init__(self, num):
        self.num = num


    def get_image_num(self):
        lines = [self.nums[i:i+8] for i in range(0,80,8)]
        line = lines[self.num]
        lst = [line[i:i+2] for i in range(0,8,2)]
        return '\n'.join(lst)


obj = CaptchaNums(int(input()))
print(obj.get_image_num())
