# Share previews before publishing

Every new static HTML page must include Open Graph title, description, absolute canonical URL, absolute representative image URL, MIME type, width and height in its initial HTML head. Do not add them only with JavaScript. Use an original or licensed 1200 x 630 JPEG under images/share, keep important text away from the edges, and inspect the image before publishing. Keep old image URLs available after revisions.

Run `python scripts/share_metadata.py --apply` and review the changes. This adds defaults only where metadata is missing; it does not replace page-specific covers. Run `python scripts/share_metadata.py --check` before every push. The shared publishing helper runs this check. Other publishing routes must also run it.

Existing `#article=` reader URLs share the same server-side index.html. Crawlers do not receive the URL fragment, so per-article cards require independent static HTML URLs. The index fallback is a magazine cover, not a claim that article-specific sharing exists.

After deployment, verify the live HTML and fetch the og:image with image decoding. Use https://developers.facebook.com/tools/debug/ with the exact shared page URL and request a new scrape. A previous text-only post may not have any share attachment to refresh. Do not delete or replace user posts without approval.

## Current public RSS snapshot

Run `python scripts/sync_youtube.py` before publishing. It checks the channel's public RSS, accepts only dated titles and valid video IDs, keeps the latest issue and retains the prior snapshot if the fetch or parse fails. A proposed hourly Actions workflow could not be installed because the current token lacks workflow scope. Run this script from the existing daily publication process; do not assume hosted hourly automation is active. The initial HTML contains a direct text link outside the player, so a blocked iframe or disabled JavaScript does not remove the viewing route. Innovation Magazine's own broadcast is not published and must not borrow DailyShot episodes as its own.

All published article HTML carries its own OG/Twitter title, description, URL and locale. Representative images are externally hosted1200×630 PNGs, not new repository media. Existing crawlers may cache an earlier preview until refreshed by that platform. A working image URL is not evidence that all third-party crawlers have refreshed their cache.
