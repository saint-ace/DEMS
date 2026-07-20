from apps.rbac.permissions import HasPermission


class CanViewCase(HasPermission):
    required_permission = "cases.view"


class CanCreateCase(HasPermission):
    required_permission = "cases.create"


class CanUpdateCase(HasPermission):
    required_permission = "cases.update"


class CanDeleteCase(HasPermission):
    required_permission = "cases.delete"


class CanAssignCase(HasPermission):
    required_permission = "cases.assign"


class CanCloseCase(HasPermission):
    required_permission = "cases.close"


class CanArchiveCase(HasPermission):
    required_permission = "cases.archive"