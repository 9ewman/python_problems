# find left median of union of two sorted sequences with length l


def union_median(seq_1, seq_2, l):
    def left_place(seq, num, l):
        if num <= seq[0]:
            return 0
        left = 0
        right = l - 1
        while left < right:
            mid = (left + right + 1) // 2
            if seq[mid] < num:
                left = mid
            else:
                right = mid - 1
        return left + 1

    def right_place(seq, num, l):
        if num >= seq[l - 1]:
            return l
        left = 0
        right = l - 1
        while left < right:
            mid = (left + right) // 2
            if seq[mid] > num:
                right = mid
            else:
                left = mid + 1
        return left

    def check_seq_1(seq_1, seq_2, l):
        left = 0
        right = l - 1
        while left < right:
            mid = (left + right + 1) // 2
            if left_place(seq_2, seq_1[mid], l) + mid + 1 <= l:
                left = mid
            else:
                right = mid - 1
        if right_place(seq_2, seq_1[left], l) + left + 1 >= l and left_place(seq_2, seq_1[left], l) + left + 1 <= l:
            return left
        else:
            return -1

    median_1 = check_seq_1(seq_1, seq_2, l)
    if median_1 != -1:
        return seq_1[median_1]
    else:
        return seq_2[check_seq_1(seq_2, seq_1, l)]


n, l = tuple(map(int, input().split()))
seqs = []
for i in range(n):
    seqs.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i + 1, n):
        print(union_median(seqs[i], seqs[j], l))
