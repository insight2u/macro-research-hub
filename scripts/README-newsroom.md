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
