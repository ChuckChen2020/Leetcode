def numRabbits(answers) -> int:
    freq = dict()
    for x in answers:
        if x in freq.keys():
            freq[x] += 1
        else:
            freq[x] = 1
    count = 0
    for key, value in freq.items():
        if value == 0:
            count += 1
        elif value <= (key + 1) and value > 0:
            count += (key + 1)
        elif value > (key + 1):
            rest = value
            while rest > key + 1:
                count += (key + 1)
                rest -= (key + 1)
            count += (key + 1)
    return count
    


if __name__ == "__main__":
    assert numRabbits([1,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7,9,11,13]) == 80
    assert numRabbits([1,0, 1,0, 0]) == 5
    assert numRabbits([1,3,5,7,9,11,13]) == 56
    assert numRabbits([1,1,2]) == 5
    assert numRabbits([10,10,10]) == 11
    assert numRabbits([]) == 0
