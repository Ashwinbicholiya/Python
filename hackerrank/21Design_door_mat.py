N = int(input())
if N%2!=0:
    M=3*N
    print('M is',M)

pattern = [('.|.'*(2*i+1)).center(M, '-') for i in range(N//2)]
print('\n'.join(pattern + ['Welcome'.center(M,'-')]+ pattern[::-1]))

