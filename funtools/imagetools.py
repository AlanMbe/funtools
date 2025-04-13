from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont

class ImageEditor:
    def __init__(self, image_path):
        """Initialize the image editor with the image at the given path"""
        self.image = Image.open(image_path)
    
    def save(self, output_path, format=None):
        """Save the image to the specified path, optionally specifying the format"""
        self.image.save(output_path, format=format)
    
    def show(self):
        """Display the image"""
        self.image.show()
    
    def resize(self, width, height):
        """Resize the image to the specified width and height"""
        self.image = self.image.resize((width, height))
    
    def rotate(self, angle):
        """Rotate the image by the specified angle"""
        self.image = self.image.rotate(angle)
    
    def crop(self, left, top, right, bottom):
        """Crop the image using the specified coordinates"""
        self.image = self.image.crop((left, top, right, bottom))
    
    def apply_filter(self, filter_type):
        """Apply a filter to the image (e.g., blur, contour, or detail)"""
        if filter_type == 'BLUR':
            self.image = self.image.filter(ImageFilter.BLUR)
        elif filter_type == 'CONTOUR':
            self.image = self.image.filter(ImageFilter.CONTOUR)
        elif filter_type == 'DETAIL':
            self.image = self.image.filter(ImageFilter.DETAIL)
    
    def enhance(self, factor):
        """Enhance the contrast of the image by the given factor"""
        enhancer = ImageEnhance.Contrast(self.image)
        self.image = enhancer.enhance(factor)
    
    def convert_format(self, output_path, format):
        """Convert the image to a specified format (JPEG, PNG, BMP, etc.)"""
        self.image.save(output_path, format=format)
    
    def create_thumbnail(self, size=(128, 128)):
        """Create a thumbnail of the image with the specified size"""
        self.image.thumbnail(size)
    
    def add_text(self, text, position=(10, 10), font_size=30, color=(255, 255, 255)):
        """Add text to the image at the specified position with given font size and color"""
        draw = ImageDraw.Draw(self.image)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()
        draw.text(position, text, fill=color, font=font)
    
    def add_watermark(self, watermark_text, position=(10, 10), font_size=30, color=(255, 255, 255)):
        """Add a watermark to the image at the specified position"""
        self.add_text(watermark_text, position, font_size, color)
    
    def merge_images(self, image_paths, layout='horizontal'):
        """Merge multiple images either horizontally or vertically"""
        images = [Image.open(img_path) for img_path in image_paths]
        widths, heights = zip(*(i.size for i in images))
        
        if layout == 'horizontal':
            total_width = sum(widths)
            max_height = max(heights)
            new_image = Image.new('RGB', (total_width, max_height))
            x_offset = 0
            for img in images:
                new_image.paste(img, (x_offset, 0))
                x_offset += img.width
        elif layout == 'vertical':
            max_width = max(widths)
            total_height = sum(heights)
            new_image = Image.new('RGB', (max_width, total_height))
            y_offset = 0
            for img in images:
                new_image.paste(img, (0, y_offset))
                y_offset += img.height
        
        self.image = new_image
