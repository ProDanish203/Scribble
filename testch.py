from data import Data
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run_test(text):
    lexer = Lexer(text)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    tree = parser.parse()
    base = Data()
    interpreter = Interpreter(tree, base)
    interpreter.interpret()
    return base

# Corrected and Renumbered Test Cases
print("Test 1: make a = 5")
print(run_test("make a = 5").read("a").value)  # Expected output: 5

print("Test 2: make b = 10")
print(run_test("make b = 10").read("b").value)  # Expected output: 10

print("Test 3: make c = 10 + 5")
print(run_test("make c = 10 + 5").read("c").value)  # Expected output: 15

print("Test 4: make d = 10 - 5")
print(run_test("make d = 10 - 5").read("d").value)  # Expected output: 5

print("Test 5: make e = 10 * 5")
print(run_test("make e = 10 * 5").read("e").value)  # Expected output: 50

print("Test 6: make f = 10 / 5")
print(run_test("make f = 10 / 5").read("f").value)  # Expected output: 2.0

print("Test 7: make g = 1 < 2")
print(run_test("make g = 1 < 2").read("g").value)  # Expected output: 1

print("Test 8: make h = 1 and 0")
print(run_test("make h = 1 and 0").read("h").value)  # Expected output: 0

print("Test 9: make i = 1 or 0")
print(run_test("make i = 1 or 0").read("i").value)  # Expected output: 1

print("Test 10: make j = not 1")
print(run_test("make j = not 1").read("j").value)  # Expected output: 0

print("Test 11: if 2 > 1 do make k = 10")
print(run_test("if 2 > 1 do make k = 10").read("k").value)  # Expected output: 10

print("Test 12: while a < 5 do make a = a + 1")
base = run_test("make a = 0 while a < 5 do make a = a + 1")
print(base.read("a").value)  # Expected output: 5

print("Test 13: make m = 1 greater than 2")
print(run_test("make m = 1 greater than 2").read("m").value)  # Expected output: 0

print("Test 14: make n = 1 less than 2")
print(run_test("make n = 1 less than 2").read("n").value)  # Expected output: 1

print("Test 15: make q = 1 equal to 1")
print(run_test("make q = 1 equal to 1").read("q").value)  # Expected output: 1

print("Test 16: make r = 1 not equal to 2")
print(run_test("make r = 1 not equal to 2").read("r").value)  # Expected output: 1

print("Test 17: make s = 10 plus 5")
print(run_test("make s = 10 plus 5").read("s").value)  # Expected output: 15

print("Test 18: make t = 10 minus 5")
print(run_test("make t = 10 minus 5").read("t").value)  # Expected output: 5

print("Test 19: make u = 10 times 5")
print(run_test("make u = 10 times 5").read("u").value)  # Expected output: 50

print("Test 20: make v = 10 divided by 5")
print(run_test("make v = 10 divided by 5").read("v").value)  # Expected output: 2.0

print("Test 21: make w = (10 + 5) * 2")
print(run_test("make w = (10 + 5) * 2").read("w").value)  # Expected output: 30

print("Test 22: make x = 10 + (5 * 2)")
print(run_test("make x = 10 + (5 * 2)").read("x").value)  # Expected output: 20

print("Test 23: make z = 1 and 1")
print(run_test("make z = 1 and 1").read("z").value)  # Expected output: 1

print("Test 24: make aa = 0 or 0")
print(run_test("make aa = 0 or 0").read("aa").value)  # Expected output: 0

print("Test 25: make ab = not 0")
print(run_test("make ab = not 0").read("ab").value)  # Expected output: 1

print("Test 26: make ac = 5 * (2 + 3)")
print(run_test("make ac = 5 * (2 + 3)").read("ac").value)  # Expected output: 25
