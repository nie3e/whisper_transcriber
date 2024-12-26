import torch
from whisper import Whisper
from whisper.utils import get_writer
from pytubefix import YouTube, extract
import gradio as gr


def run(model: Whisper, filepath_or_url: str, output_dir: str) -> str:
    try:
        if any(check in filepath_or_url
               for check in ["youtube.com", "youtu.be"]):
            gr.Info(f"Downloading {filepath_or_url}")
            filename = get_yt_audio(filepath_or_url, output_dir)
        else:
            filename = filepath_or_url

        gr.Info("Getting transcription")
        result = inference(model, filename)

        gr.Info("Saving results")
        write_results(result, filename, output_dir)
    except Exception as e:
        gr.Info(str(e))
        raise
    finally:
        torch.cuda.empty_cache()

    return result["text"]


def inference(model: Whisper, audio_path: str) -> dict:
    result = model.transcribe(audio_path, word_timestamps=True)
    return result


def write_results(result: dict, audio_name: str, output_dir: str) -> None:
    writer = get_writer("all", output_dir)
    writer(result, audio_name)  # noqa


def get_yt_audio(url: str, output_dir: str) -> str:
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True)[0]
    filename = extract.video_id(url) + f".{stream.subtype}"
    res = stream.download(output_dir, filename=filename)

    return res
