"""
모듈 의존성을 제외하면 제일 좋은 방법인듯
폰트를 자동으로 포함시켜줌
"""
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate

filename = 'test_png.png'

pdfmetrics.registerFont(TTFont('test', 'testfont.ttf'))

our_style = (ParagraphStyle(name='custom_style',
                            fontName='test',
                            fontSize=30,
                            leading=10.1
                            )
             )

doc = SimpleDocTemplate("image.pdf")
parts = [
    Paragraph("My name is Hyunwoo, kcrong", our_style),
    Image(filename)
]
doc.build(parts)