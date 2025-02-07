def queryResults(limit, queries):
    """
    After each query, finds the number of distinct colors among the balls
    :param limit: number of balls + 1
    :param queries: [ball number, color number]
    :return: list of number distinct colors for each query
    """
    balls = {}
    answ = []
    color_balls = {}
    for ball, color in queries:
        if ball in balls and balls[ball] != color:
            if len(color_balls[balls[ball]]) == 1:
                color_balls.pop(balls[ball])
            else:
                color_balls[balls[ball]].remove(ball)

        balls[ball] = color

        if color not in color_balls:
            color_balls[color] = [ball]
        elif ball not in color_balls[color]:
            color_balls[color].append(ball)

        answ.append(len(color_balls))
    return answ


def main():
    limit = 4
    queries = [[0,1],[0,4],[0,4],[0,1],[1,2]]
    print(queryResults(limit, queries))


if __name__ == '__main__':
    main()