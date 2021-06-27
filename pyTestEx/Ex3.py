import pytest

@pytest.mark.parametrize(
  "id,name",
  [(100,"user1"), (200,"user2"), (300,"user3"), (400,"user4"), (500,"user5")]
  )

def test_Ids(id,name):
    print(id,name)

