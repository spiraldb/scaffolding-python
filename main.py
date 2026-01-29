from torch.utils.data import IterableDataset, Dataset

class MapDataset(Dataset):
    def __init__(self) -> None: ...

    def __getitem__(self, index): ...

    def __len__(self) -> int: ...


class MyIterableDataset(IterableDataset):
    def __init__(self) -> None: ...
    def __iter__(self): ...


def main():
    print("Hello World")


if __name__ == "__main__":
    main()
