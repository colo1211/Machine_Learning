def rsorted (th): #dhash를 th파라미터로 전달받음
    return sorted(th,key=th.get,reverse=True) 
#sorted는 인자를 1~3개까지 가질 수 있다. 
#필수: 먼저 th인 Index는 반드시 있어야 한다. th하나만 쓸 경우, 이름을 기준으로 오름차순으로 
#정렬된다. 
#(선택)두번째 인자, key=th.get을 추가할 경우 value값을 기준으로 정렬하기 원할때 사용한다. 
#여기서는 value값을 기준으로 정렬하기 위해 key=th.get인자를 추가하였다. 
#(선택)세번째 인자, reverse는 내림차순으로 정렬하기 위해 추가한 부울자료형이다. 
# 만약 reverse 인자를 추가하지 않을 경우는 자동으로 오름차순 정렬을 시행한다. 

dhash={} #딕셔너리를 선언 
fp=open("data_log.csv","r",encoding="UTF8") #파일 읽기모드로 파일을 오픈 
for line in fp: #파일 전체를 loop를 돌게한다. 
    line=line.strip("\r\n") #파일내에 있는 데이터(문자열)에 보이지 않는 개행문자와 띄어쓰기 제거 
    psd = line.split(",") #문자열로 존재하는 데이터를 "," 를 기준으로 리스트 psd로 저장한다. 
    query = psd[1] #psd리스트의 첫번째 요소(이름)을 query(문자열)에 저장한다. 
    
    if not query in dhash: #dhash안에 이름 데이터가 없다면, 
        dhash[query]=0 #value는 0으로 설정해준다. key를 추가해주는 역할
    
    dhash[query]+=1 #있으면 1씩 증가 
    
fp.close() #파일 클로즈 

sorted_list=rsorted(dhash) #딕셔너리를 resorted함수로 전달된 데이터를 sorted_list에 저장

for query in sorted_list: #sorted_list를 모두 돌면서 변수 query에 담고 그에 해당하는 key값을 출력
    print (query,dhash[query])