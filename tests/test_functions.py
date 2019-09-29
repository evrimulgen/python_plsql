def test_simple_function(plsql):
    assert plsql.simple_function(p_int=5) == 5 + 5
    assert plsql.simple_function(p_int=None) is None


def test_function_with_defaults(plsql):
    assert plsql.function_with_defaults() == 5
    assert plsql.function_with_defaults(p_int_a=0) == 4
    assert plsql.function_with_defaults(p_int_b=0) == 1
    assert plsql.function_with_defaults(p_int_a=0, p_int_b=0) == 0


def test_string_function(plsql):
    assert plsql.string_function(p_str='test') == 'test' * 2


def test_function_in_out(plsql):
    result, in_out = plsql.function_in_out(p_int=21, p_float=1337.42, p_str='input')

    assert result == 42
    assert in_out['p_str'] == 'input: 42'
    assert in_out['p_float'] == 10.5
