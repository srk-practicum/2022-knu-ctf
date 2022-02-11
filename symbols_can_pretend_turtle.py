import turtle
turtle.speed("fastest")
turtle.hideturtle()


class ChainCodePicture:

    def __init__(self, codes, scale, color):
        self._codes = codes
        self._scale = scale
        self._color = color
        self._kkstr = codes[len(codes) - 1][0]
        self._x0 = -400
        self._y0 = (self._kkstr / 2 + 1) * self._scale

    def show(self):
        # turtle.setpos(self._x0, self._y0)

        for posl in self._codes:
            turtle.penup()
            y = self._y0 - posl[0] * self._scale
            x = self._x0 + (posl[1]) * self._scale
            # turtle.setpos(self._x0, self._y0)
            for n in range(posl[2]):

                turtle.setpos(x, y)
                turtle.setheading(0)
                turtle.pendown()
                turtle.color(self._color, self._color)
                turtle.begin_fill()

                for i in range(4):
                    turtle.fd(self._scale)
                    turtle.left(90)
                turtle.end_fill()
                x += self._scale
                turtle.penup()
        turtle.done()


class ChainCodeReader:
    def __init__(self, file_name):
        with open(file_name, 'r') as file:
            self.lines = file.readlines()
        self.index = 0
        self.bin_code = []
        i = 0
        for line in self.lines:
            self.bin_code += self.line_translate(i, line)
            i += 1

    @property
    def codes(self):
        return self.bin_code

    def line_translate(self, i, line):
        codes = []
        cur_index = 0
        while '*' in line[cur_index:]:
            code = [i, 0, 0]
            if '*' in line[cur_index:]:
                code[1] = line.find('*', cur_index)

            cur_index = code[1]
            if '.' in line[cur_index+1:]:
                code[2] = line.find('.', cur_index) - code[1]
            else:
                code[2] = len(line) - cur_index - 1
            codes.append(tuple(code))
            cur_index = line.find('.', cur_index)
        #print(codes)
        return codes

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.bin_code):
            raise StopIteration
        res = self.bin_code[self.index]
        self.index += 1
        return res


if __name__ == "__main__":
    # with open("C:/Users/User/Downloads/code.txt", "r") as file:
    #     encode = file.read()
    # encode = encode.replace("0", ".")
    # encode = encode.replace("1", "*")
    # code = ""
    # for i in range(0, 625, 25):
    #     code += (encode[i:i*25] + "\n")
    # with open("C:/Users/User/Downloads/code_turtle.txt", "w") as file:
    #     file.write(code)
    code = ChainCodeReader(r"C:/Users/User/Downloads/code_turtle.txt")
    paint = ChainCodePicture(code.codes, 10, 'black')
    paint.show()
