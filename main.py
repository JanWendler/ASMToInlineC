# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputFilePath = "D:/Praktikum/test.txt"  # sys.argv[0]
    outputFilePath = "D:/Praktikum/result.txt"  # sys.argv[1]
    tmp = []
    with open(inputFilePath, "r+") as temp_f:
        dataFile = temp_f.readlines()
    tmp.append("__asm volatile(\n")
    for line in dataFile:
        tmp.append("\"" + line.strip() + "\\n\\t\"\n")
    tmp.append(");")
    outputFile = open(outputFilePath, "w")
    outputFile.writelines(tmp)
    outputFile.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
