from demo_app.messages import greeting


def test_greeting_uses_name() -> None:
    assert greeting("Ada") == "Hello, Ada!"


def test_greeting_uses_default_for_blank_name() -> None:
    assert greeting("  ") == "Hello, there!"