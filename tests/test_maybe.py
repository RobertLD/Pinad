from src.pinad import Maybe

def test_maybe_when_given_value_correctly_unwraps_value():
    # ints
    assert 3 == Maybe(3).unwrap()
    assert 4 == Maybe(4).unwrap()
    assert 5 == Maybe(5).unwrap()

    #strings
    assert "foo" == Maybe("foo").unwrap()
    assert "bar" == Maybe("bar").unwrap()
    assert "baz" == Maybe("baz").unwrap()

    # More complex object
    example_object = [1,2,3,4]
    assert example_object == Maybe(example_object).unwrap()

def test_maybe_when_given_none_unwraps_to_none():
    assert Maybe(None).unwrap() is None

def test_maybe_when_bind_results_in_none_unwraps_to_none():
    assert Maybe(1).bind(lambda _: None).unwrap() is None

def test_maybe_or_selects_first_non_none_value():
    assert (Maybe(None) | Maybe(None) | Maybe(1).bind(lambda _: None) | Maybe(1)).unwrap() == 1

def test_maybe_or_else_uses_value_as_default_when_value_is_none():
    assert Maybe(1).bind(lambda _: None).orElse(5).unwrap() == 5


def test_maybe_or_else_uses_base_value_when_its_not_none():
    assert Maybe(1).orElse(5).unwrap() == 1