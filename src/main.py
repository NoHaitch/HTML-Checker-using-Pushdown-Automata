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

    f = ["Q", "", "Z"]
    res = ["Q", "Z"]
    delta = ["Q", "", "Z", "Q", "Z"]
    mistakes = []
    command = ""
    print(html)
    for i in range(len(html)):
        command += html[i]
        for j in range(len(PDA)):
            if delta[0] == PDA[j][0] and PDA[j][1] == "eps" and PDA[j][2] in delta[2]:
                delta[0] = PDA[j][3]
                delta[2] = delta[2].replace(PDA[j][2], PDA[j][4], 1)

                print(PDA[j][1], delta, mistakes)

            elif delta[0] == PDA[j][0] and command == PDA[j][1]:
                if PDA[j][2] in delta[2]:
                    delta[0] = PDA[j][3]
                    delta[2] = delta[2].replace(PDA[j][2], PDA[j][4], 1)
                else:
                    mistakes.append(command)
                print(command, delta, mistakes)
                command = ""
    print(delta)

    if delta[0] == "Q99" and delta[2] == "":
        print("Accepted")
    else:
        print("Syntax error")
