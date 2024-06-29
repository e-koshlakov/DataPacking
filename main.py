import pickle


class CountryState:
    def __init__(self):
        self.__country_state_dict = {}

    def add_country(self, country, state):
        self.__country_state_dict[country] = state
        print(f"Страна '{country}' с столицей '{state}' добавлена.")
        return self.__country_state_dict

    def remove_country(self, country):
        if country in self.__country_state_dict:
            del self.__country_state_dict[country]
            print(f"Страна '{country}' удалена из словаря.")
            return self.__country_state_dict
        else:
            print('Такой страны нет в словаре.')

    def find_value_by_key(self, country):
        if country in self.__country_state_dict:
            capital = self.__country_state_dict[country]
            print(f"Столица страны '{country}' - '{capital}'.")
            return capital
        else:
            print('Такой страны нет в словаре.')

    def find_key_by_value(self, capital):
        if capital in self.__country_state_dict.values():
            for key, value in self.__country_state_dict.items():
                if value == capital:
                    print(f"Страна со столицей '{capital}' - '{key}'.")
                    return key
        else:
            print('Такой столицы нет в словаре.')

    def edit_value_by_key(self, country, new_value):
        if country in self.__country_state_dict:
            old_value = self.__country_state_dict[country]
            self.__country_state_dict[country] = new_value
            print(f"Столица страны '{country}' изменена с '{old_value}' на '{new_value}'.")
            return self.__country_state_dict
        else:
            print('Такой страны нет в словаре, нечего редактировать.')

    def pickle_data_to_file(self):
        with open('countries.pkl', 'wb') as file:
            pickle.dump(self.__country_state_dict, file)
        print("Данные были записаны в файл 'countries.pkl'")
        return True

    def unpickle_data_from_file(self):
        with open('countries.pkl', 'rb') as file:
            self.__country_state_dict = pickle.load(file)
        print("Данные были успешно загружены из файла 'countries.pkl'.")
        return self.__country_state_dict


my_country = CountryState()
print(my_country.add_country('Russia', 'Moscow'))
print(my_country.add_country('Belarus', 'Minsk'))
print(my_country.remove_country('Russia'))
print(my_country.find_value_by_key('Belarus'))
print(my_country.find_key_by_value('Minsk'))
print(my_country.edit_value_by_key('Belarus', 'Grodno'))
print(my_country.edit_value_by_key('Belarus', 'Minsk'))
print(my_country.pickle_data_to_file())
print(my_country.unpickle_data_from_file())
