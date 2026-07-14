from unittest.mock import MagicMock, patch

from omnitest.actions.fill import FillAction


@patch("omnitest.actions.fill.BaseAction.execute")
def test_fill(mock_execute, mock_browser, mock_locator):

    action = FillAction(mock_browser)

    action.locator = MagicMock(return_value=mock_locator)

    action("#username", "admin")

    mock_execute.assert_called_once_with(
        "fill",
        mock_locator.fill,
        "admin",
    )
