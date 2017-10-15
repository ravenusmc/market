def main():
    counter = 0
    values = []
    while counter <= 3:
        num = int(input('Please give me a number: '))
        values.append(num)
        counter += 1
    print(values)

main()

