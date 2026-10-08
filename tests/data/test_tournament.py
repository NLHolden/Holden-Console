import pytest
from pydantic import ValidationError

from data.enums import PokerSite
from data.tournament import Tournament


def test_tournament_accepts_valid_data() -> None:
    tournament = Tournament(name="Daily Special", buy_in=10, site=PokerSite("ggpoker"))

    assert tournament.name == "Daily Special"
    assert tournament.buy_in == 10
    assert tournament.site is PokerSite.GGPoker


@pytest.mark.parametrize("buy_in", [0, -1])
def test_tournament_rejects_nonpositive_buy_in(buy_in: float) -> None:
    with pytest.raises(ValidationError):
        Tournament(name="Daily Special", buy_in=buy_in, site=PokerSite.GGPoker)


def test_tournament_rejects_unknown_site() -> None:
    with pytest.raises(ValidationError):
        Tournament(name="Daily Special", buy_in=10, site=PokerSite("unknown"))
