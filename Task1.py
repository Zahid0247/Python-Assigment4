with open("sample.txt", "wt") as fh:
    fh.write("This is simple file\n")
    fh.write("it contains multipal lines")

try:
    with open("Sample.txt", "rt") as fh:
        line1 = fh.readline()
        print(f"line1: {line1}")
        line2 = fh.readline()
        print(f"line2: {line2}")
     

except FileNotFoundError:
    print(f"file Sample.txt was not found")