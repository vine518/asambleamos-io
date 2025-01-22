# models/__init__.py

# Import all models here
from .unit import Unit
from .person import Person
from .role import Role
from .user import User
from .identity_provider import IdentityProvider
from .user_identity import UserIdentity
from .owner import Owner
from .representation import Representation
from .condominium import Condominium
from .assembly import Assembly
from .agenda import Agenda
from .agenda_item import AgendaItem
from .voting import Voting
from .voting_question import VotingQuestion
from .vote import Vote
from .attendance import Attendance
from .attorney import Attorney
from .common_area import CommonArea
from .booking import Booking
from .notification import Notification
from .access_log import AccessLog
from .expense import Expense

# Logical grouping ensures circular dependency resolution and maintainability.
