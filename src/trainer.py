"""
trainer.py

Defines the Trainer class for the Gym Management App.
"""

class Trainer:
    """Represents a gym trainer responsible for leading classes.

    Attributes:
        trainer_id (int): Unique identifier for the trainer.
        name (str): Trainer's full name.
        specialty (str): Area of expertise (e.g., strength, cardio).
    """

    def __init__(self, trainer_id: int, name: str, specialty: str):
        self.trainer_id = trainer_id
        self.name = name
        self.specialty = specialty

    def assign_class(self, class_name: str) -> str:
        """Assigns the trainer to a class.

        Args:
            class_name (str): Name of the class being assigned.

        Returns:
            str: Confirmation message.
        """
        return f"Trainer {self.name} assigned to class: {class_name}"
