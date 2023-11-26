import os
import argparse
import sys


# Fungsi untuk parse HTML ke array
def parseHTMLfile(filename):
    contentofFile = []
    file = open(filename, "r")
    for line in file:
        startSpace = True
        syntax = ""
        for i in range(len(line)):
            if startSpace:
                if line[i] == " ":
                    continue
                else:
                    startSpace = False
            syntax += line[i]
        syntax.removeprefix(" ")
        syntax.removesuffix(" ")
        syntax.removesuffix("\n")
        if syntax != '' and len(syntax) != 0 and syntax != '\n' and syntax != '\t' and syntax != '\r' and syntax != '\0':
            doubleSpace = True
            while doubleSpace:
                if "  " in syntax:
                    syntax = syntax.replace("  ", " ")
                else:
                    doubleSpace = False
            removeSpaceCloseTag = True
            while removeSpaceCloseTag:
                if " >" in syntax:
                    syntax = syntax.replace(" >", ">")
                elif "> " in syntax:
                    syntax = syntax.replace("> ", ">")
                elif " <" in syntax:
                    syntax = syntax.replace(" <", "<")
                else:
                    removeSpaceCloseTag = False
            contentofFile.append(syntax.strip())
    return contentofFile


def deleteComment(html):
    inTag = False
    commentInsideTag = False
    comment = False
    string = ""
    for i in range(len(html)):
        if not inTag:
            if html[i] == '<' and html[i + 1] == '!':
                comment = True
            if html[i] == '>' and html[i - 1] == '-':
                comment = False
                continue
        if comment:
            continue
        if html[i] == '<' and html[i + 1] != '!':
            inTag = True
        if not comment:
            string += html[i]
        if html[i] == '>' and html[i - 1] != '-':
            inTag = False

    return string


def removeStrings(html):
    result = []
    inside_quotes = False
    for char in html:
        if char == '"':
            inside_quotes = not inside_quotes
        elif not inside_quotes:
            result.append(char)
    return ''.join(result)


if __name__ == "__main__":
    # Inisialisasi untuk mengambil argumen PDA.txt dan juga file HTML
    parser = argparse.ArgumentParser(description="Masukkan PDA dan HTML File!")
    parser.add_argument("PDAFile", nargs="?", default=None, help="Masukkan nama file PDA")
    parser.add_argument("HTMLFile", nargs="?", default=None, help="Masukkan nama file HTML")
    args = parser.parse_args()

    # Cek apakah file PDA dan HTML ada, dan jika ada di-parse dan di-save di HTML array
    if not os.path.exists(args.PDAFile) or args.PDAFile is None:
        print("File PDA tidak ditemukan!")
        sys.exit()
    else:
        if not os.path.exists(args.HTMLFile) or args.HTMLFile is None:
            print("File HTML tidak ditemukan!")
            sys.exit()
        else:
            htmlArray = parseHTMLfile(args.HTMLFile)

    # Inisialisasi PDA dan string input dari HTML
    PDAFile = open(args.PDAFile, "r")
    PDA = []
    for line in PDAFile:
        if "#" in line or line == '\n' or line == ' ' or len(line) == 0:
            continue
        else:
            PDA.append(line.split())

    for i in range(len(PDA)):
        if PDA[i][4] == "eps":
            PDA[i][4] = ""
        elif PDA[i][4] == "_":
            PDA[i][4] = " "
    delta = [" " for i in range(5)]
    string = ""
    for i in range(len(htmlArray)):
        string += htmlArray[i]


    # Proses menghilangkan kalimat di luar tag
    command = ""
    html = ""
    insideTag = False
    comment = False
    for i in range(len(string)):
        if string[i] == '<':
            insideTag = True
        if insideTag:
            command += string[i]
        if string[i] == '>':
            insideTag = False
            html += command
            command = ''
    html = deleteComment(html)
    html = removeStrings(html)
    f = ["Q", "", "Z"]
    res = ["Q", "Z"]
    delta = ["Q", "", "Z", "Q", "Z"]
    mistakes = []
    command = ""
    print(html)
    found = False
    done = False
    i = 0
    checker = 0
    isEps = False
    while not done:
        command = ""
        while not found:
            command += html[i]
            for j in range(len(PDA)):
                if delta[0] == PDA[j][0] and command == PDA[j][1]:
                    if PDA[j][2] in delta[2]:
                        found = True
                        delta[0] = PDA[j][3]
                        delta[2] = delta[2].replace(PDA[j][2], PDA[j][4], 1)
                        command = ""
                        checker = i
                        break
            # if not found yet the html string is end
            if i + 1 >= len(html):
                break

        if not found:
            for j in range(len(PDA)):
                if delta[0] == PDA[j][0] and PDA[j][1] == "eps" and PDA[j][2] in delta[2]:
                    delta[0] = PDA[j][3]
                    delta[2] = delta[2].replace(PDA[j][2], PDA[j][4], 1)
                    isEps = True
                    break


    print("result:", delta)

    if delta[0] == "Q99" and delta[2] == "":
        print("Accepted")
    else:
        print("Syntax error")
