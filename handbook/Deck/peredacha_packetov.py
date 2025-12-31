import heapq

class Solution:
    def main(self):
        n, m = map(int, input().split())
        packets = [tuple(map(int, input().split())) for _ in range(n)]
        servers = [(0, i) for i in range(m)]

        heapq.heapify(servers)
        result = []

        for t, d in packets:
            ready_time, server_idx = heapq.heappop(servers)
            start = t if ready_time <= t else ready_time
            finish = start + d
            result.append(finish)

            heapq.heappush(servers, (finish, server_idx))

        print(" ".join(map(str, result)))

if __name__ == '__main__':
    solve = Solution()
    solve.main()