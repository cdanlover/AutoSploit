from autosploit.main import main
from lib.output import error
from lib.page_generator import HtmlPageGenerator


if __name__ == "__main__":
    output = HtmlPageGenerator(
        ["/test/rce/something", "/test/something/else"],
        ["/test/a/failure", "/test/some/other/failure"],
        23
    ).generator()
    print output
    exit(1)
    try:
        main()
    except KeyboardInterrupt:
        error("user aborted session")
