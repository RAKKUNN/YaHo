N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back":
        num.append(int(line[1]))
    elif line[0] == "get":
        # 1번 인덱스가 리스트의 0번 인덱스에 대응되므로 -1을 해줍니다.
        print(num[int(line[1]) - 1])
    elif line[0] == "pop_back":
        num.pop()  
    elif line[0] == "size":
        print(len(num))
    else:
        num.append(0)