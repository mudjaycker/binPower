bin_inputed = int(input("=> "))
bin_inputed = bin(bin_inputed)[2:]
binlist = list(bin_inputed)
binlist.reverse()


gen_bin = (index for index, value in enumerate(binlist) if value == "1")

for binval in gen_bin:
    print(f"2.power({binval}) = {2**binval}")
