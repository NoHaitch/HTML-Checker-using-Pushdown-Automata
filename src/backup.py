import os
import argparse
import sys


# Fungsi untuk parse HTML ke array
def parseHTMLfile(filename):
    contentofFile = []
    file = open(filename, "r")
    isComment = False
    dash = False
    secondDash = False
    for line in file:
        startSpace = True
        openTag = False
        syntax = ""
        for i in range(len(line)):
            if startSpace:
                if line[i] == " ":
                    continue
                else:
                    startSpace = False

            if line[i] == '<' and line[i+1] != '!':
                openTag = True
            elif line[i] == '>':
                openTag = False
            if line[i] == '<' and line[i + 1] == '!' and not openTag:
                isComment = True
            if isComment:
                if line[i] == '-':
                    dash = True
                if dash and line[i] == '-':
                    secondDash = True
                    dash = False
                if secondDash and line[i] == '>':
                    isComment = False
                    secondDash = False
                continue
            else:
                if line[i] == '\n':
                    continue
                syntax += line[i]
        syntax.removeprefix(" ")
        syntax = syntax.replace("-->", "")
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
    delta = [" " for i in range(5)]
    string = ""
    for i in range(len(htmlArray)):
        string += htmlArray[i]

    # Proses menghilangkan comment di luar tag
    command = ""
    html = ""
    insideTag = False
    for i in string:
        if i == '<':
            insideTag = True
        if insideTag:
            command += i
        if i == '>':
            insideTag = False
            html += command
            command = ''

    f = ["Q", "", ["Z"]]
    res = ["Q", ["Z"]]
    delta = ["Q", "", ["Z"], "Q", ["Z"]]
    command = ""
    print(html)
    for i in range(len(html)):
        command = html[i]
        string = ""
        space = False
        closeTag = False
        for j in command:
            if j == ' ':
                space = True
            elif j == '>':
                closeTag = True
            else:
                string += j

            if space:
                for k in PDA:
                    if string in k[1]:
                        print(string, "found")
                        delta[0] = k[0]
                        delta[1] = string
                        delta[2] = k[2]
                        delta[3] = k[3]
                        delta[4] = k[4]
