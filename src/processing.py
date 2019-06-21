#-------------------------------------Data processing
from methods import Methods


class Processing():


    def __init__(self):
        self.methods = Methods()


    def data_processing(self, index1, index2, option_list):
        self.showdata(index1, index2, option_list)
        self.maxmin(index1, option_list)
        self.maxmin(index2, option_list)
        self.mean(index1, index2, option_list)
        self.medi(index1, index2, option_list)
        self.quant(index1, option_list[0])
        self.quant(index2, option_list[1])
        self.mode(index1, index2, option_list)
        self.dis(index1, index2, option_list)
        self.var(index1, index2, option_list)
        self.covar(index1, index2)
        self.correlation(index1, index2)

    
    def showdata(self, index1, index2, option_list):
        pass


    def maxmin(self, index, option_list):
        maxi, mini = self.methods.maxMin(index)        
        print("Maximum set value: " + str(maxi) + ". Minimum value: " + str(mini) + "\n")
                

    def mean (self, index1, index2, option_list):
        result1 = self.methods.mean(index1)
        result2 = self.methods.mean(index2)
        print("Average value for  " + option_list[0] + ": " + str(result1))
        print("Average value for  " + option_list[1] + ": " + str(result2) + "\n")

    
    def medi (self, index1, index2, option_list):
        result1 = self.methods.median(index1)
        result2 = self.methods.median(index2)
        print("Median value for  " + option_list[0] + ": " + str(result1))
        print("Median value for  " + option_list[1] + ": "+ str(result2)+ "\n")

    
    def quant (self, index, option_list):
        index25, result25 = self.methods.quant(index, 0.25)
        index50, result50 = self.methods.quant(index, 0.50)
        index75, result75 = self.methods.quant(index, 0.75)        
        print(str(index25) + " (25%) values ​​in the data set: " 
        + str(option_list) + ", are less than the value: " 
        + str(result25) + " in a set of: " + str(len(index)) + " data." )
        print(str(index50) + " ( 50% ) values ​​in the data set: "
        + str(option_list) + ", are less than the value:: " 
        + str(result50) + " in a set of: " + str(len(index)) + " data." )
        print(str(index75) + " ( 75% ) values ​​in the data set: "
        + str(option_list) + ", are less than the value: " 
        + str(result75) + " in a set of: " + str(len(index)) + " data." + "\n")    


    def mode(self, index1, index2, option_list):
        result1 = self.methods.mode(index1)
        result2 = self.methods.mode(index2)
        print("Mode for " + option_list[0] + ": " + str(result1))
        print("Mode for " + option_list[1] + ": " + str(result2) + "\n")


    def dis(self, index1, index2, option_list):
        result1 = self.methods.data_range(index1)
        result2 = self.methods.data_range(index2)
        print("dispersion for " + option_list[0] + ": " + str(result1))
        print("dispersion for " + option_list[1] + ": " + str(result2) + "\n")


    def var(self, index1, index2, option_list):
        result1 = self.methods.variance(index1)
        result2 = self.methods.variance(index2)
        print("The variance for " + option_list[0] + ": " + str(result1))
        print("The variance for " + option_list[0] + ": " + str(result2) + "\n")


    def covar(self, index1, index2):
        result = self.methods.covariance(index1, index2)
        print("The variance between the two sets in relation to their means is: " + str(round(result,2)) + "\n")


    def correlation(self, index1, index2):
        result = self.methods.correlation(index1, index2)
        print("The correlation between the two datasets: " +str(round(result, 3)) + "\n")
