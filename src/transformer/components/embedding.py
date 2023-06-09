import numpy as np

from src.neural_net.grad_engine import ValueNode
from src.neural_net.network import NeuralComponent
from src.utils.type_utils import Matrix

def generate_embeddings(vocabulary_size: int, embedding_size: int) -> Matrix:
    """
    Generates a matrix of initial embeddings for a vocabulary of given size and embedding dimension.

    Args:
        vocabulary_size (int): The number of words in the vocabulary.
        embedding_size (int): The dimension of the embedding space.

    Returns:
        list: A matrix of shape (vocabulary_size, embedding_size) containing the initial embeddings.
    """
    return [[ValueNode(np.random.rand()) for _ in range(embedding_size)] for _ in range(vocabulary_size)]

def get_token_embeddings(embeddings: list[list[float]], vocabulary: dict[str, int], tokens: list[str]) -> list[list[float]]:
    """
    Gets the embeddings for a list of tokens from a matrix of embeddings.

    Args:
        embeddings (np.ndarray): A matrix of shape (vocabulary_size, embedding_size) containing the embeddings.
        vocabulary (dict[str, int]): A dictionary mapping tokens to their indices in the vocabulary.
        tokens (list[str]): The list of tokens to fetch the embeddings for.

    Returns:
        list[list[float]]: A matrix of shape (len(tokens), embedding_size) containing the embeddings for the tokens.
    """
    return [embeddings[vocabulary[token]] for token in tokens]

class Embedding(NeuralComponent):
    def __init__(self, vocabulary_size: int, embedding_size: int):
        self.vocabulary_size = vocabulary_size
        self.embedding_size = embedding_size
        self.embeddings = generate_embeddings(vocabulary_size, embedding_size)

    def parameters(self) -> list[ValueNode]:
        return [p for row in self.embeddings for p in row]

    def forward(self, tokens: list[str], vocabulary: dict[str, int]) -> Matrix:
        return [self.embeddings[vocabulary[token]] for token in tokens]
