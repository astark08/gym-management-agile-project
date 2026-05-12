"""
main.py

Entry point for the Gym Management App.
Demonstrates basic functionality using clean code and documentation.
"""

from member import Member
from trainer import Trainer
from schedule import ClassSchedule


def main():
    """Runs a simple demonstration of the Gym Management App."""

    # Create sample objects
    member = Member(member_id=1, first_name="Alec", last_name="Smith")
    trainer = Trainer(trainer_id=101, name="Jordan Lee", specialty="Strength Training")
    class_schedule = ClassSchedule(class_name="Morning Strength", trainer=trainer, capacity=2)

    # Demonstrate check-in
    print(member.check_in())

    # Demonstrate class assignment
    print(trainer.assign_class("Morning Strength"))

    # Demonstrate enrollment
    print(class_schedule.enroll_member(member.member_id))
    print(class_schedule.enroll_member(2))
    print(class_schedule.enroll_member(3))  # Should show "class full"


if __name__ == "__main__":
    main()
