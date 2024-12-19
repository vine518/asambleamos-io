# models/__init__.py

# Ensure logical grouping to avoid circular dependencies
# 1. Core models
from .user import User
from .condominium import Condominium

# 2. Ownership and representation
from .owner import Owner
from .attendance import Attendance
from .representation import Representation

# 3. Assemblies and agendas
from .assembly import Assembly
from .agenda import Agenda

# 4. Voting
from .voting import Voting
from .voting_question import VotingQuestion
from .vote import Vote

# 5. Attorneys (if applicable)
from .attorney import Attorney

# Add other models as needed