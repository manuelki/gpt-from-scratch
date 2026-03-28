"""Download the Tiny Shakespeare dataset."""
import urllib.request
import os

URL = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
OUTPUT = os.path.join(os.path.dirname(__file__), "input.txt")


def download():
    if os.path.exists(OUTPUT):
        print(f"Dataset already exists at {OUTPUT}")
        return

    print(f"Downloading Tiny Shakespeare dataset...")
    urllib.request.urlretrieve(URL, OUTPUT)

    # Quick stats
    with open(OUTPUT, "r") as f:
        text = f.read()
    print(f"Downloaded: {len(text):,} characters, {len(set(text))} unique characters")


if __name__ == "__main__":
    download()
