fp=open("data_score.csv","r",encoding="UTF8")

sum_w=0#여자합
sum_m=0#남자합
count_w=0 #여자 카운트 변수
count_m=0 #남자 카운트 변수
vun_m=0 #남자 제곱합 
vun_w=0 #여자 제곱합 
for line in fp:
    line=line.strip("\r\n")
    psd=line.split(",")
    name = psd[0]
    man = psd[1]
    height = psd[2]
    
    if man == "0": #여자 키 합 
        count_w+=1
        sum_w+=float(height)
        vun_w+= float(height)*float(height)
    else: #남자 키 합
        count_m+=1
        sum_m+=float(height)
        vun_m+=float(height)*float(height)
        
ave_m=sum_m/float(count_m)
ave_w=sum_w/float(count_w)

bun_m=(vun_m/float(count_m))-(ave_m**2) #남자 분산 
bun_w=(vun_w/float(count_w))-(ave_w**2) #여자 분산 

fout=open("result.txt","w")
fout.write("MAN\t%.2f\t%.2f\n"%(ave_m,bun_m))
fout.write("WOMAN\t%.2f\t%.2f\n"%(ave_w,bun_w))
fout.close()