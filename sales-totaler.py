infile = input("Enter sales file name: ")
outfile = input("Enter name for total sales file: ")

reader = open(infile,"r")
writer= open(outfile,"w")

for line in reader.readlines():
    aCol, bCol = line.split()
    aCol, bCol = float(aCol[1:]), float(bCol[1:])
    total = str(aCol+bCol)
    s = "$ {0:>7}".format(aCol)+" $ {0:>7}".format(bCol)+" $ {0:>7}\n".format(total)
    writer.write(s)

reader.close()
writer.close()

print("\nDone writing totals to",outfile)