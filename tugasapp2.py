class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack kosong")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack kosong")
        return self._data.pop()

def reverse_file(filename):
    a = ArrayStack()
    original = open(filename)
    for line in original:
        a.push(line.rstrip("\n"))
    original.close()

    output = open(filename, "w")
    while not a.is_empty():
        output.write(a.pop() + "\n")
    output.close()

    openfile = open(filename, "r")
    k = openfile.readlines()
    for i in k:
        print(i.rstrip())

def is_matched(expr):
    kiri = "({["
    kanan = ")}]"
    a = ArrayStack()
    for i in expr:
        if i in kiri:
            a.push(i)
        elif i in kanan:
            if a.is_empty():
                return False
            if kanan.index(i) != kiri.index(a.pop()):
                return False
    return a.is_empty()

operasi = True

while operasi :
    print("\nMenu : \n 1. Reverse File \n 2. Matching Delimiters \n 3. Keluar")
    pilih = int(input("Masukkan Pilihan Menu : "))
    if pilih == 1 :
        namaFile = input("Masukkan Nama File : ")
        print(namaFile + ".txt")
        reverse_file(namaFile + ".txt")
    elif pilih == 2 :
        expression = input("Masukkan Expression : ")
        match = is_matched(expression)
        if match :
            print("\nSemua pembatas cocok dengan baik")
        else :
            print("\nTerdapat pembatas yang tidak cocok")
    else :
        break
