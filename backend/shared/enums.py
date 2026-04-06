from enum import Enum


class AgentDomain(str, Enum):
    SALES = "sales"
    INVENTORY = "inventory"
    MARKETING = "marketing"
    CUSTOMER_SUPPORT = "customer_support"
