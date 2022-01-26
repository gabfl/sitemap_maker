# sitemap_maker

[![Pypi](https://img.shields.io/pypi/v/sitemap_maker.svg)](https://pypi.org/project/sitemap_maker)
[![Build Status](https://github.com/gabfl/sitemap_maker/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/gabfl/sitemap_maker/actions)
[![codecov](https://codecov.io/gh/gabfl/sitemap_maker/branch/main/graph/badge.svg)](https://codecov.io/gh/gabfl/sitemap_maker)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/gabfl/sitemap_maker/main/LICENSE)

Python tool to generate sitemap XML files.

This tool relies mainly on the Python crawler [sitecrawl](https://github.com/gabfl/sitecrawl).

## Installation

Using pip:

```bash
pip3 install sitemap_maker

sitemap_maker --help
```

Or build from sources:

```bash
# Clone project
git clone https://github.com/gabfl/sitemap_maker && cd sitemap_maker

# Installation
pip3 install .
```

### Usage

```bash
sitemap_maker --url https://www.weather.gov/ \
    --sitemap output.xml \
    --depth 1 \
    --verbose \
    --max 5 \
    --no_pound

# For help:
# sitemap_maker --help
```

Will create a file `sitemap.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.weather.gov</loc>
  </url>
  <url>
    <loc>https://www.weather.gov/wrh/climate</loc>
  </url>
  <url>
    <loc>https://www.weather.gov/safety/flood</loc>
  </url>
  <url>
    <loc>https://www.weather.gov/safety/tsunami</loc>
  </url>
  <url>
    <loc>https://www.weather.gov/safety/beachhazards</loc>
  </url>
</urlset>
```