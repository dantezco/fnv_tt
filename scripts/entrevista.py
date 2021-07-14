class Class:
    pass

class Filter:
    pass

class FilterFunction(Filter, Class):
    def filter_evens(self, l):
        out = []
        for i in l:
            if i % 2 == 0:
                out.append(i)

        return out

class FilterLambda(Filter, Class):
    def filter_evens(self, l):
        return list(filter(lambda x: x % 2 == 0, l))

if __name__ == "__main__":
    input_list = range(1, 101)
    filter1 = FilterFunction()
    out1 = filter1.filter_evens(input_list)

    filter2 = FilterLambda()
    out2 = filter2.filter_evens(input_list)

    print(f"output for function: {out1}")
    print(f"output for lambda: {out2}")

