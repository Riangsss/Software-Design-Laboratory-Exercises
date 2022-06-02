def MinMax(list):

    if list:
        max, *min = list

        if min:
            minimum, maximum = MinMax(min)

            return [max, minimum][minimum < max], [max, maximum][maximum > max]

        return max, max

print()
print(MinMax([7,4,9,20,11,14,75,2,5]))
print()
