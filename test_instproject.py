import instproject as ip;

def test_price_method():
    expected = Menu("Mcdonalds", "Burger","Big Mac","No",563,3.99)
    assert ip.price_method() == expected