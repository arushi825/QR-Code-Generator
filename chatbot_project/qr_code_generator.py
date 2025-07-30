import openai
import qrcode 
from PIL import Image
openai.api_key = "sk-pro-jmMXmbATq6USX3HNAeuPgODvD4BJEWseMOx8grR_p63VLJuapb6jHA5ndGSRrASkWr-46E5zGywT3BlbkFJiAvIyiDgrClBhWBXytcsT99jgqBinztWD2zdkF1oIW9o6OKFZ0V9z18H-cxJ0h2zkgGI6QkEsA"
qr = qrcode.QRCode(version = 1,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size = 10,border = 4,)
qr.add_data("https://www.youtube.com/")

qr.make(fit = True)
img = qr.make_image(fill_color = "blue",back_color = "white")
img.save("qr_code.png")