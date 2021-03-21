
class CaptchaNums:
    nums = '########.###.#.###.##.####.#.#######.#.####..###.##.######.##.#.##..########.##.'


    def __init__(self, num):
        self.num = num


    def get_image_num(self):
        i = self.num*8
        line = self.nums[i:i+8]
        lst = [line[i:i+2] for i in range(0,8,2)]
        return '\n'.join(lst)


obj = CaptchaNums(int(input()))
print(obj.get_image_num())
