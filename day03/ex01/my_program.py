from local_lib.path import Path


def main():
    try:
        Path.mkdir_p(Path('dir'))
        with Path.open(Path('dir/file.txt'), 'w') as file:
            file.write('Hello world!')
        with Path.open(Path('dir/file.txt'), 'r') as file:
            print(file.readline())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
