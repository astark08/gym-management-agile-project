"""
schedule.py

Provides scheduling functionality for gym classes.
"""

from typing import List
from trainer import Trainer


class ClassSchedule:
    """Manages class scheduling for the gym.

    Attributes:
        class_name (str): Name of the class.
        trainer (Trainer): Trainer assigned to the class.
        enrolled_members (List[int]): List of member IDs enrolled.
        capacity (int): Maximum number of members allowed.
    """

    def __init__(self, class_name: str, trainer: Trainer, capacity: int = 20):
        self.class_name = class_name
        self.trainer = trainer
        self.capacity = capacity
        self.enrolled_members: List[int] = []

    def enroll_member(self, member_id: int) -> str:
        """Enrolls a member into the class if capacity allows.

        Args:
            member_id (int): The ID of the member enrolling.

        Returns:
            str: Enrollment status message.
        """
        if len(self.enrolled_members) >= self.capacity:
            return f"Class '{self.class_name}' is full."

        self.enrolled_members.append(member_id)
        return f"Member {member_id} enrolled in '{self.class_name}'."
