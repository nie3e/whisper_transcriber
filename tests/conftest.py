import os

import pytest
import whisper

dir_path = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def sample_audio() -> str:
    return f"{dir_path}/resources/question_10.mp3"


@pytest.fixture(scope="session")
def whisper_tiny_en() -> whisper.Whisper:
    model = whisper.load_model(
        f"{dir_path}/resources/tiny.en.pt",
        device="cuda"
    )
    return model


@pytest.fixture
def sample_result() -> dict:
    result = {
        "text": " Is Fred a fan of Liverpool? Are supporters of Real Madrid "
                "devotees of PSG? In European football, it is sometimes "
                "difficult to keep track of the mutual admiration and "
                "dislike. The following argument seeks to clarify some such "
                "relations. First of all, no member of Juventus is an expert "
                "of Hatov SCF. Next, somebody is a follower of West Ham "
                "United FC and an expert of Hatov SCF. So, necessarily, "
                "not every follower of West Ham United FC is a member of "
                "Juventus. Is the argument, given the explicitly stated "
                "premises, deductively valid or invalid? Options. Valid. "
                "Invalid. Answer the question.",
        "segments": [
            {
                "id": 0, "start": 0.0, "end": 6.04,
                "text": " Is Fred a fan of Liverpool? Are supporters of Real "
                        "Madrid devotees of PSG? In European football,"
            },
            {
                "id": 1, "start": 6.74, "end": 10.92,
                "text": " it is sometimes difficult to keep track of the "
                        "mutual admiration and dislike."
            },
            {
                "id": 2, "start": 11.22, "end": 17.58,
                "text": " The following argument seeks to clarify some such "
                        "relations. First of all, no member of Juventus is"
            },
            {
                "id": 3, "start": 17.58, "end": 24.64,
                "text": " an expert of Hatov SCF. Next, somebody is a "
                        "follower of West Ham United FC and an expert"
            },
            {
                "id": 4, "start": 24.64, "end": 32.22,
                "text": " of Hatov SCF. So, necessarily, not every follower "
                        "of West Ham United FC is a member of Juventus."
            },
            {
                "id": 5, "start": 33.02, "end": 38.68,
                "text": " Is the argument, given the explicitly stated "
                        "premises, deductively valid or invalid?"
            },
            {
                "id": 6, "start": 39.3, "end": 43.26,
                "text": " Options. Valid. Invalid. Answer the question."
            }
        ],
        "language": "en"
    }
    return result


@pytest.fixture
def sample_yt_link() -> str:
    return "https://www.youtube.com/watch?v=QohH89Eu5iM"
