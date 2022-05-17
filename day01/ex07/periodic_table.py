def main():
    out_file = open("periodic_table.html", "w")
    print_start(out_file)
    with open("periodic_table.txt", "r") as input_file:
        lines = input_file.readlines()
        i = 0
        index = 0
        while True:
            data = lines[index].split(',')
            pos = data[0].split(":")[1]
            if i == 0:
                out_file.write("<tr>\n")
            if int(pos) == i:
                out_file.write("<td style=\"border: 1px solid black; padding:10px\">\n")
                out_file.write(f"\t<h4>{data[0].split(' ')[0]}</h4>\n")
                out_file.write("\t<ul>\n")
                out_file.write(f"\t\t<li>No {data[1].split(':')[1]}</li>\n")
                out_file.write(f"\t\t<li>{data[2].split(':')[1].strip()}</li>\n")
                out_file.write(f"\t\t<li>{data[3].split(':')[1]}</li>\n")
                out_file.write(f"\t\t<li>{data[4].split(':')[1].strip()}{data[4].split(':')[0]}</li>\n")
                out_file.write("\t</ul>\n")
                out_file.write("</td>\n")
                index += 1
            else:
                out_file.write("<td style=\"border: 1px solid black; padding:10px\">\n")
                out_file.write("</td>\n")
            if i == 17:
                out_file.write("</tr>\n")
                i = -1
            i += 1
            if index == len(lines):
                break
    print_end(out_file)
    out_file.close()


def print_start(out_file):
    out_file.write("<!DOCTYPE html>\n\
<html lang=\"en\">\n\
<head>\n\
    <meta charset=\"UTF-8\">\n\
    <meta name=\"viewport\"\n\
        content=\"width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0\">\n\
    <meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\">\n\
<title>Title</title>\n\
</head>\n\
<body>\n\
<table>\n")


def print_end(out_file):
    out_file.write("</table>\n\
</body>\n\
</html>\n")


if __name__ == '__main__':
    main()
