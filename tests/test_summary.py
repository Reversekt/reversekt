from demo_app.summary import build_summary


def test_summary_counts_nonblank_items() -> None:
    assert build_summary(["commits", "", "pull requests"]) == "Demo summary: 2 item(s)"