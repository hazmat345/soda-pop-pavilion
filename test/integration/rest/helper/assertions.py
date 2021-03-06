from brewtils.errors import BrewmasterValidationError


def assert_system_running(client, system_name, system_version, **kwargs):
    system = client.find_unique_system(name=system_name, version=system_version)
    system_attrs = kwargs.pop('system', {})
    for key, value in system_attrs.items():
        actual = getattr(system, key)
        assert value == actual, "%s did not match. Expected (%s)\n Got: (%s)" % (key, value, actual)

    for instance in system.instances:
        assert_instance_running(instance, **kwargs)


def assert_instance_running(instance, **kwargs):
    assert instance.status == "RUNNING", "status did not match. Expected (RUNNING) got (%s)" % instance.status


def assert_validation_error(testcase, client, request, **kwargs):
    assert_error_creating_request(testcase, client, request, BrewmasterValidationError, **kwargs)


def assert_error_creating_request(testcase, client, request, exc_class, regex=None, **kwargs):
    if regex is None:
        with testcase.assertRaises(exc_class) as ex:
            created_request = client.create_request(request)
            print("Uh-oh. Request (%s) should have errored, but didn't." % created_request.id)
    else:
        with testcase.assertRaisesRegexp(exc_class, regex) as ex:
            created_request = client.create_request(request)
            print("Uh-oh. Request (%s) should have errored, but didn't." % created_request.id)

    the_exception = ex.exception
    for k in kwargs.keys():
        assert getattr(the_exception, k) == kwargs[k], "Exception was thrown, but %s did " \
                                                       "not match. Expected (%s) got (%s)" % \
                                                       (k, kwargs[k], getattr(the_exception, k))


def assert_successful_request(request, **kwargs):
    assert_request(request, status='SUCCESS', **kwargs)


def assert_errored_request(request, **kwargs):
    assert_request(request, status='ERROR', **kwargs)


def assert_request(request, **kwargs):
    for key in kwargs.keys():
        actual = getattr(request, key)
        expected = kwargs[key]
        if key == "error_class" and not isinstance(expected, str):
            expected = type(expected).__name__

        assert actual == expected, "%s did not match. Expected (%s) got (%s)" % (key, expected, actual)
