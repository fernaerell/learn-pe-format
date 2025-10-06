import binary, endian, coff

file_name = "main.obj"

# COFF File Header (Size 20 byte)
coff_file_header = binary.size(20)

# Machine (Offset 0, Size 2 byte)
binary.set(coff_file_header, 0, coff.IMAGE_FILE_MACHINE_AMD64, endian.LITTLE)

# NumberOfSections (Offset 2, Size 2 byte)
binary.set(coff_file_header, 2, binary.size(2), endian.LITTLE)

# TimeDateStamp (Offset 4, Size 4 byte)
binary.set(coff_file_header, 4, binary.size(4), endian.LITTLE)

# PointerToSymbolTable (Offset 8, Ukuran 4 byte)
binary.set(coff_file_header, 8, binary.size(4), endian.LITTLE)

# NumberOfSymbols (Offset 12, Ukuran 4 byte)
binary.set(coff_file_header, 12, binary.size(4), endian.LITTLE)

# SizeOfOptionalHeader (Offset 16, Ukuran 2 byte)
binary.set(coff_file_header, 16, binary.size(2), endian.LITTLE)

# Characteristics (Offset 18, Ukuran 2 byte)
binary.set(coff_file_header, 18, coff.IMAGE_FILE_NONE, endian.LITTLE)

# Write binary
binary.write(file_name, coff_file_header)