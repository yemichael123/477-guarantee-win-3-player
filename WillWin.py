def WillWin(a, b, c, n):
    #this initalizes memo[1...n], where each index contains at most 3 numbers
    #0's are just empty numbers in this case

    memo = [set([0]) for y in range(n + 1)]
    if min(a, b, c) > n:
        return 1
    for i in range(min(a,b,c)):
        memo[i] = set([3])
    for i in range(min(a,b,c), n + 1):
        #check for out of bounds
        if i - a >= 0:
            memo_i_minus_a = memo[i - a]
        else:
            memo_i_minus_a = set([])
        if i - b >= 0:
            memo_i_minus_b = memo[i - b]
        else:
            memo_i_minus_b = set([])
        if i - c >= 0:
            memo_i_minus_c = memo[i - c]
        else:
            memo_i_minus_c = set([])

        #print(i)
        #print((memo_i_minus_a.union(memo_i_minus_b, memo_i_minus_c)))

        if memo_i_minus_a.union(memo_i_minus_b, memo_i_minus_c) == set([0]):
            memo[i] = memo[i - 1].union(memo[i - 2], memo[i - 3])
            continue
        if set([2]) == (memo_i_minus_a.union(memo_i_minus_b, memo_i_minus_c)):
            memo[i] = set([3])
        elif set([3]) == (memo_i_minus_a.union(memo_i_minus_b, memo_i_minus_c)):
            memo[i] = set([1])
        elif set([1]) == (memo_i_minus_a.union(memo_i_minus_b, memo_i_minus_c)):
            memo[i] = set([2])
        elif (1 in memo_i_minus_a or 1 in memo_i_minus_b or 1 in memo_i_minus_c) and (3 in memo_i_minus_a or 3 in memo_i_minus_b or 3 in memo_i_minus_c):
            memo[i] = set([1, 2])
    '''
    player3Win = []
    a_b_c = [a, b, c]
    counter = 0
    for i in range(3):
        for j in range(3):
            if n - a_b_c[i] - a_b_c[j] >= 0:
                player3Win.append(memo[n - a_b_c[i] - a_b_c[j]])
    '''
    print("MEMO LIST")
    for i in memo:
        print(list(i))
    player2Win = set([])
    a_b_c = [a, b, c]
    counter = 0
    for i in range(3):
        if n - a_b_c[i] >= 0:
            player2Win = player2Win.union(memo[n - a_b_c[i]])
            #print(memo[n - a_b_c[i]])
    #print("MEMO")
    #print(memo[n])
    if memo[n] != set([3]) and memo[n] != set([2]) and 1 in player2Win or 2 in player2Win or set([]) == player2Win:
        print("My algorithm: You cannot win with a fixed strategy")
        return 1
    else:
        print("My algorithm: You have a strategy to win!!!")
        return 0
    '''
    if 1 in player2Win or 3 in player2Win or set([]) == player2Win:
        print("My algorithm: You have a strategy to win!!!")
        return 0
    else:
        print("My algorithm: You cannot win with a fixed strategy")
        return 1
    '''
    '''
    if memo[n] == set([3])
        print("My algorithm: You cannot win with a fixed strategy")
        return 1
    else:
        print("My algorithm: You have a strategy to win!!!")
        return 0
    '''

def solutionAlgorithm(a, b, c, n):
    memo = [True for i in range(n + 1)]
    for i in range(n + 1):
        memo[i] = ((i >= a and not memo[i - a]) or (i >= b and not memo[i - b]) or (i >= c and not memo[i - c]))

    if memo[n] == False:
        print("Solution's algorithm: You cannot win with a fixed strategy")
        return 1
    else:
        print("Solution's algorithm: You have a strategy to win!!!")
        return 0


def main():
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for n in range(1, 10):
                    if min(a,b,c) <= n:
                        print("===========================")
                        print("Testing (" + str(a) + ", " + str(b) + ", " + str(c) + ", " + str(n) + ")")
                        mySol = WillWin(a, b, c, n)
                        ansSol = solutionAlgorithm(a, b, c, n)
                        if mySol != ansSol:
                            print("==============DIFFERENCE DETECTED================")
if __name__ == "__main__":
    main()


