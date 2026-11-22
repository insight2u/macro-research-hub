# International newsroom

The homepage contains 10 editorial slots of about90 seconds: seven verified live broadcasts and three selected official news recordings. Initial allocation: US30%, Korea20%, Europe20%, China10%, Japan10%, Qatar10%. This is an editorial weighting, not a measured influence ranking. Actual viewing share changes when channels end, block a region, require sign-in or fail.

Player: official YouTube IFrame API; muted autoplay; explicit retry; 90-second visible exposure countdown; pause offscreen or in hidden tab; resume on return; skip errors and nonadvancing clocks; bounded cooldown; stop with original links if everything fails. Pinning stops rotation but does not override provider restrictions. No stream copying or paywall bypass.

CNN HLN is not the same as the selected CNN recorded news. HLN official access guidance requires a participating TV-provider subscription. Do not relabel CNN clips as HLN.

Refresh uses the existing regional slots. scripts/refresh_favorite_news.py proposes source changes for review; it never converts a blocked discovery result into a new verification timestamp. Review current live status, official ownership, embed permission and actual playback before publishing an updated manifest. If unavailable, preserve last verified timestamps, identify the failure and use browser/source checks rather than silently declaring the list fresh.

The old bottom portal remains stored unchanged inside preserved-portal but is display:none. Its visible navigation is hidden and the main browse button opens the current searchable article archive. All144articles,135leads,4142reference entries and existing per-article broadcast links remain. Existing consultation UI is detached from the hidden old layout but its recipient route has not been changed pending a verified direct chat URL.


## Daily editorial placement, effective 22 November 2026

Keep the ten canonical desks, but do not cap the number of daily articles at ten. Today's Book is one daily ordinary article in 도파민성애자, with a book or related-book review, actual cover, YES24 link, short author biography and clearly stated reading scope. John Lee's November22 video analysis is ordinary personal-finance coverage in 마이다스의 Z-Tech; preserve its original standalone URL and source video.

For each new owner-requested article, run `python scripts/classify_article.py --file PATH --title TITLE` before creating the registry record. Read the text and the ranking, choose one of the ten existing desks, and record any semantic override reason in the internal publication ledger. The tool uses an editorial keyword feature map and pooled-diagonal shrinkage linear discriminant ranking, plus explicit book/personal-finance format rules. Scores are not probabilities. No validated out-of-sample accuracy is claimed. Existing historical records are never silently reclassified.

SPECIAL NEWS is an independent main-page feature, not a weekend-only edition. Discuss each day's topic with the owner before writing; one approved main story, full feature and about five related pieces are the daily target. Keep the previous special pinned until its successor is actually published. Do not count the regular ten articles or merely relabel old series as a newly produced special. The separate Monday weekly domestic/overseas research pair remains a separate commitment.


## Daily singer and film coverage, effective22November2026

Owner request phonemsg-01M80E5SJ2Z12K3BGXNX4DDFXC adds at least one singer-focused and one film-focused ordinary article every day to 도파민성애자, alongside TodayBook and beyond the basic ten. Four daily languages: Korean, English, simplified Chinese, Japanese. Owner topic instructions may create further ordinary articles beyond ten. Run the classifier and semantic review, preserve the ten desks.

The owner-provided Music and Movie source collections are required references. Read their relevant child pages separately if recursive reads truncate. Use the private production record to recover their locations. Do not edit the original collection. Record actual inspected scope; a stored link is not evidence that its transcript or rights were checked. Do not expose private notebook links in public articles. Reverify claims in primary sources.

Maintain a reviewed critic/broadcaster registry. Separate current feeds, archive-only programs and unverified creator channels; never infer official status from a channel name. Link the actual official song/performance or film/trailer separately from commentary, record original event and upload dates, no copied lyrics or downloaded film/music footage. Official viewing is not permission to reupload. Explicitly state limited viewing/reading scope without claiming full-film or complete-discography review. Publish sequentially magazine, Facebook-style text, audio, podcast, Spotify, YouTube under each owner's existing authority, not by counting a draft as a publication.

Send SUN through main a dated JSON ledger with type/title/subject, per-language and per-medium status/URL/check time, official-video URL and verification grounds. Use null/unverified/pending for absent values. Registry review itself is not article publication.


22Nov2026 replacement: owner requested TheLastEmperor instead of Mabu. The Mabu registry entry is held out of the live article list; all four original Markdown manuscripts and their existing translation data are preserved, not deleted. Production keeps a recovery copy of the registry row. Restore only when assigned. The source files remain in this public repository; holding an article out of the reader is not a confidentiality guarantee for previously published source text. The Last Emperor guide separates1911 revolution/1912 abdication,1932 Manchukuo/1934 imperial accession,1966-76 CulturalRevolution/Puyi1967 death, and1987 film/1988 Oscar/2008 recording metadata. Score credit names Sakamoto,Byrne,CongSu.
