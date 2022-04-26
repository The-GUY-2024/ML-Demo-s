
class weighted_mean():
    x = [1,2,3,4]
    w = [30,200,100,25]

    def __init__(self):
        self.DENOMINATOR = 0
        # N/D
        self.NUMERATOR = 0
        # after you divided the amount 
        self.TOTAL = 0
        self.w
        self.x
        self.numerator_calc();
        self.denominator_calc();\

        self.TOTAL = self.NUMERATOR/self.DENOMINATOR
        print("Numerator " + str( self.NUMERATOR ))
        
        print("___________________")

        print("Denominator " + str(self.DENOMINATOR ))
       
        print("=")
        
        print("total "+ str(self.TOTAL))

    def denominator_calc(self):
        for t in range(len(self.x)):
            self.DENOMINATOR  = self.DENOMINATOR + self.w[t]
        

    def numerator_calc(self):
        for t in range(len(self.w)):
            self.NUMERATOR = self.NUMERATOR + (self.w[t] * self.x[t]) 
        


weighted_mean()