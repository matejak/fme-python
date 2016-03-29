import kostka

reload(kostka)

def test_prob():
    assert kostka.def2prob(2) == [0.5, 0.5]
    assert kostka.def2prob(3) == [1 / 3.0] * 3
    
    
def test_1_6():
    moje_kostka = kostka.Kostka(6)
    assert moje_kostka.hodit() in (1, 2, 3, 4, 5, 6)