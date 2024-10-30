import time

import gradio as gr

from uv_ruff.util import sleep


def slowly_reverse(word, progress=gr.Progress()):
    progress(0, desc="Starting")
    time.sleep(1)
    progress(0.05)
    new_string = ""
    for letter in progress.tqdm(word, desc="Reversing"):
        sleep(0.25)
        new_string = letter + new_string
    return new_string


demo = gr.Interface(slowly_reverse, gr.Text(), gr.Text())


def _main():
    demo.launch()


if __name__ == "__main__":
    _main()
