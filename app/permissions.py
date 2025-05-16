from rest_framework import permissions


class GlobalDefaultPermissions(permissions.BasePermission):
    def has_permission(
        self, request, view
    ):   # verifica se o usuario que esta fazendo a requisição tem o nivel de acesso necessario para a ação que esta tentando executar
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )

        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(
        self, method, view
    ):   # recebe o nome da app e da model e da ação do usuario para verificar se ele tem permissões
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None

    def __get_action_sufix(
        self, method
    ):   # recebe o tipo da requição e converte no controle de acesso equivalente usado pelo django admin
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
