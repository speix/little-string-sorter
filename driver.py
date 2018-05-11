def reorder(log):

    items, sub_items = [], []

    for line in log:
        sentence = line.split()
        items.append(line)
        sub_items.append(" " . join(sentence[1:]))

    print merger(items, sub_items)


def merger(line, subs):
    temp, sorter = [], []
    unique_entries = set(subs)

    indices = {value: [i for i, v in enumerate(subs) if v == value]
               for value in unique_entries}

    for ind in sorted(indices):
        for item in indices[ind]:
            temp.append(line[item])

        temp.sort()
        sorter.extend(temp)
        del temp[:]

    position = 0
    for i, r in enumerate(sorter):
        it = r.split()
        if not it[1].isdigit():
            position = i
            break

    return sorter[position:] + sorter[:position]


def main():

    log = [
        'q1 300 410 222',
        'b5 xi me nu',
        'br8 eat nim did',
        'w1 has uni gry',
        't2 34 54 398',
        'f3 34 54 410',
        'r1 box ape bit',
        'b4 xi me nu',
        'a3 34 54 410',
        'a2 34 54 398'
    ]

    reorder(log)


if __name__ == "__main__":
    main()
