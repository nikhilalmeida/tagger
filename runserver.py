from selftag import app
from selftag.connections import init_db, insert_images


def main():
    init_db()
    insert_images()
    app.run()


if __name__ == '__main__':
    main()