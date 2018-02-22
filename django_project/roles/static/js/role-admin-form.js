(function ($) {
    $(document).ready(function () {
        setTimeout(function () {
            var rolesJson = JSON.parse($('.field-all_roles_permissions').find(".readonly").text());
            $("#id_groups_add_link").click(function () {
                renderRolePermissions()
            });
            $("#id_groups_remove_link").click(function () {
                renderRolePermissions()
            });
            function renderRolePermissions() {
                var permissions = [];
                $("#id_groups_to option").each(function (index, element) {
                    permissions = $.merge(permissions, rolesJson[$(element).text()]);
                });
                if (permissions.length > 0) {
                    $(".field-role_permissions .readonly").html(permissions.join('<br>'));
                } else {
                    $(".field-role_permissions .readonly").html('-');
                }
            }
        }, 500);

    });
})(django.jQuery);