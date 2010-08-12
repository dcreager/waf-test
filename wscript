def set_options(opt):
    opt.tool_options("compiler_cc")
    opt.tool_options("osx")
    opt.tool_options("unittestw")


def configure(conf):
    conf.check_tool("compiler_cc")
    conf.check_tool("osx")
    conf.check_tool("unittestw")


def build(bld):
    bld(
        features="cc cshlib",
        source = bld.path.ant_glob("src/*.c"),
        includes = ["src"],
        target = "foobar",
        vnum = "0.0.0",
        export_incdirs = ["src"],
    )

    bld(
        features="cc cprogram test",
        source = "tests/test.c",
        target = "tests/test",
        uselib_local = "foobar",
        install_path = None,
    )

    import unittestw
    bld.add_post_fun(unittestw.summary)
