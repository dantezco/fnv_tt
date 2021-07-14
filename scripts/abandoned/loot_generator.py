from latex_table import LatexTable

class LootGenerator:

    def __init__(self):
        pass

    def get_item_table(self):
        pass

    def get_items_tables(self):
        regex_food = "([\w ]+) & [\d\.]+ & [\d\.]+ & [\w, \d+\-\(\)]+ \\\\"
        regex_items = "([\w \-]+) & [\d\.]+ & [\d\.]+ & [\+\w\- \(\)\%,\\]+ & [\+\w\- \(\)\%,\\]+[ ]*\\\\"
        items_paths = [
            ("../rules/table_chems.tex", regex_items),
            ("../rules/table_drinks.tex", regex_items),
            ("../rules/table_food.tex", regex_food),
        ]
        table = []
        for path, regex in items_paths:
            items = LatexTable(name="Consumables",
                               regex=regex,
                               path=path)
            for item in items:
                table.append(item)



if __name__ == "__main__":
    lg = LootGenerator()
    lg.get_items_tables()
