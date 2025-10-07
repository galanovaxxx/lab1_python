import src.final
import pytest


def test_1():
    with pytest.raises(ValueError):
        final_function('100//9.7')


def test_2():
    with pytest.raises(ValueError):
        final_function('100%7.9')


def test_3():
    with pytest.raises(ZeroDivisionError):
        final_function('8/(9*0)')


def test_4():
    with pytest.raises(ValueError):
        final_function('k*8+1')


def test_5():
    with pytest.raises(ValueError):
        final_function('(9+1*(8-1)')


def test_6():
    with pytest.raises(ValueError):
        final_function('*8+1')

def test_7():
    with pytest.raises(ValueError):
        final_function('1*-7*4')


def test_8():
    with pytest.raises(ValueError):
        final_function(')9*8(')


def test_9():
    with pytest.raises(ValueError):
        final_function('2 4.6 + 9')


def test_10():
    assert final_function('2**(-2)') == 0.25


def test_11():
    assert final_function('45**77*8+777*456') == 158654921195537705268149422920019030111324807283696814379484215409548387540182527570033210739808282596641220152378082275390979312


def test_12():
    assert final_function('3.345*8.1234*0.67693684698439') == 18.394251278442567


def test_13():
    assert final_function('3**4**5') == 373391848741020043532959754184866588225409776783734007750636931722079040617265251229993688938803977220468765065431475158108727054592160858581351336982809187314191748594262580938807019951956404285571818041046681288797402925517668012340617298396574731619152386723046235125934896058590588284654793540505936202376547807442730582144527058988756251452817793413352141920744623027518729185432862375737063985485319476416926263819972887006907013899256524297198527698749274196276811060702333710356481


def test_14():
    assert final_function('(((8*7-1)+9**2)*2)') == 272


def test_15():
    assert final_function('57%9+79%5') == 7


def test_16():
    assert final_function('(-(+(-(+(-(+(-2)))))))') == 2


def test_17():
    assert final_function('2**0.001**0.001**0.001**0.001**0.001**0.001**0.001**0.001**0.001**0.001**0.001') == 1.0007289372419133


def test_18():
    assert final_function('(9.677+8.323)//2') == 9


def test_19():
    assert final_function('(-5 + 3) * (- 2) - 8 / (-4) + (- 10)*(+ 6-7)') == 16


def test_20():
    assert final_function('-2 + 8 * (7 - 2) / 4 + 8 // 3 * (7 + (6 % 4) - (9 - 9) * 5)') == 26
