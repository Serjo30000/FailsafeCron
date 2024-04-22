from failsafe_cron.repositories.info_data_repository import InfoDataRepository


class InfoDataService:
    def __init__(self):
        self.repo = InfoDataRepository()

    def create_info_data(self, data):
        return self.repo.create(data)

    def get_info_data_by_id(self, id_):
        return self.repo.read(id_)

    def get_all_info_data(self):
        return self.repo.read_all()

    def update_info_data(self, id_, new_data):
        self.repo.update(id_, new_data)

    def delete_info_data(self, id_):
        self.repo.delete(id_)

    def number_of_models(self):
        return len(self.repo.read_all())