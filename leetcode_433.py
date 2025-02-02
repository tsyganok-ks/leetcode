from collections import deque

def minMutation(startGene, endGene, bank):
    """
    Calculate the minimum number of mutations needed to mutate from startGene to endGene
    :param startGene: start position
    :param endGene: end position
    :param bank: possible positions
    :return: count of mutations or -1
    """
    #if end is not valid, we can't reach it
    if endGene not in bank:
        return -1

    bank = set(bank)

    #All possible values can be used
    genes = ['A', 'T', 'G', 'C']

    #Create queue with level of mutations
    queue = deque()
    queue.append((startGene, 0))

    while queue:
        currGene, lvl = queue.popleft()
        if currGene == endGene:
            return lvl

        for i, gen in enumerate(currGene):
            for new_gen in genes:
                if gen != new_gen:
                    newGene = currGene[:i] + new_gen + currGene[i+1:]
                    if newGene in bank:
                        queue.append((newGene, lvl + 1))
                        bank.remove(newGene)

    return -1


def main():
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    print(minMutation(startGene, endGene, bank))


if __name__ == '__main__':
    main()