import sys
import re


def main():
    if len(sys.argv) != 2:
        print("error: bad parameters")
        sys.exit()
    if not sys.argv[1].endswith(".template"):
        print("error: wrong extension")
        sys.exit()
    in_file = open("settings.py", "r")
    d = {}
    for line in in_file.readlines():
        d[line.split('=')[0].strip()] = line.split('=')[1].strip()
    in_file.close()
    in_file = open(sys.argv[1], "r")
    out_file = open(sys.argv[1].replace("template", "html"), "w")
    for line in in_file.readlines():
        res = re.search("\\{.+\\}", line)
        if res:
            match = res.group(0)
            line = line.replace(match, d[match.replace("{", "").replace("}", "")].replace('"', ""))
        out_file.write(line)
    in_file.close()
    out_file.close()


if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        print("error: file not found")
    except IOError:
        print("error: io")
