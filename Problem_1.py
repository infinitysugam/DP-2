# In this case we use DP to solve it.
# We calculate the amount required for each and every for each and every color.
# It the repeated problem is already solved we just use the previous calculated value
# Time Complexity = O(n)
# Space Complexity = O(n)

def PaintHouse(costs):
    m = len(costs)
    n = len(costs[0])

    dp_matrix = [[None for i in range(0,n)] for j in range(0,m)]

    for i in range(0,n):
        dp_matrix[m-1][i] = costs[m-1][i]


    for i in range(m-2,-1,-1):
        dp_matrix[i][0] = costs[i][0] + min(dp_matrix[i+1][1],dp_matrix[i+1][2])
        dp_matrix[i][1] = costs[i][1] + min(dp_matrix[i+1][0],dp_matrix[i+1][2])
        dp_matrix[i][2] = costs[i][2] + min(dp_matrix[i+1][0],dp_matrix[i+1][1])



    return min(dp_matrix[0][0],min(dp_matrix[0][1],dp_matrix[0][2]))




