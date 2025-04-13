from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont

class ImageEditor:
    def __init__(self, image_path):
        """初始化图像编辑器"""
        self.image = Image.open(image_path)
    
    def save(self, output_path, format=None):
        """保存图像到指定路径，可以指定保存格式"""
        self.image.save(output_path, format=format)
    
    def show(self):
        """显示图像"""
        self.image.show()
    
    def resize(self, width, height):
        """调整图像大小"""
        self.image = self.image.resize((width, height))
    
    def rotate(self, angle):
        """旋转图像"""
        self.image = self.image.rotate(angle)
    
    def crop(self, left, top, right, bottom):
        """裁剪图像"""
        self.image = self.image.crop((left, top, right, bottom))
    
    def apply_filter(self, filter_type):
        """应用滤镜"""
        if filter_type == 'BLUR':
            self.image = self.image.filter(ImageFilter.BLUR)
        elif filter_type == 'CONTOUR':
            self.image = self.image.filter(ImageFilter.CONTOUR)
        elif filter_type == 'DETAIL':
            self.image = self.image.filter(ImageFilter.DETAIL)
    
    def enhance(self, factor):
        """增强图像"""
        enhancer = ImageEnhance.Contrast(self.image)
        self.image = enhancer.enhance(factor)
    
    def convert_format(self, output_path, format):
        """转换图像格式（JPEG, PNG, BMP等）"""
        self.image.save(output_path, format=format)
    
    def create_thumbnail(self, size=(128, 128)):
        """生成缩略图"""
        self.image.thumbnail(size)
    
    def add_text(self, text, position=(10, 10), font_size=30, color=(255, 255, 255)):
        """添加文字到图像"""
        draw = ImageDraw.Draw(self.image)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()
        draw.text(position, text, fill=color, font=font)
    
    def add_watermark(self, watermark_text, position=(10, 10), font_size=30, color=(255, 255, 255)):
        """添加水印文字到图像"""
        self.add_text(watermark_text, position, font_size, color)
    
    def merge_images(self, image_paths, layout='horizontal'):
        """图像合并（横向或纵向拼接）"""
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
