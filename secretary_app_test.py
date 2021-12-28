import app

get_all_doc_owners_names_return_value = {'Геннадий Покемонов', 'Аристарх Павлов', 'Василий Гупкин'}


class TestSecretaryApp:

    def setup(self):
        print('method setup')

    def teardown(self):
        print('method teardown')

    def test_get_doc_owner_name(self):
        assert app.get_doc_owner_name() == "Геннадий Покемонов"

    def test_get_all_doc_owners_names(self):
        assert app.get_all_doc_owners_names() == get_all_doc_owners_names_return_value

    def test_add_new_doc(self):
        assert app.add_new_doc() == '2'

    def test_delete_doc(self):
        assert app.delete_doc() == ('10006', True)



