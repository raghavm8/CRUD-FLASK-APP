import enum
    
class Status(enum.Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    ASSIGNED = "Assigned"
    BLOCKED = "Blocked"