from PIL import Image


def concat_pic(paths: list, output_path: str):
    """
    e.g.
    paths: ['./test/01.png', './test/02.png'.....]
    dst_path: './result.png'
    """
    imgs = [Image.open(p) for p in paths]
    result_height = max([i.height for i in imgs])
    result_width = sum([i.width for i in imgs])
    result = Image.new("RGB", (result_width, result_height))

    pos_x = 0
    for i in imgs:
        result.paste(i, (pos_x, 0))
        pos_x += i.width

    result.save(output_path)
