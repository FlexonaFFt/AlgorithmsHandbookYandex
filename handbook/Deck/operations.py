from collections import deque

def main():
    ored = deque()
    output = []
    b = int(input())
    for _ in range(b):

        line = list(map(int, input().split()))
        if line[0] == 1:
            ored.append(line[1])

        if line[0] == 2:
            ored.popleft()
        else: pass 

        if ored:
            output.append(str(ored[0]))
        else: output.append("-1")
    
    print('\n'.join(output))

if __name__ == '__main__':
    main()