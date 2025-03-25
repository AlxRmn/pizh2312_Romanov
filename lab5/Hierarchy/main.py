from writing_tool import WritingTool, Pencil, Pen, GelPen

def main():
    # Тестирование пишущих инструментов
    pencil = Pencil("Faber-Castell", "HB")
    pen = Pen("Parker", "Blue")
    gel_pen = GelPen("Pilot", "Black", 0.5)

    pencil.write("Эскиз чертежа")
    pen.write("Деловой документ")
    gel_pen.write("Подпись")


main()
