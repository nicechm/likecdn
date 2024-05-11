# from flask import Flask

from flask import Flask, request, send_file
from PIL import Image, ImageDraw

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, Cho CDN!'

@app.route('/about')
def about():
    return 'About'

@app.route('/getImage/png')
def get_image():
    # 요청에서 파라미터 추출
    width = int(request.args.get('width', 300))
    height = int(request.args.get('height', 200))
    text = request.args.get('text', 'default text')
    bg = request.args.get('bg', 'white')

    # 이미지 생성
    image = Image.new('RGB', (width, height), '#' + bg)
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(text)
    draw.text(((width - text_width) / 2, (height - text_height) / 2), text, fill='black')

    # 이미지를 임시 파일로 저장하고 전송
    image.save('temp_image.png')
    return send_file('temp_image.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
