import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner

rotate_board = False
# rotate_board = True

# GPIO to key mapping
_KEY_CFG_A = [
    board.GP6, board.GP13, board.GP18, 
    board.GP7, board.GP14, board.GP17,
    board.GP8, board.GP15, board.GP16, 
]

_KEY_CFG_B = [
    board.GP18, board.GP17, board.GP16, 
    board.GP13, board.GP14, board.GP15,
    board.GP6, board.GP7, board.GP8, 
]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            pins = _KEY_CFG_A if not rotate_board else _KEY_CFG_B
        )

    # flake8: noqa
    # fmt: off
    coord_mapping = [
     0,  1,  2, 
     3,  4,  5,
     6,  7,  8
    ]

keyboard = KMKKeyboard()


from kmk.modules.encoder import EncoderHandler
from kmk.keys import KC
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())
from kmk.modules.mouse_keys import MouseKeys; keyboard.modules.append(MouseKeys())
from kmk.modules.layers import Layers;


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)


keyboard.debug_enabled = True

# encoder_handler.divisor = 2 # for encoders with more precision
encoder_handler.pins = ((board.GP3, board.GP5, board.GP28, False),
                        (board.GP10, board.GP12, board.GP19, False))

encoder_handler.map = [ ((KC.VOLD, KC.VOLU, KC.MUTE), (KC.VOLD, KC.VOLU, KC.MUTE)),
                        ((KC.MW_DOWN, KC.MW_UP, KC.NO),   (KC.BRID, KC.BRIU, KC.NO)),]

# encoder layers example
# encoder_handler.map = [ ((encoder 1 layer 1), (encoder 2 layer 1), ), 
#                         ((encoder 1 layer 2), (encoder 2 layer 2), ),
#                       ]

keyboard.keymap = [
    [# Base Layer
        KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK,
        KC.AUDIO_VOL_DOWN,   KC.AUDIO_MUTE,       KC.AUDIO_VOL_UP,
        KC.NO,               KC.NO,               KC.TG(1), # toggle layer one
    ],
    [# Mouse Layer
        KC.MB_RMB,    KC.MS_UP,     KC.MB_LMB,
        KC.MS_LEFT,   KC.MS_DOWN,   KC.MS_RIGHT,
        KC.MB_MMB,    KC.MB_BTN4,   KC.TRNS,
    ]
]



if __name__ == '__main__':
    print("Starting Poco_pad")
    keyboard.go()

