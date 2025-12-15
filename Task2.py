try:
    with open("output.txt", "xt") as fh:
        taxt1 = fh.write(input("Enter text to write into the file: "))
except FileExistsError:
    print("")
finally:
    print("Data is successfuly return in the file")
        
with open("output.txt", "at") as fh:
    fh.write('\n')
    taxt2 = fh.write(input("Enter additional text to append: "))
    print("Data successfully appended")

with open("output.txt", "rt") as fh:
    print("\nFile Content:")
    print(fh.read())

    