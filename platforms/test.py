nums3 = [2, 2, 2, 1]
nums4 = [2, 2, 2, 2, 2, 2, 2, 1, 1, 3, 4, 5, 6, 7]
duplicates = []
duplicates2 = []
for i in nums3:
    if nums3.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)

for i in nums4:
    if nums4.count(i) > 1:
        if i not in duplicates2:
            duplicates2.append(i)

duplicates.extend(duplicates2)
print(duplicates)