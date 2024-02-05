from Modulo4 import pares

def main():
    T = int(input(" "))
    found_pairs2 = []
    for y in range(1, T + 1):

        n, k = map(int, input(" ").split())
        T_n = list(map(int, input(" ").split()))

        found_pairs = pares(T_n, k)

        if found_pairs:
            found_pairs2.append(len(found_pairs))
        else:
            print(" ")
    for z in range(0, T, 1):
        print(f"Case #{z+1}: {found_pairs2[z]}")

if __name__ == "__main__":
    main()
