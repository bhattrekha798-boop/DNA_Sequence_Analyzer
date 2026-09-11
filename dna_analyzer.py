while True:
    dna = input("Enter your DNA sequence: ")
    dna = dna.upper()

    if not dna:
        print("Error: DNA sequence cannot be empty.\n")

    elif not all(base in "ATGC" for base in dna):
        print("Error: Invalid DNA sequence. Use only A, T, G and C.")
        print("Please enter a valid DNA sequence.\n")

    else:
        break

length = len(dna)

a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

gc_content = ((g_count + c_count) / length) * 100

print("\nDNA Sequence Analysis")
print("---------------------")
print("Sequence length:", length)
print("A count:", a_count)
print("T count:", t_count)
print("G count:", g_count)
print("C count:", c_count)
print("GC content:", round(gc_content, 2), "%")