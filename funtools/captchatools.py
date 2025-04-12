import random
from PIL import Image, ImageDraw, ImageFont

class Captcha:
    def __init__(self, n=4, width=600, height=200):
        self.num = n
        self.width = width
        self.height = height
        self.text = ""
        self.image = Image.new('RGB', (self.width, self.height), 'white')
        self.draw = ImageDraw.Draw(self.image)

        try:
            self.font = ImageFont.truetype('f.TTF', size=100)
        except IOError:
            self.font = ImageFont.load_default()

    def random_color(self):
        """Generate a random color, avoiding too similar colors"""
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def random_char(self):
        """Generate a random character (letter or digit)"""
        char_type = random.choice(['lower', 'upper', 'digit'])
        if char_type == 'lower':
            return chr(random.randint(97, 122))  # Lowercase letter
        elif char_type == 'upper':
            return chr(random.randint(65, 90))  # Uppercase letter
        else:
            return chr(random.randint(48, 57))  # Digit

    def generate(self):
        """Generate the captcha image"""
        start_x = (self.width - self.num * 70) // 2
        y = (self.height - 100) // 2
        
        for i in range(self.num):
            char = self.random_char()
            self.text += char
            self.draw.text(
                (start_x + i * 80, y),
                text=char,
                fill=self.random_color(),
                font=self.font
            )

        # Draw random lines
        for _ in range(30):
            x1, y1 = random.randint(0, self.width), random.randint(0, self.height)
            x2, y2 = random.randint(0, self.width), random.randint(0, self.height)
            self.draw.line([(x1, y1), (x2, y2)], fill=self.random_color(), width=3)

        # Draw random points
        for _ in range(100):
            x, y = random.randint(0, self.width), random.randint(0, self.height)
            self.draw.point((x, y), fill=self.random_color())

    def show(self):
        """Display the captcha image"""
        self.image.show()

    def save(self, path):
        """Save the captcha image to a file"""
        self.image.save(path)
