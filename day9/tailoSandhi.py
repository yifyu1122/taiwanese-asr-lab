from taibun import Converter

c = Converter(system='Tailo', sandhi='auto')

result = c.get("癩哥蛾仔")
print("實際口語發音：", result)
