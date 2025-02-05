from collections import deque


def openLock(deadends, target):
    """
    Count the minimum total number of turns required to open the lock
    :param deadends: impossible states
    :param target: target
    :return: number of turns or -1
    """
    #we can't reach it, if it blocks
    if target in deadends or '0000' in deadends:
        return -1

    deadends = set(deadends)

    queue = deque()
    queue.append(('0000', 0))

    checked = set(deadends)
    checked.add('0000')

    while queue:
        curr_state, count = queue.popleft()
        if curr_state == target:
            return count

        for i, num in enumerate(curr_state):
            #There is 1 click forward or backward
            val = '0' if num == '9' else str(int(num) + 1)
            changed = curr_state[:i] + val + curr_state[i+1:]
            if changed not in checked:
                queue.append((changed, count + 1))
                checked.add(changed)

            val = '9' if num == '0' else str(int(num) - 1)
            changed = curr_state[:i] + val + curr_state[i+1:]
            if changed not in checked:
                queue.append((changed, count + 1))
                checked.add(changed)
    return -1


def main():
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(openLock(deadends, target))


if __name__ == '__main__':
    main()