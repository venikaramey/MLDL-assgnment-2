a =input("enter a word:")
try:
    val = int(a)
    print("Input is an integer Please enter a word.")
except:
    try:
        val = float(a)
        print("Input is an float Please enter a word.")
    except:
        print(a[::-1])