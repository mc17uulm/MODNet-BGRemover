import argparse
from bg_remove import BGRemove

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ckpt_image', type=str, default='/usr/src/app/MODNet-BGRemover/pretrained/modnet_photographic_portrait_matting.ckpt',
                        required=False, help='Checkpoint path')
    parser.add_argument('--image', type=str, required=True, help='Inference image filename')
    parser.add_argument('--output', type=str, required=True, help='Output path')                    

    args = parser.parse_args()
    try:
        bg_remover = BGRemove(args.ckpt_image)
        bg_remover.image(args.image, output=args.output)
        

    except Exception as Err:
        print("Erro happend {}".format(Err))
