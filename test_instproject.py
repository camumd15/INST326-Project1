import instproject as ip;

def test_price_method():
    first = ip.Menu("Mcdonalds", "Burger","Big Mac","No",563,3.99)
    second = ip.Menu("Hard Times", "Wings","12 Texas Wings","No",954,13.43)
    third = ip.Menu("Jersey Mikes", "Sandwich","Giant Club Supreme","No",2140,15.99)
    menus = [first, second, third]
    assert ip.price_method(menus, 3.00) == []
    assert ip.price_method(menus, 7.00) == [first]
    assert ip.price_method(menus, 15.00) == [first, second]
    assert ip.price_method(menus, 18.00) == [first, second, third]
def test_gluten():
    first = ip.Menu("Mcdonalds", "Burger","Big Mac","No",563,3.99)
    second = ip.Menu("Hard Times", "Wings","12 Texas Wings","No",954,13.43)
    third = ip.Menu("Jersey Mikes", "Sandwich","Giant Club Supreme","No",2140,15.99)
    fourth = ip.Menu("Chipotle","Mexican","Chicken Bowl","Yes",390,6.50)
    menus = [first, second, third, fourth]
    assert ip.gluten_method(menus, "Yes") == [fourth]
    assert ip.gluten_method(menus, "No") == [first, second, third]
def test_foodtype():
    first = ip.Menu("Mcdonalds", "Burger","Big Mac","No",563,3.99)
    second = ip.Menu("Hard Times", "Wings","12 Texas Wings","No",954,13.43)
    third = ip.Menu("Jersey Mikes", "Sandwich","Giant Club Supreme","No",2140,15.99)
    fourth = ip.Menu("Chipotle","Mexican","Chicken Bowl","Yes",390,6.50)
    menus = [first, second, third, fourth]
    assert ip.matchFood(menus, "Burger") == [first]
    assert ip.matchFood(menus, "Wings") == [second]
    assert ip.matchFood(menus, "Sandwich") == [third]
    assert ip.matchFood(menus, "hfondo") == []
    assert ip.matchFood(menus, "Mexican") == [fourth]