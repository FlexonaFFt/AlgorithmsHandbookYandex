import sys

def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:]  

    ans = [0] * n
    st = []  

    for i, x in enumerate(a):
        while st and a[st[-1]] < x:
            st.pop()

        if not st:
            ans[i] = i
        else:
            ans[i] = i - st[-1] - 1

        st.append(i)

    sys.stdout.write(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
