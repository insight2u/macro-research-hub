# Favorite-media newsroom

The magazine's `#nr-media` is the only automatic news-video player. The older portal retains its music controls, not its old fixed news IDs.

The four source media were recovered from the magazine's actual imported favorites: Bloomberg.com, 연합뉴스, 뉴스타파, 오마이뉴스. Channel bindings were recovered from their official sites. Keep those bindings and source links, do not broaden the favorites list silently.

Refresh public sources during the existing 00:30 magazine publishing and 21:00 source-prefetch steps, reusing the day's manifest. Do not duplicate the broadcast host's rendering. No authenticated-account polling or new recurring timer is needed. The 90-second timer in the reader changes among already-fetched videos only; it does not poll sources. Provider live video itself continues live.

Run `python scripts/refresh_favorite_news.py --output-dir /tmp/favorite-news-refresh`. Read its errors. It retrieves public channel listings and public Atom feeds, excludes upcoming streams, retains observed LIVE metadata, extracts observed watch URLs, interleaves sources, removes repeated video IDs, and includes original upload dates when available. A failed source check must not be called a fresh success. Reuse the last verified source entry with its original timestamp only if clearly labeled, or omit that source.

Update `favorite-news.json` and the JSON contents of `<script type="application/json" id="nm-data">` in the current live `index.html` from the same verified manifest. Preserve all other site changes. Verify current repository HEAD before a non-force commit. Never overwrite from an old local copy. The embed renderer reads that embedded manifest. Do not call an old snapshot current or call every recording live.

Before committing: validate source authors and official embed availability with the provider's oEmbed endpoint; no video download or reupload is needed. Inspect actual desktop/mobile pixels. Test the ten distinct videos, previous/next, pause/resume, live pinning, reload continuation, source links, and archive/CTA regression checks. After deployment, verify actual new HTML and pixels at a fresh URL. Do not treat a commit as a completed deployment.
