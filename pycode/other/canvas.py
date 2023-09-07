from collections import OrderedDict

class Shape:
    def __init__(self, x: int, y: int, xw: int, yw: int, shapeId: str):
        self.x = x
        self.y = y
        self.xw = xw
        self.yw = yw
        self.xwView = 0
        self.ywView = 0
        self.id = shapeId

class Pixel:
    BASE = '0'

    def __init__(self):
        self.layers: OrderedDict[Shape, None] = OrderedDict()

    def getColor(self) -> str:
        if self.layers:
            return next(reversed(self.layers)).id
        return Pixel.BASE
    
    def popShapePixel(self, shape: Shape):
        self.layers.pop(shape, None)

    def pushShapePixel(self, shape: Shape):
        self.popShapePixel(shape)
        self.layers[shape] = None

# Shape's coordinate is the top-left corner, and it must be within the canvas
# Shape's width and height must not be negative, it will be adjusted if it exceeds the canvas
class Canvas:
    def __init__(self, xw: int, yw: int) -> None:
        self.xw = xw
        self.yw = yw
        self.canvasView: list[list[str]] = [[Pixel.BASE for _ in range(xw)] for _ in range(yw)]
        self.canvasInternal = [[Pixel() for _ in range(xw)] for _ in range(yw)]
        self.shapeMap: OrderedDict[str, Shape] = OrderedDict()
        
    def _checkBoundary(self, x: int, y: int, xw: int, yw: int) -> tuple[int, int]:
        if not (0 <= x < self.xw and 0 <= y < self.yw):
            raise ValueError('Out of boundary')
        xw = max(0, min(xw, self.xw - x))
        yw = max(0, min(yw, self.yw - y))
        return xw, yw
    
    def _fit(self, shape: Shape) -> None:
        shape.xwView, shape.ywView = self._checkBoundary(shape.x, shape.y, shape.xw, shape.yw)
    
    def _extract(self, shape: Shape) -> None:
        for i in range(shape.y, shape.y + shape.ywView):
            for j in range(shape.x, shape.x + shape.xwView):
                self.canvasInternal[i][j].popShapePixel(shape)
                self._renderPixel(i, j)

    def _draw(self, shape: Shape) -> None:
        x, y, xw, yw = shape.x, shape.y, shape.xwView, shape.ywView
        for i in range(y, y + yw):
            for j in range(x, x + xw):
                self.canvasInternal[i][j].pushShapePixel(shape)
                self._renderPixel(i, j)

    def _renderPixel(self, x: int, y: int) -> str:
        color = self.canvasInternal[x][y].getColor()
        self.canvasView[x][y] = color
        return color
    
    
    def erase(self, shapeId: str) -> None:
        shape = self.shapeMap[shapeId]
        self._extract(shape)
        self.shapeMap.pop(shape.id, None)

    def draw(self, shapeId: str, x: int, y: int, xw: int, yw: int) -> None:
        if shapeId in self.shapeMap:
            raise ValueError('Shape already exists')
        shape = Shape(x, y, xw, yw, shapeId)
        self._fit(shape)
        self.shapeMap[shapeId] = shape
        self._draw(shape)
        
    def move(self, shapeId: str, newX: int, newY: int) -> None:
        if shapeId not in self.shapeMap:
            raise ValueError('Shape does not exist')
        shape = self.shapeMap[shapeId]
        xwv, ywv = self._checkBoundary(newX, newY, shape.xw, shape.yw)
        self._extract(shape)
        shape.x, shape.y, shape.xwView, shape.ywView = newX, newY, xwv, ywv
        self._draw(shape)

    def __str__(self) -> str:
        canvasStrLines = []
        for line in self.canvasView:
            canvasStrLines.append(', '.join(line))
        return '\n'.join(canvasStrLines)

    def print(self) -> None:
        print(self)

if __name__ == '__main__':
    canvas = Canvas(3, 3)
    canvas.draw('a', 0, 0, 2, 2)
    canvas.draw('b', 1, 1, 2, 2)
    canvas.draw('c', 0, 0, 3, 1)
    canvas.draw('d', 2, 2, 0, 0)
    canvas.move('a', 0, 1)
    canvas.move('a', 0, 2)
    canvas.move('b', 2, 0)
    canvas.move('b', 1, 0)
    canvas.move('a', 0, 1)
    canvas.erase('a')
    canvas.print()
