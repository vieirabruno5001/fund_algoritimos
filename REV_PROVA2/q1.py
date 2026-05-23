N = int(input())

M = []

for i in range(N):
    R = []
    for j in range(N):
        R.append((i + j + 1))
    M.append(R)
for i in range(N):
    for j in range(N):
        print(f"{M[i][j]:4}", end=" ")
    print()