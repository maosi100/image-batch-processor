from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_preview_label(batch_name: str, batch_size: int, output_dir: str) -> str:
    img = Image.open('./image_batch_processor/image_processing/utilities/label.png')
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype('./image_batch_processor/image_processing/utilities/Meslo_Regular.ttf', 32)
    _, _, w, h = draw.textbbox((0,0), batch_name, font=title_font)
    draw.text(((1140 - w) / 2, (100 - h - 40) / 2), batch_name, font=title_font, fill='white')

    subtitle_font = ImageFont.truetype('./image_batch_processor/image_processing/utilities/Meslo_Regular.ttf', 20)
    subtitle_text = f"300 dpi - {batch_size} high Quality PNG Files - 12\"x12\""
    _, _, w, h = draw.textbbox((0,0), subtitle_text, font=subtitle_font)
    draw.text(((1140 - w) / 2, (100 - h + 50) / 2), subtitle_text, font=subtitle_font, fill='white')

    output_path = f"{output_dir}/label.png"
    img.save(output_path)

    return output_path
