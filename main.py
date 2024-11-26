def longest_common_subsequence(X,Y):
    m = len(X)
    n = len(Y)
    # Initializing a matrix of size (m+1)*(n+1)
    dp = [[0] * (n + 1) for x in range(m + 1)]
    # Building dp[m+1][n+1] in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])

    # dp[m][n] contains length of LCS for X[0..m-1]
    # and Y[0..n-1]
    return dp[m][n]
if __name__ == "__main__":
    X = "CLOUD"
    Y = "LOUD"
    print("Length of LCS is", longest_common_subsequence(X,Y))
