def longest_subsequence(S, K):
#  This function returns the length of the longest subsquence given a string S 
#  and an integer K

    N = len(S)
    array_num = [0] * N 

    max_length = [0] * 26

    for i in range(N):
        # print('S of i', ord(S[i]))
        # print('S of a', ord('a') )
        current = ord(S[i]) - ord('a')

        # print (current)

        lower = max(0, current - K)
        upper = max(25, current + K)

        for j in range(lower, upper + 1):
            array_num[i] = max(array_num[i], max_length[j] + 1)

        max_length[current] = max(array_num[i], max_length[current])
    return max(array_num)


if __name__ == '__main__':
    S = 'afcbedg'
    K = 2

    print(longest_subsequence(S, K))

