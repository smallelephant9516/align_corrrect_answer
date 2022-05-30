def align_sequence(s0, s1):
    # s1 is the true result, s0 is the input
    if s0 is None:
        raise TypeError("sequence 0 has no input.")
    if s1 is None:
        raise TypeError("sequence 1 has no input.")
    s0_len, s1_len = len(s0), len(s1)
    x, y = s0[:], s1[:]
    # create matrix
    matrix = [[0] * (s1_len + 1) for _ in range(s0_len + 1)]
    #DP, matrix[i][j] is the number of index that aligned between s0[:i],s1[:j]
    for i in range(1, s0_len + 1):
        for j in range(1, s1_len + 1):
            if x[i-1] == y[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    # bottom up to find aligned sequence 
    aligned_answer=[]
    aligned_index=[]
    maxi=s0_len
    maxj=s1_len
    for i in range(s0_len,0, -1):
        if i>maxi:
            continue
        for j in range(s1_len,0, -1):
            if j>maxj:
                continue
            if (matrix[i][j]>matrix[i][j-1]) & (matrix[i][j]>matrix[i-1][j]):
                aligned_answer.append(x[i-1])
                aligned_index.append(j-1)
                print(i,j,matrix[i][j])
                maxi=i
                maxj=j
    aligned_answer.reverse() #reverse the sequence of list, a function in python
    aligned_index.reverse()
    return matrix[-1][-1], aligned_answer, aligned_index


#user's steps
a=[1,1,3,5,4,4,1,2,6,8]

#correct answer
b=[1,2,3,4,5,6,7,8]

#a=[5,4,3,2,1]
#b=[1,2,3,4,5]
number,answer,index=align_sequence(b,a)
print('Total aligned sequence are %s, and the score would be %s' % (number, (number/len(a)*100)))
print('The result of the steps that aligned to the correct answers are',answer)
print('The index of the steps that aligned to the correct answer are',index)
