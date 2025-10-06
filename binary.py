from endian import LITTLE, BIG

def size(value: int) -> bytearray:
    return bytearray(b"\x00" * value)

def write(file_name: str, value: bytes):
    with open(file_name, mode="wb") as file:
        file.write(value)

def set(bytes: bytearray, offset: int, value: bytes, endian: int):
    if endian == LITTLE:
        bytes[offset:offset+len(value)] = value[::-1]
    elif endian == BIG:
        bytes[offset:offset+len(value)] = value
    else:
        raise IndexError("Endian is not valid value.")

def read(file_name: str):
    with open(file_name, mode="rb") as file:
        return file.read()

def append(file_name: str, value: bytes):
    with open(file_name, mode="ab") as file:
        file.write(value)