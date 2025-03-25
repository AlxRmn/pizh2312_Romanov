from line_segment import LineSegment
from line_segment_collection import LineSegmentCollection

collection = LineSegmentCollection()

# Добавляем отрезки в коллекцию
collection.add(LineSegment(0, 0, 3, 4))
collection.add(LineSegment(1, 2, 5, 6))

print("Коллекция отрезков:", collection)

# Сохраняем в JSON
collection.save("segments.json")

# Удаляем первый элемент
collection.remove(0)
print("После удаления элемента:", collection)

# Загружаем обратно из JSON
collection.load("segments.json")
print("После загрузки:", collection)
