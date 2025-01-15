import pandas as pd

def getDataframeSize(players):
    """
    Calc shape of DF
    :param players: pandas DF
    :return: list of numbers of rows and number of columns
    """
    return list(players.shape)


def main():
    players = pd.DataFrame(data = [
        [1, 'Richy', 17],
        [2, 'Anthony', 19]],
        columns=['player_id', 'name', 'age'])

    print(getDataframeSize(players))

if __name__ == '__main__':
    main()

