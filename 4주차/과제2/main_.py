import statpy as st
fp= open ("data.csv","r",encoding="UTF8")

da=st.Discstat() # 클래스에서 설정한 설계도를 따라 객체 1개를 설정한다. 
list_data=[]
for line in fp:
    line = line.strip("\r\n")
    fd = line.split(",")
    man = fd[1]
    height = fd[2]
    if man == "1":
        list_data.append(float(height))

a= da.get_avg(list_data)
b= da.get_std(list_data)
print("평균:", a)
print("표준편차:",b)

    


        

