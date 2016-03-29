import kostka

reload(kostka)

def test_prob():
    assert kostka.def2prob(2) == [0.5, 0.5]
    assert kostka.def2prob(3) == [1 / 3.0] * 3
    
    
def test_1_6():
    moje_kostka = kostka.Kostka(6)
    assert moje_kostka.hodit() in (1, 2, 3, 4, 5, 6)
    
def test_vyber_simple():
    # .5 == 0.5
    inp = [.5, 0, .5]
    ret = kostka.vyber(inp)
    
    assert int(ret) == ret
    assert 0 <= ret < len(inp)
    
    
def test_vykresli():
    inp = [.5, 0, .5]
    zaznam = [0, 0, 0]
    for i in range(100):
        ret = kostka.vyber(inp)
        zaznam[ret] += 1
    print(zaznam)
    # assert 0

    
def test_vyber_adv():
    inp = [.5, 0, .5]
    for i in range(100):
        ret = kostka.vyber(inp)
        assert ret != 1
    
    # vvv to by nemelo fungovat vvv
    inp = [1, 2, 3]
    ret = kostka.vyber(inp)
    inp = [0, 0, 0.2]
    ret = kostka.vyber(inp)