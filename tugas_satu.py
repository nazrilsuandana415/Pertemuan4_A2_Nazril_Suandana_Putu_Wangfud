#tugas 1 batu gunting kertas
# batu = "()"
# gunting = "8<"
# kertas = "[]"

pemain = input()
pemain = pemain.split()

#statment Batu
if pemain[0]=="()" and pemain[1] == "()":
    print("Dua Pemain Seri")
elif pemain[0]=="()" and pemain[1] == "8<":
    print("Pemain A Menang")
elif pemain[0]=="()" and pemain[1] == "[]":
    print("Pemain B Menang")

#statement Gunting    
elif pemain[0]=="8<" and pemain[1] == "()":
    print("Pemain B Menang")
elif pemain[0]=="8<" and pemain[1] == "8<":
    print("Dua Pemain Seri")
elif pemain[0]=="8<" and pemain[1] == "[]":
    print("Pemain A Menang")

#statement kertas
elif pemain[0]=="[]" and pemain[1] == "()":
    print("Pemain A Menang")
elif pemain[0]=="[]" and pemain[1] == "8<":
    print("Pemain B menang")
elif pemain[0]=="[]" and pemain[1] == "[]":
    print("Dua Pemain Seri")
else :
    print()
