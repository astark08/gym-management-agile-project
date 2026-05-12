"""
member.py

Defines the Member class used in the Gym Management App.
Follows PEP 8 naming conventions and includes Google-style docstrings.
"""

class Member:
    """Represents a gym member with basic profile information.

    Attributes:
        member_id (int): Unique identifier for the member.
        first_name (str): Member's first name.
        last_name (str): Member's last name.
        membership_active (bool): Whether the member's membership is active.
    """

    def __init__(self, member_id: int, first_name: str, last_name: str, membership_active: bool = True):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.membership_active = membership_active

    def check_in(self) -> str:
        """Simulates a member check-in.

        Returns:
            str: A confirmation message indicating check-in status.
        """
        if not self.membership_active:
            return f"Member {self.member_id} cannot check in — membership inactive."

        return f"Member {self.member_id} checked in successfully."
