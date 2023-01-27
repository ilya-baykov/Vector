def math_operation_with_vector(other, symbol, self, cls, cls_all_vectors):
    if isinstance(other, int):
        return cls(*list(map(lambda x: eval(f"{x} {symbol} {other}"), cls_all_vectors[self.index_position])))
    elif isinstance(other, cls):
        if len(self.values) == len(other.values):
            return cls(*list(map(lambda x: eval(f"{x[0]} {symbol} {x[1]}"), list(zip(self.values, other.values)))))
        else:
            print("Сложение" if symbol == "+" else "Умножение" + "Векторов разных длин невозможно")

    else:
        print("Вектор нельзя " + ("сложить с " if symbol == "+" else "умножить с ") + str(other))
