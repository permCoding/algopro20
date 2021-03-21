
class CaptchaNums:
    d = [
        ['##', '##', '##', '##'],
        ['.#', '##', '.#', '.#'],
        ['##', '.#', '#.', '##'],
        ['##', '.#', '.#', '##'],
        ['##', '##', '.#', '.#'],
        ['##', '#.', '.#', '##'],
        ['.#', '#.', '##', '##'],
        ['##', '.#', '#.', '#.'],
        ['##', '..', '##', '##'],
        ['##', '##', '.#', '#.']
    ]


    def __init__(self, num):
        self.num = num


    def get_image_num(self):
        return '\n'.join(self.d[self.num])


obj = CaptchaNums(int(input()))
print(obj.get_image_num())
