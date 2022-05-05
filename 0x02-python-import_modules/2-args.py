#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(f"{len(sys.argv) -1} arguments.")
    else:
        print(f"{len(sys.argv) -1} argument:")
        for i in range(1 ,len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
