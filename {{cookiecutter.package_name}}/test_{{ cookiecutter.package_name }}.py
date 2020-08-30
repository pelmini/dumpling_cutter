"""Default test module"""
import {{ cookiecutter.package_name }}


def test_main_001():
    """Default test function"""
    result = {{ cookiecutter.package_name }}.main()  # pylint: disable=assignment-from-no-return
    assert not result
