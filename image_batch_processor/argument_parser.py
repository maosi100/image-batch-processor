import argparse

def argument_parser():
    parser = argparse.ArgumentParser(
            description="Image batch processor for upscaling and preview picture creation."
            )
    parser.add_argument(
            '-i',
            '--input',
            help="Specify an input directory to look for pictures. Nested structures are allowed.",
            type=str,
            )
    parser.add_argument(
            '-m',
            '--multiplier',
            help="Specify the upscale multiplier. "
                 "If set to None the default multiplicator of 3 will be set.",
            choices=[3, 4],
            type=int,
            default=3
            )
    parser.add_argument(
            '-w',
            '--watermark',
            help="Specify to set a watermark on the input pictures. "
                 "(default = True)",
            default=True,
            )
    parser.add_argument(
            '-p',
            '--preview',
            help="Specify if a preview picture composition should be created. "
                 "(default = True)",
            default=True
            )
    parser.add_argument(
            '-l',
            '--label',
            help="Specify if a label should created and added to the preview composition. "
                 "(default = False)"
            )
    return parser.parse_args()
