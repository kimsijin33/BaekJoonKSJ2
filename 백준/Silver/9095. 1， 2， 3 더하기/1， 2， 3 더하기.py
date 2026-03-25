import sys

def solve_9095():
    # DP 테이블 초기화 (n은 최대 10까지)
    dp = [0] * 11
    dp[0] = 1 
    dp[1] = 1 
    dp[2] = 2 
    dp[3] = 4 

    # 점화식 적용: f(n) = f(n-1) + f(n-2) + f(n-3)
    for i in range(4, 11):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    # 테스트 케이스 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    T = int(input_data[0])
    for i in range(1, T + 1):
        n = int(input_data[i])
        print(dp[n])
        
if __name__ == "__main__":
    solve_9095()