import numpy as np # numpy 라이브러리를 끌어온다. 
class Discstat: # 설계도 즉, 클래스를 설정 
    def get_avg(self,list_data):
        sum =0
        for data in list_data:
            sum += data 
        return float(sum)/len(list_data)
    
    def get_std(self,list_data):
        ssum=0
        avg= self.get_avg(list_data)
        for data in list_data:
            ssum+=data*data
        
        dev=float(ssum)/len(list_data)-avg*avg #분산 
        return np.sqrt(dev) #표준편차 
    
class Teststat:
    name = "Test Stastistics"
    def t_test(self):
        return "t-Test"
    def get_name(self):
        return self.name
            

if __name__ == "__main__":
    ta= Teststat()
    print (ta.get_name())
    print (ta.name)
    