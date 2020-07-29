grade=[92, 88, 86, 78, 98, 100, 72, 68, 90]

def list_hap(alist) :
    hap = 0
    for i in alist :
        hap = hap + i
    return hap

def list_over(ave,alist) :
    cnt = 0
    for i in alist :
        if i > ave :
            cnt = cnt + 1
    return cnt

hap = list_hap(grade)
ave = list_hap(grade)//len(grade)

print('총점 : ', hap)
print('평균 : ', ave)
print('성적이 평균 이상인 학생의 수 : ', list_over(ave, grade))
