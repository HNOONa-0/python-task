import sys
import random
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QMessageBox, QSizePolicy
from PySide2.QtGui import QFont, QColor, QPalette
from PySide2.QtCore import Qt, QPoint
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from checkers import *
from my_utils import *

class MainWindow(QWidget):
    def __init__(self,func_content=INIT_FUNC,x1_content=INIT_X1,x2_content=INIT_X2):
        super().__init__()

        self.x1_content=x1_content
        self.x2_content=x2_content
        self.func_content=func_content
        # Set the font and background color for the labels
        label_font = QFont("Arial", 14, QFont.Bold)
        label_color = QColor("#333333")

        # Create the labels for the text areas
        function_label = QLabel("Function")
        function_label.setFont(label_font)
        function_label.setAlignment(Qt.AlignCenter)
        function_label.setStyleSheet(f"color: {label_color.name()};")

        x1_label = QLabel("x1")
        x1_label.setFont(label_font)
        x1_label.setAlignment(Qt.AlignCenter)
        x1_label.setStyleSheet(f"color: {label_color.name()};")

        x2_label = QLabel("x2")
        x2_label.setFont(label_font)
        x2_label.setAlignment(Qt.AlignCenter)
        x2_label.setStyleSheet(f"color: {label_color.name()};")

        # Create the text areas
        self.function_text = QLineEdit()
        self.function_text.setText(self.func_content)
        self.x1_text = QLineEdit()
        self.x1_text.setText(self.x1_content)
        self.x2_text = QLineEdit()
        self.x2_text.setText(self.x2_content)

        # Set the font and background color for the text areas
        text_font = QFont("Arial", 12)
        text_color = QColor("#666666")

        for text_area in [self.function_text, self.x1_text, self.x2_text]:
            text_area.setFont(text_font)
            text_area.setStyleSheet(f"color: {text_color.name()}; background-color: #F0F0F0; height: 30px;")

        # Create the matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Create a vertical layout for the text areas and labels

        text_layout = QVBoxLayout()
        text_layout.addWidget(function_label)
        text_layout.addWidget(self.function_text)
        text_layout.addWidget(x1_label)
        text_layout.addWidget(self.x1_text)
        text_layout.addWidget(x2_label)
        text_layout.addWidget(self.x2_text)
        text_layout.setContentsMargins(0, 0, 0, 0)
        text_layout.setSpacing(0)
        # Set the vertical stretch factor of the text line widgets to 0
        self.x1_text.setSizePolicy(self.x1_text.sizePolicy().horizontalPolicy(), QSizePolicy.Fixed)
        self.x2_text.setSizePolicy(self.x2_text.sizePolicy().horizontalPolicy(), QSizePolicy.Fixed)
        self.function_text.setSizePolicy(self.function_text.sizePolicy().horizontalPolicy(), QSizePolicy.Fixed)
        
        
        # Create a "Plot" button
        plot_button = QPushButton("Plot")
        plot_button.setFont(label_font)
        plot_button.setStyleSheet(f"color: {label_color.name()}; background-color: #F0F0F0;")
        plot_button.clicked.connect(self.plot_button_clicked)  # Connect the button to a function

        random_test_button = QPushButton("Random Test")
        random_test_button.setFont(label_font)
        random_test_button.setStyleSheet(f"color: {label_color.name()}; background-color: #F0F0F0;")
        random_test_button.clicked.connect(self.random_test_button_clicked)
        # Add the "Plot" button to the vertical layout
        text_layout.addWidget(plot_button)
        text_layout.addWidget(random_test_button)
        # Create a QWidget to contain the text_layout
        text_widget = QWidget()

        # Set the fixed width for the text_widget
        text_widget.setFixedWidth(200)

        # Set the text_layout for the text_widget
        text_widget.setLayout(text_layout)

        # Create a horizontal layout for the figure and text areas
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.canvas)
        main_layout.addWidget(text_widget)

        # Set the main layout for the window
        self.setLayout(main_layout)

        # # Set the main layout for the window
        # self.setLayout(main_layout)

        # Draw a random plot figure
        self.start_plot(self.func_content,self.x1_content,self.x2_content)
        # Set the size of the window and show it
        self.setGeometry(100, 100, 1000, 600)  # Increase the width of the window
        self.show()

    def draw_figure(self, x_vals, y_vals, s):
        # Clear the existing subplots
        self.figure.clear()

        # Calculate the number of subplots based on the length of x_vals
        num_subplots = len(x_vals)

        # Create the subplots and plot the data
        ax = self.figure.add_subplot(111)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Plotting function: "+math_expr(s) )
        for i in range(num_subplots):
            # Plot the data
            ax.plot(x_vals[i], y_vals[i],'blue')

        # Adjust the layout and refresh the canvas
        self.figure.tight_layout()
        self.canvas.draw()
    def start_plot(self,s,x1,x2):
        x_vals,y_vals=get_pts_new(float(x1),float(x2),s)
        self.draw_figure(x_vals,y_vals,s)
    def plot_button_clicked(self):
        # Display an error message box when the button is clicked
        x1,x2,s=str(self.x1_text.text() ),str(self.x2_text.text() ),str(self.function_text.text() )
        r=is_valid_GUI(x1,x2,s)
        if r!=0:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Critical)  # Set the label to "Error"
            message_box.setText(r)
            # Get the center point of the main window's frame geometry in global coordinates
            center_point = self.mapToGlobal(self.frameGeometry().center())

            # Calculate the position of the message box relative to the center of the main window
            message_box_position = center_point - QPoint(message_box.rect().width() / 2,
                                                            message_box.rect().height() / 2)
            # Set the position of the message box
            message_box.move(message_box_position)
            message_box.exec_()
        else:
            self.start_plot(py_expr(s),x1,x2)
    def set_text(self,f,x1,x2):
        if x1>x2:
            x1,x2=x2,x1
        # set the text areas correctly
        # maybe put this in its own function
        self.function_text.setText(math_expr(f) )
        self.x1_text.setText(str(x1) )
        self.x2_text.setText(str(x2) )
    def random_test_button_clicked(self):
        f=get_rand_function(valid_functions,valid_functions)
        x1,x2=get_rand_2x()
        self.set_text(f,x1,x2)
        self.start_plot(py_expr(f),x1,x2)

if __name__ == '__main__':
    # Create the PySide2 application
    app = QApplication(sys.argv)

    # Create the main window
    main_window =MainWindow()

    # Run the application
    sys.exit(app.exec_())