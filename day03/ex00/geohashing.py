import sys
import antigravity


def main():
    if len(sys.argv) != 4:
        print("error: bad arguments!")
        sys.exit()
    try:
        antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
