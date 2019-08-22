'''Emulate G65 macro to analyze macro assignment'''


class Macro():
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
