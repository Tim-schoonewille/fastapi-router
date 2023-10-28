import os

from fastapi import FastAPI


class FastAPIRouter:
    def __init__(
        self,
        root_path: str = 'app/routers',
        exclude_folders: list[str] = ['__pycache__'],
        exclude_files: list[str] = ['__init__.py']
    ) -> None:
        self.root_path = root_path
        self.exclude_folders = exclude_folders
        self.exclude_files = exclude_files

    def init_routers(self, app: FastAPI, folder: str = ''):
        current_folder = os.path.join(self.root_path, folder)
        sub_folders = [
            sub_folder
            for sub_folder in os.listdir(current_folder)
            if os.path.isdir(os.path.join(current_folder, sub_folder))
            and sub_folder not in self.exclude_folders
        ]

        router_path = "app.routers." + (folder + "." if folder else "")
        router_files = [
            filename[:-3]
            for filename in os.listdir(current_folder)
            if filename.endswith(".py") and filename not in self.exclude_files
        ]
        router_import_path = router_path.replace("/", ".")
        for router_name in router_files:
            router_module = __import__(
                router_import_path + router_name, fromlist=["router"]
            )
            router = router_module.router
            app.include_router(router)

        for sub_folder in sub_folders:
            new_folder = (
                os.path.join(folder, sub_folder)
                if folder
                else sub_folder
            )
            self.init_routers(app, new_folder)
