# Publication checks

Before every publication:

1. Verify dates, sources, media rights and the magazine identity.
2. Place a short reader-importance block after the article heading/deck. Use `article-importance-block.py` with one to three editor-verified sentences. State what changes for readers and separate proposals from adopted policy. Do not derive factual sentences from a title alone. Existing articles are not bulk-summarized.
3. Run `python scripts/publication-title-gate.py`. The reviewed baseline permits only unchanged third-party titles and compound-word contexts. Any new context stops the push and needs semantic review, never an automatic allowlist addition.
4. Inspect phone and desktop pixels. Verify links and embedded-video titles, magazine/section matching and publication dates.
5. For the general magazine, run `python scripts/sync-broadcast-rss.py` during publication. The snapshot excludes the Innovation sections; content dates and public release dates are kept separate.
6. Update the publication manifest immediately when new articles are published. A UI-only correction does not count as a new article.

Publish through `scripts/publish-checked.sh origin HEAD:main`, which runs the title gate and whitespace check before pushing. Do not rely on Git hooks: the execution environment can disable them. Preserve media on Drive and do not copy new large media into this repository.

Image credit standard: description, creator, provider, rights, verified original URL, and edits. Use `article-image-credit.py` only with inspected rights evidence. Preserve existing captions and merge manually rather than duplicate. A publicly viewable image is not automatically reusable. Keep illustration vs documentary-photo qualifications.
