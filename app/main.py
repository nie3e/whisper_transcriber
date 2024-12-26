import os
import gradio as gr
import whisper
from datetime import datetime

from services import run

dir_path = os.path.dirname(os.path.realpath(__file__))
output_dir = f"{dir_path}/../outputs/"

model = whisper.load_model(
    "medium.en",
    device="cuda",
    download_root=f"{output_dir}/../models"
)


def show_output() -> None:
    os.startfile(output_dir)


def get_transcription(url: str) -> str:
    url = url.replace("file:/", "", 1)

    d = datetime.today().strftime('%Y-%m-%d')
    current_output_dir = f"{output_dir}/{d}"
    os.makedirs(current_output_dir, exist_ok=True)

    return run(model, url, current_output_dir)


def main() -> int:
    with gr.Blocks() as demo:
        with gr.Group():
            with gr.Row():
                transcription = gr.TextArea(label="Transcription",
                                            interactive=False,
                                            lines=15)
            with gr.Row():
                folder_btn = gr.Button(value="\U0001f4c2")
        with gr.Row(equal_height=True):
            url_text = gr.Textbox(label="YouTube url or Path", scale=60)
        with gr.Row():
            run_btn = gr.Button(scale=20, value="Run", variant="primary")

        folder_btn.click(show_output)

        run_btn.click(
            get_transcription,
            inputs=url_text,
            outputs=transcription
        )
    demo.launch()
    return 0


if __name__ == "__main__":
    os.makedirs(output_dir, exist_ok=True)
    exit(main())
