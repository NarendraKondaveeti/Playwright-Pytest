class TablesLocators:

    TABLES_LINK = (
        "a[href='/tables']"
    )

    TABLE1 = "#table1"

    TABLE2 = "#table2"

    TABLE1_ROWS = (
        "#table1 tbody tr"
    )

    TABLE2_ROWS = (
        "#table2 tbody tr"
    )

    LAST_NAME_HEADER_TABLE1 = (
        "#table1 th:nth-child(1)"
    )

    EDIT_LINK = (
        "#table1 tbody tr:first-child a[href='#edit']"
    )

    DELETE_LINK = (
        "#table1 tbody tr:first-child a[href='#delete']"
    )