MAX_RETRIES: int = 3
DEFAULT_TIMEOUT_SECONDS: int = 30
HUMAN_APPROVAL_REQUIRED_ACTIONS: tuple[str, ...] = (
    "restock",
    "run_discount",
    "pause_campaign",
    "create_support_ticket",
    "execute_action",
)
