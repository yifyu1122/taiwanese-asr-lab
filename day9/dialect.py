from taibun import Converter

c = Converter(
    system='Tailo',
    dialect='south'
)

result = c.get("癩哥蛾仔")
print(result)
