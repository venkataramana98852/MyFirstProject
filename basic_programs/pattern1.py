
def print_pattern(n):
    for i in range(n):
        for j in range(n):
            # Print '*' at the boundaries and the center
            if i == j or j==n or j==0 or i+j==n+1: #or j == 0 or j == n-1 or i+j == n+1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()   
print_pattern(7)        