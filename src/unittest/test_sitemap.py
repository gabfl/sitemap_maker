import unittest
import tempfile
import os.path

from .. import sitemap


class Test(unittest.TestCase):

    def setUp(self):
        sitemap.exclude_paths = ['/contact', '/articles']

    def test_crawl_site(self):

        crawl = sitemap.crawl_site('https://www.github.com/', max_crawl=5)
        assert crawl is None

    def test_get_last_modified(self):

        # The output format should be YYYY-MM-DD
        lm = sitemap.get_last_modified('https://www.gab.lc/')
        assert isinstance(lm, str)
        assert len(lm) == 10

        # Test with no last-modified header
        assert sitemap.get_last_modified(
            'https://www.gab.lc/some_404_page') is None

    def test_write_sitemap(self):

        sitemap_file = tempfile.NamedTemporaryFile()

        # Crawl website, write file
        crawl = sitemap.crawl_site(
            'https://www.gab.lc/', max_crawl=20, depth=4)
        sitemap.write_sitemap(sitemap_file.name, verbose=True)

        # Ensure sitemap exists
        assert os.path.isfile(sitemap_file.name)

        # Read sitemap content
        with open(sitemap_file.name) as f:
            sitemap_content = f.read()

        print(sitemap_content)

        assert sitemap_content.startswith(
            '<?xml version="1.0" encoding="UTF-8"?>')
        assert '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' in sitemap_content
        assert '<url>' in sitemap_content
        assert '<loc>https://www.gab.lc</loc>' in sitemap_content
        assert '<lastmod>' in sitemap_content
        assert '</lastmod>' in sitemap_content
        assert '</url>' in sitemap_content
        assert sitemap_content.endswith("</urlset>\n")
