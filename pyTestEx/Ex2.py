import pytest

@pytest.mark.parametrize(
  "id",
  [(100), (200), (300), (400), (500)]
  )

def test_Ids(id):
    print(id)

