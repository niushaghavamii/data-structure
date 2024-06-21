class Polynomial:
    class Node:
        def __init__(self, coeff, power):
            self.coefficient = coeff
            self.power = power
            self.next = None

    def __init__(self):
        self.head = None

    def add_term(self, coeff, power):
        if self.head is None:
            self.head = self.Node(coeff, power)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = self.Node(coeff, power)

    def add(self, poly1, poly2):
        result = Polynomial()
        current1 = poly1.head
        current2 = poly2.head

        while current1 is not None and current2 is not None:
            if current1.power > current2.power:
                result.add_term(current1.coefficient, current1.power)
                current1 = current1.next
            elif current1.power < current2.power:
                result.add_term(current2.coefficient, current2.power)
                current2 = current2.next
            else:
                result.add_term(current1.coefficient + current2.coefficient, current1.power)
                current1 = current1.next
                current2 = current2.next

        while current1 is not None:
            result.add_term(current1.coefficient, current1.power)
            current1 = current1.next

        while current2 is not None:
            result.add_term(current2.coefficient, current2.power)
            current2 = current2.next

        return result

    def multiply(self, poly1, poly2):
        result = Polynomial()
        current1 = poly1.head
        while current1 is not None:
            current2 = poly2.head
            while current2 is not None:
                result.add_term(current1.coefficient * current2.coefficient, current1.power + current2.power)
                current2 = current2.next
            current1 = current1.next
        return result

    def display(self):
        current = self.head
        if current is None:
            print("Empty polynomial")
            return
        while current is not None:
            print(f"| {current.coefficient}x^{current.power} ", end="")
            current = current.next
        print("|")


# Example usage
poly1 = Polynomial()
poly1.add_term(2, 2)
poly1.add_term(4, 1)
poly1.add_term(6, 0)

poly2 = Polynomial()
poly2.add_term(1, 2)
poly2.add_term(3, 1)
poly2.add_term(5, 0)

print("Polynomial 1:")
poly1.display()
print("Polynomial 2:")
poly2.display()

print("Addition result:")
result_addition = Polynomial().add(poly1, poly2)
result_addition.display()

print("Multiplication result:")
result_multiplication = Polynomial().multiply(poly1, poly2)
result_multiplication.display()
