#15:40 - 15:56
from operator import itemgetter

def findMinArrowShots(points) -> int:
        sorted_pts = sorted(points, key=itemgetter(1))
        start, end = sorted_pts[0]
        count = 1
        for i in range(1,len(sorted_pts)):
            n_s, n_e = sorted_pts[i]
            if n_s <= end and start <= n_e:
                continue
            else:
                start, end = n_s, n_e
                count += 1
        return count
    

if __name__ == "__main__":
    print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))