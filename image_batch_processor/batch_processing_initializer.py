import argparse

from image_batch_processor.data_collection.image_file_finder import ImageFileFinder

def main():
    parser = argparse.ArgumentParser(
            description="Image batch processor for upscaling and preview picture creation."
            )
    parser.add_argument(
            '-i',
            '--input',
            help="Specify an input directory to look for pictures. Nested structures are allowed",
            type=str,
            )
    parser.add_argument(
            '-m',
            '--multiplier',
            help="Specify the upscale multiplier."
                 "If set to None the default multiplicator of 4 will be set",
            choices=[3, 4],
            type=int,
            default=3
            )
    parser.add_argument(
            '-w',
            '--watermark',
            help="Specify to set a watermark on the input pictures."
                 "Default is set to True",
            default=True,
            )
    parser.add_argument(
            '-p',
            '--preview',
            help="Specify if a preview picture composition should be created."
                 "Default is set to True",
            default=True
            )
    args = parser.parse_args()

    print("### PROCESSING STARTED ###\n")
    print(f"### PARAMETERS: UPSCALE={args.multiplier}, WATERMARK={args.watermark}, PREVIEW={args.preview} ###\n")
    
    image_batches = ImageFileFinder.find(args.input)

    print("\n### PROCESSING SUCCESFULLY FINISHED! ###")

if __name__ == "__main__":
    main()
