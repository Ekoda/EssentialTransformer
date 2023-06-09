import numpy as np
from src.utils.generic_utils import load_text_data
from src.transformer.transformer import EssentialTransformer


data = load_text_data(path="data/test.txt")
model = EssentialTransformer(data, model_dimension=64, n_attention_heads=2, decoder_blocks=2)

forward_pass = model.forward("the quick fox jumped", "over")

print(forward_pass)