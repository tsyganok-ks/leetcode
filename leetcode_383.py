def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    Return True if ransomNote can be constructed from magazine's letters
    """
    dict_ransom = {x: ransomNote.count(x) for x in ransomNote}
    dict_magazine = {x: magazine.count(x) for x in magazine}
    for letter in dict_ransom:
        if letter not in dict_magazine:
            return False
        elif dict_magazine[letter] < dict_ransom[letter]:
            return False
    return True


def main():
    ransomNote = "aa"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine))


if __name__ == '__main__':
    main()