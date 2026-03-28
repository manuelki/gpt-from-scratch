# GPT from Scratch

Building a character-level GPT following Andrej Karpathy's ["Let's build GPT: from scratch, in code, spelled out"](https://youtu.be/kCc8FmEb1nY).

## What this is

A step-by-step implementation of a Transformer-based language model, trained on the [Tiny Shakespeare](https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt) dataset. The goal is not just to reproduce the code, but to deeply understand every component of the GPT architecture.

## Architecture

```
Input Text
    ↓
Character Tokenization
    ↓
Token + Position Embeddings
    ↓
┌─────────────────────┐
│   Transformer Block  │ × N
│  ┌─────────────────┐ │
│  │ Multi-Head       │ │
│  │ Self-Attention   │ │
│  ├─────────────────┤ │
│  │ Feed-Forward     │ │
│  │ Network          │ │
│  ├─────────────────┤ │
│  │ Layer Norm +     │ │
│  │ Residual Conn.   │ │
│  └─────────────────┘ │
└─────────────────────┘
    ↓
Linear → Softmax
    ↓
Next Character Prediction
```

## Learning Journey

Each step is a separate commit, following the video's progression:

| Step | Concept | File |
|------|---------|------|
| 1 | Bigram Language Model | `notebooks/01_bigram.ipynb` |
| 2 | Self-Attention mechanism | `notebooks/02_self_attention.ipynb` |
| 3 | Multi-Head Attention | `notebooks/03_multihead.ipynb` |
| 4 | Feedforward + Residuals | `notebooks/04_transformer_block.ipynb` |
| 5 | Full GPT model | `src/gpt.py` |
| 6 | Training + Generation | `src/train.py` |

## Key Concepts Implemented

- **Bigram model** as baseline
- **Self-attention** — the core mechanism that lets tokens "look at" other tokens
- **Multi-head attention** — multiple attention heads in parallel for richer representations
- **Positional embeddings** — because attention has no notion of order
- **Residual connections** — enabling deep networks to train
- **Layer normalization** — stabilizing training
- **Dropout** — regularization

## Setup

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Download training data
python data/download_data.py

# Train the model
python src/train.py

# Generate text
python src/generate.py
```

## Results

<!-- TODO: Add training loss curve and sample outputs after training -->

## Background

This project is part of my learning path transitioning from Voice/NLP Tech Lead to AI Product Manager / AI Tech Lead. See my [learning plan](https://github.com/YOUR_USERNAME) for the full context.

Built following: [Karpathy's "Let's build GPT"](https://youtu.be/kCc8FmEb1nY)

## License

MIT
