from image_batch_processor.argument_parser import argument_parser
from image_batch_processor.data_collection.image_file_finder import ImageFileFinder
from image_batch_processor.image_batch_processor import ImageBatchProcessor

def main():
    args = argument_parser()

    print("### PROCESSING STARTED ###\n")
    print(f"### PARAMETERS: UPSCALE={args.multiplier}, WATERMARK={args.watermark}, PREVIEW={args.preview}, LABEL={args.label} ###\n")
    
    image_batches = ImageFileFinder().find(args.input)
    print(f"### PROCESSING TOTAL OF {len(image_batches)} BATCHES ###\n")

    for i, batch in enumerate(image_batches, start=1):
        print(f"### PROCESSING BATCH {i}/{len(image_batches)} ###\n")

        processor = ImageBatchProcessor(batch, args.multiplier)
        # processor.upscale_images()
        if args.watermark == True:
            processor.watermark_images()
            if args.preview == True:
                processor.create_preview_image(args.label)


    print("\n### PROCESSING SUCCESFULLY FINISHED! ###")

if __name__ == "__main__":
    main()
