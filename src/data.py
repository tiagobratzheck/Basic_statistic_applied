#-------------------------------------Processing CSV
import pandas as pd

from processing import Processing

class Data():

    def __init__ (self):
        self.processing = Processing()
        self.file = pd.read_csv('file.csv')
        self.header = self.file.columns.tolist()
        self.option_list = []  
        self.list = []  

    def initialize(self):        
        index = len(self.header)
        print("Choose two options for statistical evaluation: \n")
        for i in range(0,index):
            print(i , " = " , self.header[i])
        self.selections(index)


    def selections(self, index):          
        try:
            choice = int(input())
            if choice >= index:
                print("Choose an element from the list ...")
                self.selections(index)    
            self.list.append(choice)
            if len(self.list) < 2:
                self.selections(index)
            else:
                self.controller(self.list)
        except ValueError:
            print("Select one of the above options (numeric value): ")
            self.selections(index)
        

    def controller(self, list):                             
        for x in list:
            self.option_list.append(self.header[x])

        index1 = self.file[self.option_list[0]]
        index2 = self.file[self.option_list[1]]
        
        self.processing.data_processing(index1, index2, self.option_list)
