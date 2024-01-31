def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    with open("results.txt", "w") as file:
        for number in range(1, 251):
            if is_prime(number):
                file.write(str(number) + "\n")

if __name__ == "__main__":
    main()
