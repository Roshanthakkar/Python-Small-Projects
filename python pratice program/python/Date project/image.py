import pywhatkit as kt



print("Lets turn image to ASCII value art!")

source_path='jannat.jpg'

kt.image_to_ascii_art(source_path, 'demo_ascii_art.text')

source_path='jannat.jpg'
target_path='demo_ascii_art.text'

kt.image_to_ascii_art(source_path, target_path)