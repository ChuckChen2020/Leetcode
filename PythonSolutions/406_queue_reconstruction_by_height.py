# 17:47-21:16
def reconstructQueue(people):
        people = sorted(people, reverse=True)
        queue = ["x"]*len(people)
        while len(people) != 0:
            shortest = people.pop()
            height, count = shortest
            i = 0
            while count != 0 or queue[i] != "x":
                if queue[i] == "x" or queue[i][0] == height:
                    i += 1
                    count -= 1
                else:
                    i += 1
            queue[i] = shortest

        return queue

if __name__ == "__main__":
    print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
