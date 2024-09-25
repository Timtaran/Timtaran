from PIL import Image, ImageDraw, ImageFont, ImageFilter


class ImageCard:
    # todo - remove hardcoded values

    def __init__(self, main_text: str, line1: str, line2: str, card_number: int):
        self.main_text = main_text
        self.line1 = line1
        self.line2 = line2
        self.card_number = card_number
        self._image = None

    def generate(self) -> Image.Image:
        base = Image.new("RGBA", (1306, 152))

        mask = self._generate_mask()
        bg = self._generate_background()
        overlay = self._generate_overlay(bg.size)

        bg.alpha_composite(overlay)

        base.paste(bg, (1, 1), mask=mask)

        return base

    @staticmethod
    def _generate_mask() -> Image.Image:
        mask = Image.new('L', (1304, 150))
        draw = ImageDraw.Draw(mask)

        draw.rounded_rectangle((0, 0, 1304, 150), fill=255, radius=20)

        return mask

    def _generate_background(self) -> Image.Image:
        bg = Image.new("RGBA", (1304, 150), (0, 0, 0, 255))
        colors = Image.new("RGBA", (1304, 150))

        draw = ImageDraw.Draw(colors)

        match self.card_number:
            case 0:
                draw.ellipse((-200, -30, 650, 90), fill='#F15404')
                draw.ellipse((650, 50, 1500, 180), fill='#0BAF03')
            case 1:
                draw.ellipse((-200, 50, 650, 180), fill='#0BAF03')
                draw.ellipse((650, -30, 1500, 90), fill='#EC5206')

        colors = colors.filter(ImageFilter.GaussianBlur(radius=100))

        bg.alpha_composite(colors)

        return bg

    def _generate_overlay(self, size: tuple[int, int]) -> Image.Image:
        overlay = Image.new("RGBA", (1304, 150))
        draw = ImageDraw.Draw(overlay)

        main_font = ImageFont.truetype('files/Gothic60-Regular.otf', 99)
        bg_font = ImageFont.truetype('files/RubikScribble-Regular.ttf', 102)

        draw.text((size[0]/2, 5), self.line1, font=bg_font, fill=(255, 255, 255, 128), anchor="mm")
        draw.text((size[0]/2, 125), self.line2, font=bg_font, fill=(255, 255, 255, 128), anchor="mm")
        draw.text((size[0]/2, size[1]/2 + 4.5), self.main_text, font=main_font, fill=(255, 255, 255), anchor="mm")

        return overlay


ImageCard(
    main_text="TIMTARAN'S GITHUB",
    line1="ничего интересного тут",
    line2="nothing interesting here",
    card_number=0
).generate().save("../assets/readme1.png")

ImageCard(
    main_text="CLOWNS PRODUCTION",
    line1="ДЕЛАЕМ ЕБАНОЕ МЯСО",
    line2="VIPERR MINECRAFT 2024",
    card_number=1
).generate().save("../assets/readme2.png")
