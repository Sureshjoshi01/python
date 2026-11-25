#Write a code to create a new list using odd-indexed elements from the first list and even-indexed elements from the second.


def new_lst(l1,l2):
    l3 = []
    l4 = []
    l5 = []

    for i in range(len(l1)):
        if i % 2 != 0:
            l3.append(l1[i])

    print("Element at odd-index positions from list one")
    print(l3)
    for i in range(len(l2)):
        if i % 2 == 0:
            l4.append(l2[i])

    print("Element at even-index positions from list one")
    print(l4)
    for i in l3:
        l5.append(i)
    for i in l4:
        l5.append(i)
    print("Printing Final third list")
    print(l5)

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
new_lst(l1,l2)
