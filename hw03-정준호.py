L = [2,19,18,14,2,17,7,14,4,15]         #주어진 리스트

print("리스트 원소 개수 입력 : 10")
print("리스트 : [2,19,18,14,2,17,7,14,4,15]")
obj=int(input("목표값 입력 : "))
p_obj= "두 수의 합이 {}".format(obj) + "인 원소 쌍"
print(p_obj)

p1 = 0              #리스트의 포인터 역할을 할 변수1(리스트 인덱싱 번호)
p2 = 1              #리스트의 포인터 역할을 할 변수2(리스트 인덱싱 번호)


while p1<len(L)-1:
    if L[p1]+L[p2] == obj:
        print("{}번째와 ".format(p1+1) + "{}번째 원소".format(p2+1))

        p2=p2+1
        continue
    else:
        if p2>=len(L)-1:
            p1=p1+1
            p2=p1+1
            continue
        else:
            p2=p2+1
            continue


import random
print("\n\n\n")
print("☆리스트 원소 개수를 입력받고 리스트의 원소들이 랜덤으로 주어졌을 때☆")
print(" * 1~20까지의 숫자들 중 랜덤으로 리스트의 원소가 됩니다.\n")
Ln=int(input("리스트 원소 개수 입력 : "))            #랜덤 리스트 원소 개수
L_R = []

for i in range(1,Ln+1):
    L_R.append(random.randrange(1,20))
print("리스트 : {}".format(L_R))
obj=int(input("목표값 입력 : "))
p_obj= "두 수의 합이 {}".format(obj) + "인 원소 쌍"
print(p_obj)

p3 = 0              #리스트의 포인터 역할을 할 변수1(리스트 인덱싱 번호)
p4 = 1              #리스트의 포인터 역할을 할 변수2(리스트 인덱싱 번호)


while p3<len(L_R)-1:
    if L_R[p3]+L_R[p4] == obj:
        print("{}번째와 ".format(p3+1) + "{}번째 원소".format(p4+1))

        p4=p4+1
        continue
    else:
        if p4>=len(L_R)-1:
            p3=p3+1
            p4=p3+1
            continue
        else:
            p4=p4+1
            continue
