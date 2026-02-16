"""Simple automation stub: a timer + optional notification hook.

This demonstrates the "automation shape" used in PrimeVector:
- Parse input (arguments/config)
- Execute a small workflow
- Leave clear placeholders for mobile integrations (Shortcuts/webhooks/notifications)
"""

from __future__ import annotations

import argparse
import time

from primevector.utils.logging import get_logger

logger = get_logger(__name__)


def run_timer(seconds: int) -> None:
    """Run a blocking countdown timer.

    Args:
        seconds: Duration in seconds.
    """
    if seconds <= 0:
        raise ValueError("seconds must be > 0")

    logger.info("Timer started: %s seconds", seconds)
    for remaining in range(seconds, 0, -1):
        logger.info("Remaining: %s", remaining)
        time.sleep(1)

    logger.info("Timer finished!")

    # Placeholder: send a push notification, play a sound, trigger a webhook, etc.
    # Example ideas:
    # - iOS Shortcut webhook to notify
    # - Pushover / ntfy / Telegram bot ping
    # - Local desktop notification


def build_arg_parser() -> argparse.ArgumentParser:
    """Create an argument parser for CLI usage."""
    parser = argparse.ArgumentParser(description="PrimeVector: simple timer automation.")
    parser.add_argument("--seconds", type=int, default=10, help="Timer length in seconds.")
    return parser


def main() -> None:
    """CLI entrypoint."""
    parser = build_arg_parser()
    args = parser.parse_args()
    run_timer(args.seconds)


if __name__ == "__main__":
    main()
