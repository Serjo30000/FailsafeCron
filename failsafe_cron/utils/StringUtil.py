class StringUtil:
    @staticmethod
    def print_number_of_models_before(number_of_models):
        print("Number of models in database before script:", number_of_models)

    @staticmethod
    def print_number_of_models_after(number_of_models):
        print("Number of models in database after script:", number_of_models)

    @staticmethod
    def print_lock():
        print("\nLOCK\n")

    @staticmethod
    def print_skip():
        print("\nSKIP\n")