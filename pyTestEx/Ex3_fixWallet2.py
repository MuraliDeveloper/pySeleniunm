import pytest
from _pytest.fixtures import SubRequest


class Wallet:
    balance = None
    initial_amount = None


# ==================== fixtures
@pytest.fixture
def wallet(request: SubRequest):
    param = getattr(request, 'param', None)
    if param:
        prepared_wallet = Wallet(initial_amount=param[0])
    else:
        prepared_wallet = Wallet()
    yield prepared_wallet
    prepared_wallet.close()


# ==================== tests
def test_default_initial_amount(wallet):
    assert wallet.balance == 0


@pytest.mark.parametrize('wallet', [(100,)], indirect=True)
def test_setting_initial_amount(wallet):
    assert wallet.balance == 100


@pytest.mark.parametrize('wallet', [(10,)], indirect=True)
def test_wallet_add_cash(wallet):
    wallet.add_cash(amount=90)
    assert wallet.balance == 100


@pytest.mark.parametrize('wallet', [(20,)], indirect=True)
def test_wallet_spend_cash(wallet):
    wallet.spend_cash(amount=10)
    assert wallet.balance == 10
"""
Neat! isn’t it. Test functions are pretty subtle, and doing only what they intend to do. 
Setting up and tearing down instantiating and closing Wallet are being taken care by fixture wallet . Not only it is helping to write reusable piece of code, it also adds the essence of data separation. If you look carefully, wallet amount is a piece of test data supplied from outside of the test logic, and not hard-coded inside test function.
@pytest.mark.parametrize(‘wallet’, [(10,)], indirect=True)

"""
