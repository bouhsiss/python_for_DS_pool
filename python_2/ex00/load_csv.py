import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        assert isinstance(path, str), "Path must be a string"
        dataset = pd.read_csv(path)
        print("Loading dataset of dimensions {0}".format(dataset.shape))
        return dataset
    except (FileNotFoundError, pd.errors.ParserError, AssertionError) as e:
        print("Error loading dataset: {0}".format(e))
        return None