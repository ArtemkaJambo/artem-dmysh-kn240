from app import Figure


class Figure:
    FIGURES = ["square", "rectangle", "triangle"]
    
    def __init__(self, type, length) -> None:
        assert length > 0, "Length must be greater than 0!"
        assert type in self.FIGURES, "Allowed figures: square, rectangle, triangle"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.type  # Error! It should be self.length, not self.type

# Testing the class

# Creating objects
square = Figure("square", 10)
rectangle = Figure("rectangle", 20)
triangle = Figure("triangle", 15)

print(f"Figure type: {square.get_figure_type}, Length: {square.get_figure_length}")
print(f"Figure type: {rectangle.get_figure_type}, Length: {rectangle.get_figure_length}")
print(f"Figure type: {triangle.get_figure_type}, Length: {triangle.get_figure_length}")

def test_app_triangle():
    """Test if we create triangle figure.
    """
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.type == fig, f"Фігура має бути {fig}"
