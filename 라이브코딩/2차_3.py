def parse_tuple(txt):
    answer = []
    for word in txt.split():
        answer.append((len(word), word))
    return sorted(answer)

def main():
    txt = input()
    result = parse_tuple(txt)
    print(result)


if __name__ == "__main__":
    main()