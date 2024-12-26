import os
from app import services


def test_services_inference(whisper_tiny_en, sample_audio):
    result = services.inference(whisper_tiny_en, sample_audio)

    assert result
    assert result["text"]
    assert result["language"] == "en"
    assert len(result["segments"]) > 0


def test_services_write_results(sample_result, tmp_path):
    services.write_results(sample_result, "my_audio", str(tmp_path))
    files = os.listdir(str(tmp_path))

    assert files
    assert len(files) == 5

    with open(f"{str(tmp_path)}/my_audio.txt", "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("\n", " ").strip()
    assert text == sample_result["text"].strip()


def test_services_get_yt_audio(sample_yt_link, tmp_path):
    services.get_yt_audio(sample_yt_link, str(tmp_path))

    files = os.listdir(str(tmp_path))

    assert files
    assert len(files) == 1
