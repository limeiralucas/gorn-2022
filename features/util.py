from behave.model import Table


def dict_to_cell(headings: list[str], dict_obj: dict) -> dict:
    return {f'{heading}': str(dict_obj[heading]) for heading in headings}


def assert_table_equals_list(table: Table, values: list[dict]):
    headings = table.headings
    values_to_compare = [
        frozenset(dict_to_cell(headings, value).items()) for value in values
    ]

    table_values = [frozenset(row.items()) for row in table]

    print(values_to_compare)
    print(table_values)

    assert values_to_compare == table_values
