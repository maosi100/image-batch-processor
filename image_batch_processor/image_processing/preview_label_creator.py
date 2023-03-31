from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_preview_label(batch_name: str, pack_size: int, output_dir: str) -> str:
    img = Image.open('./image_batch_processor/image_processing/utilities/label.png')
        
    I1 = ImageDraw.Draw(img)
     
    myFont = ImageFont.truetype('./image_batch_processor/image_processing/utilities/Meslo_Regular.ttf', 32)
     
    I1.text((200, 25), batch_name, font=myFont, fill =(255, 255, 255))
    output_path = f"{output_dir}/label.png"
    img.save(output_path)

    return output_path
