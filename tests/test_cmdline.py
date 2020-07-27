import auto_cmdline.cmdline as cmdline


def test_project_defines_author_and_version():
    assert cmdline.add_argparser()
