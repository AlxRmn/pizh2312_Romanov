# main.py - тестирование класса
from line_segment import LineSegment

segment = LineSegment(0, 0, 3, 4)
print(segment)  # LineSegment((0, 0) - (3, 4))
print("Длина:", segment.length())  # 5.0
    
segment.save("segment.json")
loaded_segment = LineSegment.load("segment.json")
print("Загруженный:", loaded_segment)
    
new_segment = LineSegment.from_string("1,2,4,6")
print("Из строки:", new_segment)