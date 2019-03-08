import datetime
import os
from functools import partial

import click
import pyscreenshot
from pynput import keyboard


def on_press(key, root_path, special_key=keyboard.Key.f2, debug=False):
    if debug:
        print('{} pressed'.format(key))
    if key == special_key:
        img_path = os.path.join(
            root_path,
            '{}.png'.format(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
        img = pyscreenshot.grab()
        img.save(os.path.join(root_path, img_path))
        if debug:
            print('save to {}'.format(img_path))


def on_release(key):
    # stop listener
    if key == keyboard.Key.esc:
        return False


def parse_key(key):
    if hasattr(keyboard.Key, key):
        return getattr(keyboard.Key, key)
    else:
        raise RuntimeError('No corresponding key for {}'.format(key))


@click.command()
@click.argument('save-path', type=click.Path(exists=True))
@click.option('--special-key', type=str, default='f2', help='key to take screenshot')
@click.option('--debug', is_flag=True, help='Print debug messages')
def grab_screenshot(save_path, special_key, debug):
    print('Screenshots will be saved to {}'.format(save_path))
    print('Press ESE to exit!')
    with keyboard.Listener(
            on_press=partial(on_press,
                             root_path=os.path.abspath(save_path),
                             special_key=parse_key(special_key),
                             debug=debug),
            on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    grab_screenshot()
