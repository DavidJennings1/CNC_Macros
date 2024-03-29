'''Emulate G65 macro to analyze macro assignment'''

import math


class Macro:
    def __init__(self, var5003, var4001, var4003, var24, var25, var18, var26,
                 var2, var9, var17, var3, var23):
        self.var5003 = var5003  # Previous Z
        self.var4001 = var4001  # G0 or G1 from previous code
        self.var4003 = var4003  # G90 or G91 from previous code
        self.var24 = var24  # X from macro call
        self.var25 = var25  # Y from macro call
        self.var18 = var18  # R from macro call
        self.var26 = var26  # Z from macro call
        self.var2 = var2  # B from macro call
        self.var9 = var9  # F from macro call
        self.var17 = var17  # Q from macro call
        self.var3 = var3  # C from macro call
        self.var23 = var23  # W from macro call
        self.var100 = self.var5003  # Store original Z for end of file
        self.var101 = self.var4001  # Store original G1 or G0 for end of file
        self.var102 = self.var4003  # Store original G90 or G91 for end of file

    def generate_gcode(self):
        if self.var5003 >= self.var18:
            ln1 = 'G0G90X{}Y{}'.format(self.var24, self.var25)
            print(ln1)
        else:
            ln1 = 'G0G90Z{}'.format(self.var18)
            ln2 = 'G0G90X{}Y{}'.format(self.var24, self.var25)
            print(ln1)
            print(ln2)
        var103 = self.var23-(self.var26+.025)
        var104 = math.ceil(var103/(self.var17*(-1)))
        var105 = (var103/var104)
        var106 = (self.var2/2)
        var107 = 1
        ln3 = 'G1G90Z{}F200.'.format(self.var26+.025)
        print(ln3)
        var108 = (self.var26+.025)
        # var109 = .01
        # var110 = 2*((var106-var109)/var106)
        # var111 = self.var9*var110
        ln4 = 'G1G41D#518X{:.4f}F20.'.format(self.var24+var106)
        print(ln4)
        while (var107 < (var104+1)):
            ln5 = 'G3I-{:.4f}Z{:.4f}F{:.2f}'.format(var106,
                                                    var108+(var107*var105),
                                                    self.var9)
            var107 += 1
            print(ln5)
        ln6 = 'G3I-{:.4}'.format(var106)
        ln7 = 'G3X{}Y{}R{}F{}'.format(self.var24-(var106-.01), self.var25,
                                      var106-.005, self.var9*2)
        ln8 = 'G1G40X{}Y{}'.format(self.var24, self.var25)
        print(ln6)
        print(ln7)
        print(ln8)
        # print(var111)
        if self.var3 == 1:
            if self.var100 >= self.var18:
                ln9 = 'G0Z{}'.format(self.var100)
                print(ln9)
            else:
                ln9 = 'G0Z{}'.format(self.var18)
                print(ln9)
        else:
            var107 = (var107-2)
            ln10 = 'G1G42D#518X{}Y{}F{}'.format(self.var24-(var106-.01),
                                                self.var25, self.var9)
            print(ln10)
            ln11 = 'G2X{}Y{}R{}F{}'.format((self.var24+var106), self.var25,
                                           (var106-.005), self.var9)
            print(ln11)
            while var107 > -1:
                ln12 = 'G2I-{}Z{:.4}'.format(var106, var108+(var107*var105))
                print(ln12)
                var107 += -1
            ln13 = 'G1G40X{}Y{}F{}'.format(self.var24, self.var25,
                                           (self.var9*2))
            print(ln13)
            if self.var100 >= self.var18:
                ln9 = 'G0Z{}'.format(self.var100)
                print(ln9)
            else:
                ln9 = 'G0Z{}'.format(self.var18)
                print(ln9)
        ln15 = 'G{}'.format(self.var101)
        ln16 = 'G{}'.format(self.var102)
        print(ln15)
        print(ln16)
        self.var100 = 0
        self.var101 = 0
        self.var102 = 0
        var103 = 0
        var104 = 0
        var105 = 0
        var106 = 0
        var107 = 0
        var108 = 0
        # var109 = 0
        # var110 = 0
        # var111 = 0


g65 = Macro(2.25, 0, 90, 5.8893, 9.647, .3182, .3182, .5, 5., .1, 0, -.0203)
g65.generate_gcode()
