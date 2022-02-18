from operator import itemgetter

def eraseOverlapIntervals(intervals) -> int:
        # sort by the finishing time in ascending order.
        sorted_intervals = sorted(intervals, key=itemgetter(1))
        start, end = sorted_intervals[0]
        count = 0
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] < end and start < sorted_intervals[i][1]:
                count += 1
            else:
                start, end = sorted_intervals[i]
        return count


if __name__ == "__main__":
    print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))