def main():
    w = list(range(7))
    for i in range(len(w)):
        w[i] = i + 10
    for j in range(len(w)):
        print("ListElement[{0}]={1}".format(j,w[i]))

if __name__ == "__main__":
    main()