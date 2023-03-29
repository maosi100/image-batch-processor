from image_batch_processor.argument_parser import argument_parser
from image_batch_processor.data_collection.image_file_finder import ImageFileFinder

def main():
    args = argument_parser()

    print("### PROCESSING STARTED ###\n")
    print(f"### PARAMETERS: UPSCALE={args.multiplier}, WATERMARK={args.watermark}, PREVIEW={args.preview} ###\n")
    
    image_batches = ImageFileFinder.find(args.input)

    print("\n### PROCESSING SUCCESFULLY FINISHED! ###")

if __name__ == "__main__":
    main()
