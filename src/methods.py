#-------------------------------------Methods
import math
from collections import Counter


class Methods():

    def maxMin(self, index):
        return max(index), min(index)


    def mean(self, index):
        return sum(index) / len(index)

    
    def median(self, values):
        size = len(values) 
        order = sorted(values)
        if size % 2 == 1:
            z = int(math.floor(size / 2) )  
            return order[z]                  
        else:
            mean = (size / 2)      
            _mean = mean - 1         
            result = (order[int(mean)] + order[int(_mean)]) / 2
            return result


    def quant(self, index, p):
        p_index = int(p * len(index))     
        quant = sorted(index)[p_index]
        return p_index, quant
                        

    def mode (self, index):
        counter = Counter(index)    
        _max = max(counter.values())  
        if _max != 1:
            for x, count in counter.items():
                if count == _max:
                    return x
        else:
            return "There is no mode in the data set!"
            

    def data_range(self, values):        
        return max(values) - min(values)


    def _mean(self, x):
        mean = self.mean(x)
        return [for_each - mean for for_each in x]


    def variance(self, values):
        n = len(values)
        deviations = self._mean(values)
        return self.sum_of_squares(deviations, deviations) / (n - 1)


    def sum_of_squares(self, index1, index2):          
        return sum(x * y for x, y in zip(index1, index2))

    
    def standart_deviation(self, values):
        return math.sqrt(self.variance(values))

    
    #New standart deviation function.
    def std_deviation(self, _list):
        size_list = len(_list)        
        mean = sum(_list) / size_list    
        final = 0.00
        for value in _list:
            result = (value - round(mean, 2)) ** 2        
            final += round(result, 2)    
        dv = round(final, 4) / mean
        return math.sqrt(dv)


    def covariance(self, index1, index2):
        n = len(index1) 
        return self.sum_of_squares(self._mean(index1), self._mean(index2)) / (n - 1)


    def correlation(self, index1, index2):
        x = math.sqrt(self.variance(index1))
        y = math.sqrt(self.variance(index2))
        if x > 0 and y > 0:
            return self.covariance(index1, index2) / x / y
        else:
            return 0
