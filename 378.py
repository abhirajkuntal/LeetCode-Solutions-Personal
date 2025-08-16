import heapq
def kth_smallest_elements_in_sorted_matrix(matrix , k):
    
    queue = []

    def push(i,j):

        if i < len(matrix) and j < len(matrix[0]) : 

            heapq.heappush(queue, [matrix[i][j],i,j])

    push(0,0)
    

    popped_element = 0

    while queue and popped_element < k-1:
        _,i,j = heapq.heappop(queue)
        popped_element += 1 
        push(i,j+1)

        if j == 0 :
            push(i+1, 0)
    res = heapq.heappop(queue)
    return matrix[res[1]][res[2]]

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print(kth_smallest_elements_in_sorted_matrix(matrix,k))

