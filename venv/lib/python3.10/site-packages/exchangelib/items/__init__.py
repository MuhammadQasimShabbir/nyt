from .base import (
    AFFECTED_TASK_OCCURRENCES_CHOICES,
    ALL_OCCURRENCES,
    ALL_PROPERTIES,
    ALWAYS_OVERWRITE,
    AUTO_RESOLVE,
    CONFLICT_RESOLUTION_CHOICES,
    DEFAULT,
    DELETE_TYPE_CHOICES,
    HARD_DELETE,
    ID_ONLY,
    MESSAGE_DISPOSITION_CHOICES,
    MOVE_TO_DELETED_ITEMS,
    NEVER_OVERWRITE,
    SAVE_ONLY,
    SEND_AND_SAVE_COPY,
    SEND_MEETING_CANCELLATIONS_CHOICES,
    SEND_MEETING_INVITATIONS_AND_CANCELLATIONS_CHOICES,
    SEND_MEETING_INVITATIONS_CHOICES,
    SEND_ONLY,
    SEND_ONLY_TO_ALL,
    SEND_ONLY_TO_CHANGED,
    SEND_TO_ALL_AND_SAVE_COPY,
    SEND_TO_CHANGED_AND_SAVE_COPY,
    SEND_TO_NONE,
    SHAPE_CHOICES,
    SOFT_DELETE,
    SPECIFIED_OCCURRENCE_ONLY,
    BulkCreateResult,
    RegisterMixIn,
)
from .calendar_item import (
    CONFERENCE_TYPES,
    AcceptItem,
    CalendarItem,
    CancelCalendarItem,
    DeclineItem,
    MeetingCancellation,
    MeetingMessage,
    MeetingRequest,
    MeetingResponse,
    TentativelyAcceptItem,
    _Booking,
)
from .contact import Contact, DistributionList, Persona
from .item import BaseItem, Item
from .message import ForwardItem, Message, ReplyAllToItem, ReplyToItem
from .post import PostItem, PostReplyItem
from .task import Task

# Traversal enums
SHALLOW = "Shallow"
SOFT_DELETED = "SoftDeleted"
ASSOCIATED = "Associated"
ITEM_TRAVERSAL_CHOICES = (SHALLOW, SOFT_DELETED, ASSOCIATED)

# Contacts search (ResolveNames) scope enums
ACTIVE_DIRECTORY = "ActiveDirectory"
ACTIVE_DIRECTORY_CONTACTS = "ActiveDirectoryContacts"
CONTACTS = "Contacts"
CONTACTS_ACTIVE_DIRECTORY = "ContactsActiveDirectory"
SEARCH_SCOPE_CHOICES = (ACTIVE_DIRECTORY, ACTIVE_DIRECTORY_CONTACTS, CONTACTS, CONTACTS_ACTIVE_DIRECTORY)


ITEM_CLASSES = (
    _Booking,
    CalendarItem,
    Contact,
    DistributionList,
    Item,
    Message,
    MeetingMessage,
    MeetingRequest,
    MeetingResponse,
    MeetingCancellation,
    PostItem,
    Task,
)
TASK_ITEM_CLASSES = (Task,)
CONTACT_ITEM_CLASSES = (Contact, DistributionList)
MESSAGE_ITEM_CLASSES = (Message, MeetingRequest, MeetingResponse, MeetingCancellation)

__all__ = [
    "ACTIVE_DIRECTORY",
    "ACTIVE_DIRECTORY_CONTACTS",
    "AFFECTED_TASK_OCCURRENCES_CHOICES",
    "ALL_OCCURRENCES",
    "ALL_PROPERTIES",
    "ALWAYS_OVERWRITE",
    "ASSOCIATED",
    "AUTO_RESOLVE",
    "AcceptItem",
    "BaseItem",
    "BulkCreateResult",
    "CONFERENCE_TYPES",
    "CONFLICT_RESOLUTION_CHOICES",
    "CONTACT_ITEM_CLASSES",
    "CONTACTS",
    "CONTACTS_ACTIVE_DIRECTORY",
    "CalendarItem",
    "CancelCalendarItem",
    "Contact",
    "DEFAULT",
    "DELETE_TYPE_CHOICES",
    "DeclineItem",
    "DistributionList",
    "ForwardItem",
    "HARD_DELETE",
    "ID_ONLY",
    "ITEM_CLASSES",
    "ITEM_TRAVERSAL_CHOICES",
    "Item",
    "MESSAGE_DISPOSITION_CHOICES",
    "MESSAGE_ITEM_CLASSES",
    "MOVE_TO_DELETED_ITEMS",
    "TASK_ITEM_CLASSES",
    "MeetingCancellation",
    "MeetingRequest",
    "MeetingResponse",
    "Message",
    "NEVER_OVERWRITE",
    "Persona",
    "PostItem",
    "PostReplyItem",
    "RegisterMixIn",
    "ReplyAllToItem",
    "ReplyToItem",
    "SAVE_ONLY",
    "SEARCH_SCOPE_CHOICES",
    "SEND_AND_SAVE_COPY",
    "SEND_MEETING_CANCELLATIONS_CHOICES",
    "SEND_MEETING_INVITATIONS_AND_CANCELLATIONS_CHOICES",
    "SEND_MEETING_INVITATIONS_CHOICES",
    "SEND_ONLY",
    "SEND_ONLY_TO_ALL",
    "SEND_ONLY_TO_CHANGED",
    "SEND_TO_ALL_AND_SAVE_COPY",
    "SEND_TO_CHANGED_AND_SAVE_COPY",
    "SEND_TO_NONE",
    "SHALLOW",
    "SHAPE_CHOICES",
    "SOFT_DELETE",
    "SOFT_DELETED",
    "SPECIFIED_OCCURRENCE_ONLY",
    "Task",
    "TentativelyAcceptItem",
]
