from memory_profiler import profile 
import collections


@profile
def main():

    Point = collections.namedtuple('Point', ['x'])

    p = [Point(42) for i in range(100000)]

if __name__ == "__main__":
    main()
  
