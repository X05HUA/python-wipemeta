from PIL import Image


def clean_image(input_img, out_dir):
    """
    Path to Img
    Output dir
    """
    image = Image.open(input_img)

    # next 3 lines strip exif
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)

    org_name = str(input_img).rsplit("/", 1)

    org_name = org_name[1].split(".")

    image_without_exif.save(f'{out_dir}/{org_name[0]}_clean.jpeg')
    print("Image was cleaned. :)")


#split_me = "/run/media/chaos/850 evo/Images/70x70/king.jpg".rsplit("/", 1)



#clean_image("/run/media/chaos/850 evo/Images/70x70/king.jpg", "/run/media/chaos/850 evo/Images/Testing")