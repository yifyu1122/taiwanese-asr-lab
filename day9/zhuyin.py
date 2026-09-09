from taibun import Converter

c = Converter(system='Zhuyin')

result = c.get("癩哥蛾仔")
print("臺語方音符號：", result)
