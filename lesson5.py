from support_function import math_operation_with_vector


class Vector:
    __all_Vectors = []

    def __init__(self, *args):
        self.values = sorted([arg for arg in args if isinstance(arg, int)])
        self.index_position = len(Vector.__all_Vectors)
        Vector.add_vectors(self.values)

    def __str__(self):
        result_string_info = [str(arg) for arg in self.values]
        return f"Вектор {self.index_position + 1} ({', '.join(result_string_info)})"

    @classmethod
    def add_vectors(cls, value):
        cls.__all_Vectors.append(value)

    @classmethod
    def get_all_vectors(cls):
        return cls.__all_Vectors

    def __add__(self, other):
        return math_operation_with_vector(other=other, symbol="+", self=self, cls=Vector,
                                          cls_all_vectors=Vector.__all_Vectors)

    def __mul__(self, other):
        return math_operation_with_vector(other=other, symbol="*", self=self, cls=Vector,
                                          cls_all_vectors=Vector.__all_Vectors)


if __name__ == "__main__":
    pass
