import reloaded.configs as configs


def test_config():
    if configs.get_config_file():
        assert True


def test_browser():
    if configs.settings['browser']:
        assert True


def test_username():
    if configs.settings['username']:
        assert True


def test_password():
    if configs.settings['password']:
        assert True


def test_workshop_site():
    if configs.settings['workshop_site']:
        assert True
