import argparse


def main(*args, **kwargs):
    parser = argparse.ArgumentParser()

    cli_group = parser.add_argument_group("cli", "options to configure a single run scan")
    cli_group.add_argument()

    web_group = parser.add_argument_group("web", "options to configure the web server")
    web_group.add_argument("-p", "--port", action="store", default=5000)

    parser.parse_args(*args, **kwargs)


if __name__ == "__main__":
    main()
