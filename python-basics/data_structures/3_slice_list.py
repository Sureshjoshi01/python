#Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk1 = sample_list[0:3]
print("Chunk  1 ", chunk1)
reverse_chunk1 = chunk1[::-1]
print("After reversing it ", reverse_chunk1) 

chunk2 = sample_list[3:6]
print("Chunk  2 ", chunk2)
reverse_chunk2 = chunk2[::-1]
print("After reversing it ", reverse_chunk2) 


chunk3 = sample_list[6:]
print("Chunk  3 ", chunk3)
reverse_chunk3 = chunk3[::-1]
print("After reversing it ", reverse_chunk3) 

