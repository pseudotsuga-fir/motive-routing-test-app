from flask import Flask, jsonify
import json
import random
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def get_vehicles():
    return {"1": {
        "id": 1,
        "title": "2021 Jeep Wrangled",
        "price": 24500,
        "image":
        "https://storage.googleapis.com/wackk-images-development/NonkAxHcPpTAggr1NpczmdVx",
        "description": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Justo nec ultrices dui sapien eget. Facilisis volutpat est velit egestas. Neque convallis a cras semper auctor neque vitae. Eu augue ut lectus arcu bibendum at varius vel pharetra. Tortor dignissim convallis aenean et tortor. Feugiat in ante metus dictum. Pharetra massa massa ultricies mi quis hendrerit dolor magna eget. Arcu dictum varius duis at consectetur lorem donec massa. Id consectetur purus ut faucibus pulvinar elementum integer enim neque. Magna eget est lorem ipsum dolor sit amet consectetur. Massa sapien faucibus et molestie ac feugiat. Quis hendrerit dolor magna eget est lorem.

      Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Elit ullamcorper dignissim cras tincidunt lobortis. Facilisi morbi tempus iaculis urna. Vitae auctor eu augue ut lectus arcu bibendum at. Faucibus pulvinar elementum integer enim neque volutpat ac. Iaculis nunc sed augue lacus viverra vitae congue. Mattis aliquam faucibus purus in. Varius duis at consectetur lorem donec massa sapien faucibus. Nibh tellus molestie nunc non blandit massa enim nec dui. Facilisi nullam vehicula ipsum a arcu. Tincidunt ornare massa eget egestas purus. Pretium fusce id velit ut tortor. Sit amet nisl purus in.""",
        "vin": random.randint(1, 1000),
    },
        "2": {
        "id": 2,
        "title": "2023 Dodge Challenged",
        "price": 65000,
        "image":
        "https://storage.googleapis.com/wackk-images-development/ALG88Z8zTEwt2vYkWiLJTPkN",
        "description": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Justo nec ultrices dui sapien eget. Facilisis volutpat est velit egestas. Neque convallis a cras semper auctor neque vitae. Eu augue ut lectus arcu bibendum at varius vel pharetra. Tortor dignissim convallis aenean et tortor. Feugiat in ante metus dictum. Pharetra massa massa ultricies mi quis hendrerit dolor magna eget. Arcu dictum varius duis at consectetur lorem donec massa. Id consectetur purus ut faucibus pulvinar elementum integer enim neque. Magna eget est lorem ipsum dolor sit amet consectetur. Massa sapien faucibus et molestie ac feugiat. Quis hendrerit dolor magna eget est lorem.

      Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Elit ullamcorper dignissim cras tincidunt lobortis. Facilisi morbi tempus iaculis urna. Vitae auctor eu augue ut lectus arcu bibendum at. Faucibus pulvinar elementum integer enim neque volutpat ac. Iaculis nunc sed augue lacus viverra vitae congue. Mattis aliquam faucibus purus in. Varius duis at consectetur lorem donec massa sapien faucibus. Nibh tellus molestie nunc non blandit massa enim nec dui. Facilisi nullam vehicula ipsum a arcu. Tincidunt ornare massa eget egestas purus. Pretium fusce id velit ut tortor. Sit amet nisl purus in.""",
        "vin": random.randint(1, 1000),
    },
        "3": {
        "id": 3,
        "title": "2004 Ford Out-Of-Focus",
        "price": 3500,
        "image": "https://pbs.twimg.com/media/EdC32clXoAAvhh9.jpg",
        "description": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Justo nec ultrices dui sapien eget. Facilisis volutpat est velit egestas. Neque convallis a cras semper auctor neque vitae. Eu augue ut lectus arcu bibendum at varius vel pharetra. Tortor dignissim convallis aenean et tortor. Feugiat in ante metus dictum. Pharetra massa massa ultricies mi quis hendrerit dolor magna eget. Arcu dictum varius duis at consectetur lorem donec massa. Id consectetur purus ut faucibus pulvinar elementum integer enim neque. Magna eget est lorem ipsum dolor sit amet consectetur. Massa sapien faucibus et molestie ac feugiat. Quis hendrerit dolor magna eget est lorem.

      Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Elit ullamcorper dignissim cras tincidunt lobortis. Facilisi morbi tempus iaculis urna. Vitae auctor eu augue ut lectus arcu bibendum at. Faucibus pulvinar elementum integer enim neque volutpat ac. Iaculis nunc sed augue lacus viverra vitae congue. Mattis aliquam faucibus purus in. Varius duis at consectetur lorem donec massa sapien faucibus. Nibh tellus molestie nunc non blandit massa enim nec dui. Facilisi nullam vehicula ipsum a arcu. Tincidunt ornare massa eget egestas purus. Pretium fusce id velit ut tortor. Sit amet nisl purus in.""",
        "vin": random.randint(1, 1000),
    },
        "4": {
        "id": 4,
        "title": "2023 Nissan Pathfinder",
        "price": 18000,
        "image":
        "https://storage.googleapis.com/wackk-images-development/pFXDQzJRGYRNvnKwpoG14Phb",
        "description": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Justo nec ultrices dui sapien eget. Facilisis volutpat est velit egestas. Neque convallis a cras semper auctor neque vitae. Eu augue ut lectus arcu bibendum at varius vel pharetra. Tortor dignissim convallis aenean et tortor. Feugiat in ante metus dictum. Pharetra massa massa ultricies mi quis hendrerit dolor magna eget. Arcu dictum varius duis at consectetur lorem donec massa. Id consectetur purus ut faucibus pulvinar elementum integer enim neque. Magna eget est lorem ipsum dolor sit amet consectetur. Massa sapien faucibus et molestie ac feugiat. Quis hendrerit dolor magna eget est lorem.

      Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Elit ullamcorper dignissim cras tincidunt lobortis. Facilisi morbi tempus iaculis urna. Vitae auctor eu augue ut lectus arcu bibendum at. Faucibus pulvinar elementum integer enim neque volutpat ac. Iaculis nunc sed augue lacus viverra vitae congue. Mattis aliquam faucibus purus in. Varius duis at consectetur lorem donec massa sapien faucibus. Nibh tellus molestie nunc non blandit massa enim nec dui. Facilisi nullam vehicula ipsum a arcu. Tincidunt ornare massa eget egestas purus. Pretium fusce id velit ut tortor. Sit amet nisl purus in.""",
        "vin": random.randint(1, 1000),
    },
        "5": {
        "id": 5,
        "title": "2021 Toyota Camry",
        "price": 34000,
        "image":
        "https://storage.googleapis.com/wackk-images-development/5JDZYGKUBHUpgpA1PbhvUfMV",
        "description": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Justo nec ultrices dui sapien eget. Facilisis volutpat est velit egestas. Neque convallis a cras semper auctor neque vitae. Eu augue ut lectus arcu bibendum at varius vel pharetra. Tortor dignissim convallis aenean et tortor. Feugiat in ante metus dictum. Pharetra massa massa ultricies mi quis hendrerit dolor magna eget. Arcu dictum varius duis at consectetur lorem donec massa. Id consectetur purus ut faucibus pulvinar elementum integer enim neque. Magna eget est lorem ipsum dolor sit amet consectetur. Massa sapien faucibus et molestie ac feugiat. Quis hendrerit dolor magna eget est lorem.

      Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Elit ullamcorper dignissim cras tincidunt lobortis. Facilisi morbi tempus iaculis urna. Vitae auctor eu augue ut lectus arcu bibendum at. Faucibus pulvinar elementum integer enim neque volutpat ac. Iaculis nunc sed augue lacus viverra vitae congue. Mattis aliquam faucibus purus in. Varius duis at consectetur lorem donec massa sapien faucibus. Nibh tellus molestie nunc non blandit massa enim nec dui. Facilisi nullam vehicula ipsum a arcu. Tincidunt ornare massa eget egestas purus. Pretium fusce id velit ut tortor. Sit amet nisl purus in.""",
        "vin": random.randint(1, 1000),
    },
        "6": {
        "id": 6,
        "title": "2007 Toyota Camry",
        "price": 4999,
        "image":
        "https://storage.googleapis.com/wackk-images-development/CDw9uXUxRLZYPawZW3vbr3rM",
        "description": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Justo nec ultrices dui sapien eget. Facilisis volutpat est velit egestas. Neque convallis a cras semper auctor neque vitae. Eu augue ut lectus arcu bibendum at varius vel pharetra. Tortor dignissim convallis aenean et tortor. Feugiat in ante metus dictum. Pharetra massa massa ultricies mi quis hendrerit dolor magna eget. Arcu dictum varius duis at consectetur lorem donec massa. Id consectetur purus ut faucibus pulvinar elementum integer enim neque. Magna eget est lorem ipsum dolor sit amet consectetur. Massa sapien faucibus et molestie ac feugiat. Quis hendrerit dolor magna eget est lorem.

      Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Elit ullamcorper dignissim cras tincidunt lobortis. Facilisi morbi tempus iaculis urna. Vitae auctor eu augue ut lectus arcu bibendum at. Faucibus pulvinar elementum integer enim neque volutpat ac. Iaculis nunc sed augue lacus viverra vitae congue. Mattis aliquam faucibus purus in. Varius duis at consectetur lorem donec massa sapien faucibus. Nibh tellus molestie nunc non blandit massa enim nec dui. Facilisi nullam vehicula ipsum a arcu. Tincidunt ornare massa eget egestas purus. Pretium fusce id velit ut tortor. Sit amet nisl purus in.""",
        "vin": random.randint(1, 1000),
    }}


@app.route('/vehicles', methods=['GET'])
@cross_origin()
def vehicles():
    return jsonify(list(get_vehicles().values()))


@app.route('/vehicles/<id>', methods=['GET'])
@cross_origin()
def vehicle(id):
    return jsonify(get_vehicles()[id])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
