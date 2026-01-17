#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]

PACKAGES_DIR = REPO_ROOT / "packages"
POSTS_DIR = REPO_ROOT / "_posts"
PUBLIC_IMG_DIR = REPO_ROOT / "assets" / "img"

FRONT_MATTER_DATE_RE = re.compile(r"^date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})\s*$", re.MULTILINE)

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\-]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "post"

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")

def write_text(p: Path, content: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def get_post_date_from_front_matter(md: str) -> Optional[str]:
    m = FRONT_MATTER_DATE_RE.search(md)
    return m.group(1) if m else None

def find_single_package() -> Tuple[str, Path]:
    """
    If multiple packages exist, we publish all. This helper is only used for messages/logging.
    """
    if not PACKAGES_DIR.is_dir():
        raise FileNotFoundError("packages/ directory not found.")
    pkgs = [p for p in PACKAGES_DIR.iterdir() if p.is_dir()]
    if not pkgs:
        raise FileNotFoundError("No packages found under packages/.")
    # Prefer the most recently modified package folder
    pkgs.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return pkgs[0].name, pkgs[0]

def publish_one(pkg_dir: Path) -> None:
    slug = slugify(pkg_dir.name)

    post_md = pkg_dir / "post.md"
    assets_dir = pkg_dir / "assets"

    if not post_md.is_file():
        raise FileNotFoundError(f"Missing {post_md}")

    md = read_text(post_md)
    post_date = get_post_date_from_front_matter(md)
    if not post_date:
        raise RuntimeError(
            f"post.md in {pkg_dir} is missing a 'date: YYYY-MM-DD' in front matter. "
            "Run ingest with --front-matter and --post-date."
        )

    # Write _posts/YYYY-MM-DD-slug.md
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    out_post = POSTS_DIR / f"{post_date}-{slug}.md"
    write_text(out_post, md)

    # Copy assets -> assets/img/<slug>/
    if assets_dir.is_dir():
        dest = PUBLIC_IMG_DIR / slug
        dest.mkdir(parents=True, exist_ok=True)
        for f in assets_dir.iterdir():
            if f.is_file():
                shutil.copy2(f, dest / f.name)

def main() -> int:
    if not PACKAGES_DIR.is_dir():
        print("[+] No packages/ directory. Nothing to publish.")
        return 0

    pkg_dirs = [p for p in PACKAGES_DIR.iterdir() if p.is_dir()]
    if not pkg_dirs:
        print("[+] No package folders found. Nothing to publish.")
        return 0

    published = 0
    for pkg in sorted(pkg_dirs):
        try:
            publish_one(pkg)
            print(f"[+] Published package: {pkg.name}")
            published += 1
        except Exception as e:
            print(f"[!] Failed publishing package {pkg.name}: {e}")
            return 2

    print(f"[+] Done. Published {published} package(s).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
