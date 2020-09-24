def compute_ave(list):
    sum = 0
    for td in list:
        sum+=td
    return float(sum)/len(list)

def compute_max(list):
    first=1
    max=0
    for td in list:
        if first==1: #루프 도는게 지금 처음이라면, first를 0으로 변경하고 리스트의 
            max=td   #처음 값을 max 값에 assign 하라. 
            first=0
        if max<td:
            max=td
    return max

if __name__ == "__main__":
    list_test=[10,20,30]
    print (compute_ave(list_test))
    print (compute_max(list_test))