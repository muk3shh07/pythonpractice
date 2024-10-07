import qrcode
name = input("Enter the name::")
img = qrcode.make(name)
type(img)  # qrcode.image.pil.PilImage
img.save(f"{name}.png")