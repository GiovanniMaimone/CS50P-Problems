from um import count

def main():
    test_len()
    test_strings()
    test_spaces_case()

def test_len():
    assert count("") == 0
    assert count("um") == 1
    assert count("um,um") == 2
    assert count("um,um,um") == 3
    assert count("um,um,um,um") == 4

def test_strings():
    assert count("yummy,um") == 1
    assert count("yummy,um,yummy") == 1
    assert count("yummy,um,yummy,um") == 2
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_spaces_case():
    assert count(" um ") == 1
    assert count("um  um") == 2
    assert count("UM") == 1
    assert count("UM,UM") == 2

if __name__ == "__main__":
    main()
