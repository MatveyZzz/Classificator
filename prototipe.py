import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QScrollArea, QLabel
)
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas
)
from matplotlib.figure import Figure


class Comments(QWidget):
    def __init__(self, comments):
        super().__init__()
        self.comments = comments
        self.initUI()

    def initUI(self):
        # Создаем область с возможностью прокрутки
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Создаем виджет-контейнер для комментариев
        container = QWidget()
        layout = QVBoxLayout(container)  # Макет для размещения комментариев
        layout.setSpacing(5)  # Устанавливаем минимальные отступы между комментариями

        # Добавляем комментарии как QLabel в макет
        for comment in self.comments:
            label = QLabel(comment)
            label.setWordWrap(True)  # Если текст длинный, перенос на следующую строку
            layout.addWidget(label)

        # Устанавливаем контейнер в область прокрутки
        scroll_area.setWidget(container)

        # Главный макет для виджета комментариев
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)


class CircleDiagram:
    def __init__(self, data, labels, colors):
        self.figure = Figure()  # Создаем фигуру для диаграммы
        self.canvas = FigureCanvas(self.figure)  # Создаем холст для отображения диаграммы
        self.data = data
        self.labels = labels
        self.colors = colors

    def show_pie_chart(self):
        # Очищаем старый график
        self.figure.clear()

        # Создаем круговую диаграмму
        ax = self.figure.add_subplot(111)
        ax.pie(
            self.data,
            labels=self.labels,
            autopct='%1.1f%%',
            startangle=90,
            colors=self.colors
        )
        ax.axis("equal")  # Установить равные оси для круговой формы

        # Отобразить диаграмму
        self.canvas.draw()


class TechComments(QWidget):
    def __init__(self, comments):
        super().__init__()
        self.comments = comments
        self.initUI()

    def initUI(self):
        # Создаем область с возможностью прокрутки
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Создаем виджет-контейнер для комментариев
        container = QWidget()
        layout = QVBoxLayout(container)  # Макет для размещения комментариев
        layout.setSpacing(3)  # Устанавливаем минимальные отступы между комментариями

        # Добавляем комментарии как QLabel в макет
        for comment in self.comments:
            label = QLabel(comment)
            label.setStyleSheet("color: red; font-weight: bold;")  # Красный текст для технических проблем
            label.setWordWrap(True)
            layout.addWidget(label)

        # Устанавливаем контейнер в область прокрутки
        scroll_area.setWidget(container)

        # Главный макет для виджета технических комментариев
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# class LineChart:
#     def __init__(self, x_data, y_data, title="Линейная диаграмма", x_label="X", y_label="Y"):
#         """
#         Класс для отображения линейной диаграммы.
#         :param x_data: Список значений по оси X.
#         :param y_data: Список значений по оси Y.
#         :param title: Заголовок графика.
#         :param x_label: Подпись оси X.
#         :param y_label: Подпись оси Y.
#         """
#         self.figure = Figure()  # Создаем фигуру для диаграммы
#         self.canvas = FigureCanvas(self.figure)  # Создаем холст для отображения диаграммы
#         self.x_data = x_data
#         self.y_data = y_data
#         self.title = title
#         self.x_label = x_label
#         self.y_label = y_label
#
#     def show_line_chart(self):
#         """
#         Построение линейного графика с заданными данными.
#         """
#         # Очищаем старый график
#         self.figure.clear()
#
#         # Создаем область для построения графика
#         ax = self.figure.add_subplot(111)
#         ax.plot(self.x_data, self.y_data, marker='o', linestyle='-', color='blue')
#
#         # Настройка заголовков и подписей
#         ax.set_title(self.title)
#         ax.set_xlabel(self.x_label)
#         ax.set_ylabel(self.y_label)
#         ax.grid(True)
#
#         # Обновление холста
#         self.canvas.draw()



class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Отображение окна
        self.setGeometry(300, 300, 1000, 500)
        self.setWindowTitle('Радар клиентского сервиса')

        # Создаем основной горизонтальный макет
        main_layout = QHBoxLayout(self)

        # Левый вертикальный макет для диаграммы и обычных комментариев
        left_layout = QVBoxLayout()

        # Создаем диаграмму
        diagram = CircleDiagram(
            data=[50, 40, 30],
            labels=["Жалобы", "Пожелания", "Благодарности"],
            colors=["red", "blue", "yellow"]
        )
        diagram.show_pie_chart()

        # Добавляем холст диаграммы в левый макет
        left_layout.addWidget(diagram.canvas)

        # Добавляем обычные комментарии в левый макет
        comments_list = ["Все хорошо", "Все замечательно", "Все очень круто"]
        comments_widget = Comments(comments_list)
        left_layout.addWidget(comments_widget)

        # Добавляем левый макет в основной
        main_layout.addLayout(left_layout)

        # Добавляем технические комментарии справа
        tech_comments_list = [
            "Ошибка подключения",
            "Долгое время ответа сервера",
            "Проблема с доступом",
            "Не удалось загрузить данные",
            "Ошибка аутентификации",
            "Сбой работы системы"
        ]
        tech_comments_widget = TechComments(tech_comments_list)
        main_layout.addWidget(tech_comments_widget)

        self.setLayout(main_layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dashboard()
    ex.show()
    sys.exit(app.exec())
