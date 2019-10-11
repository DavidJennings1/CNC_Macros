'''Emulate G65 macro to analyze CYCLE189 macro assignment'''

import math


class Macro:
    def __init__(self, b_size, x_pos, y_pos, r_pln, z_top,
                 f_rate, z_bot, step):
        self.r2 = b_size  # B from macro call
        self.r24 = x_pos  # X from macro call
        self.r25 = y_pos  # Y from macro call
        self.r18 = r_pln  # R from macro call
        self.r26 = z_top  # Z from macro call
        self.r9 = f_rate  # F from macro call
        self.r17 = step  # Q from macro call
        self.r23 = z_bot  # W from macro call

    def generate_gcode(self):
        r103 = self.r23-(self.r26+.025)
        # print('r103', r103)
        r104 = math.ceil(r103/(self.r17*(-1)))
        print('r104', r104)
        r105 = (r103/r104)
        # print('r105', r105)
        r106 = (self.r2/2)
        # print('r106', r106)
        r108 = self.r26+.025
        # print('r108', r108)
        r107 = 1
        r109 = (self.r2/4)
        ln3 = 'G0G90X{}Y{}'.format(self.r24, self.r25)
        ln4 = 'G0G90Z{:.4f}'.format(self.r18)
        ln5 = 'G1Z{:.4f}F100.'.format(r108)
        ln6 = 'G1X{}F{:.2f}'.format(self.r24+r106, self.r9*2)
        print(ln3)
        print(ln4)
        print(ln5)
        print(ln6)
        while (r107 < (r104+1)):
            ln7 = 'G3I{:.4f}J0.0Z{:.4f}F{:.2f}'.format(r106*(-1),
                                                       r108+(r107*r105),
                                                       self.r9)
            r107 += 1
            print(ln7)
        ln8 = 'G3I{:.4f}J0.0'.format(r106*(-1))
        ln9 = 'G3X{}Y{}I{}J0.0F{:.2f}'.format(self.r24+r109, self.r25+r109,
                                              r109*(-1), self.r9*2)
        ln10 = 'G1X{}Y{}'.format(self.r24, self.r25)
        print(ln8)
        print(ln9)
        print(ln10)
        r107 = r107-2
        ln11 = 'G1X{}Y{}F{:.2f}'.format(self.r24+r109, self.r25+r109,
                                        self.r9*2)
        ln111 = 'G2X{}Y{}I0.0J{}F{:.2f}'.format(self.r24+r106, self.r25,
                                                r109*(-1), self.r9)
        print(ln11)
        print(ln111)
        while r107 > -1:
            ln12 = 'G2I{:.4f}J0.0Z{:.4f}F{:.2f}'.format(r106*(-1),
                                                        r108+(r107*r105),
                                                        self.r9)
            print(ln12)
            r107 += -1
        ln13 = 'G1X{}Y{}F{:.2f}'.format(self.r24, self.r25, (self.r9*2))
        print(ln13)
        ln14 = 'G0G90Z{:.4}'.format(self.r18)
        print(ln14)
        print('M17')


g65 = Macro(.5, 5.8893, 10.2375, .4182, .3182, 5, -.0203, .1)
g65.generate_gcode()
