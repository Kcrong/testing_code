"""
모듈 의존성을 제외하면 제일 좋은 방법인듯
폰트를 자동으로 포함시켜줌
"""

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
filename = 'test_png.png'

pdfmetrics.registerFont(TTFont('test', 'testfont.ttf'))

c = canvas.Canvas("sample2_result.pdf")
c.setFont('test', 13)
# x, y format
c.drawString(100, 750, "Lorem ipsum dolor sit amet, consectetuer adipiscing elit")
c.drawImage(filename, 150, 400)
c.save()
