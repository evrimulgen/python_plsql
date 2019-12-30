import pytest
import datetime


@pytest.mark.parametrize(
    "func, expected",
    [
        ("ret_varchar", "42"),
        ("ret_number", 42.42),
        ("ret_binary_integer", 42),
        ("ret_clob", "42"),
        ("ret_rowid", "AAAACPAABAAAAShAAA"),
        ("ret_date", datetime.datetime(year=2019, month=12, day=20)),
        ("ret_raw", b"42"),
        ("ret_long_raw", b"42"),
        ("ret_char", "42"),
        ("ret_bool", True),
        ("ret_record", (42, 84, 126)),
        ("ret_record_of_records", (42, (42, 84, 126), (42, 84, 126))),
        ("ret_nested", [i * 2 for i in range(1, 11)]),
        ("ret_nested_of_records", [(42, 84, 126) for i in range(1, 11)]),
        ("ret_plsql_table", {i: i for i in range(1, 11)}),
        ("ret_plsql_table_of_records", {i: (42, 84, 126) for i in range(1, 11)}),
        pytest.param(
            "ret_nested_of_nested",
            [[i * 2 for i in range(1, 11)] for i in range(1, 11)],
            marks=pytest.mark.skip(reason="Memory access violation"),
        ),
        pytest.param(
            "ret_nested_of_plsql_table",
            [{i: i for i in range(1, 11)} for i in range(1, 11)],
            marks=pytest.mark.skip(reason="Memory access violation"),
        ),
        pytest.param(
            "ret_plsql_table_of_plsql_table",
            {i: {j: j for j in range(1, 11)} for i in range(1, 11)},
            marks=pytest.mark.skip(reason="Memory access violation"),
        ),
    ],
)
def test_return_values(plsql, func, expected):
    return_value = getattr(plsql.test_return, func)()

    assert return_value == expected
