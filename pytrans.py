from py_trans import PyTranslator


frase = """
hello, how are u?
im fine. thanks"""

py_t = PyTranslator()

py_t = PyTranslator(provider="google")

print(py_t.translate(frase, "pt"))